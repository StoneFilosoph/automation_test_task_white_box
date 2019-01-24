import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObject import MainPage, LoginFrame, UserMainPage,NotesPage, ProjectPage
import unittest

"""Сначала думал использовать фрейворк behave с cucumber и всякими такими плюшками, но вышло, что дольше писать
всякую обвязку чем начать писать тесты. тем более что почему-то возникли проблемы запуска firefox на моей виртуалке.
в итоге плюнул, и сделал проще, зато всё. Запихнул в unittest. 
pageobject вобщем получился довольно удобным и расширяемым, им я доволен.

"""

def browser_init():
    """browser_init - Инициализация браузера

    :return: возвращает объект webdriver
    """
    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(
        executable_path='/home/akozlov/testCase/automation_test_task_white_box/task3/chromedriver',
        chrome_options=ch_options)
    return browser


class SemrushUiTests(unittest.TestCase):

    def test_login(self):
        """test_login - тест логин зарегестрированного пользователя

        :return:
        """
        browser = browser_init()
        browser.get('http://semrush.com')
        browser.implicitly_wait(10) # устанавливаем таймер неявного ожидания, если вдруг что-то подтормозит
        browser.maximize_window()
        main_page = MainPage(browser)
        login_frame = LoginFrame(browser)
        login_button = main_page.login_button()
        login_button.click()
        login_form = login_frame.login_form()
        password_field = login_frame.password_field()
        button_to_log_in = login_frame.button_to_log_in()
        email_field = login_frame.email_field()
        email_field.send_keys('stonefilosoph@gmail.com')
        password_field.send_keys('456654852258')
        button_to_log_in.click()
        user_main_page = UserMainPage(browser)
        self.assertTrue(user_main_page.profile_dropdown()) # так проверяем что залогинились
        browser.close()

    def test_note_creating(self):
        """test_note_creating - тест создания заметки

        :return:
        """
        browser = browser_init()
        browser.get('http://semrush.com')
        browser.implicitly_wait(10)
        browser.maximize_window()
        main_page = MainPage(browser)
        login_frame = LoginFrame(browser)
        login_button = main_page.login_button()
        login_button.click()
        login_form = login_frame.login_form()
        password_field = login_frame.password_field()
        button_to_log_in = login_frame.button_to_log_in()
        email_field = login_frame.email_field()
        email_field.send_keys('stonefilosoph@gmail.com')
        password_field.send_keys('456654852258')
        button_to_log_in.click()
        user_main_page = UserMainPage(browser)
        notes_button = user_main_page.notes_button()
        notes_button.click()
        notes_page = NotesPage(browser)
        add_note_button = notes_page.add_note_button()
        add_note_button.click()
        notes_page.add_note_frame()
        add_note_name = notes_page.add_note_name()
        note_name = str(random.randrange(0, 100, 1)) # случайное название заметки
        add_note_name.send_keys(note_name)
        save_note_button = notes_page.save_note_button()
        save_note_button.click()
        self.assertTrue(notes_page.lastesl_created_note(note_name)) # проверяем последнюю созданную заявку
        browser.close()

    def test_project_creating(self):
        """test_project_creating - проверка создания проекта

        :return:
        """
        browser = browser_init()
        browser.get('http://semrush.com')
        browser.implicitly_wait(10)
        browser.maximize_window()
        main_page = MainPage(browser)
        login_frame = LoginFrame(browser)
        login_button = main_page.login_button()
        login_button.click()
        login_form = login_frame.login_form()
        password_field = login_frame.password_field()
        button_to_log_in = login_frame.button_to_log_in()
        email_field = login_frame.email_field()
        email_field.send_keys('stonefilosoph@gmail.com')
        password_field.send_keys('456654852258')
        button_to_log_in.click()
        user_main_page = UserMainPage(browser)
        project_button = user_main_page.project_button()
        project_button.click()
        project_page = ProjectPage(browser)
        add_project_button = project_page.add_project_button()
        add_project_button.click()
        project_page.add_new_project_frame()
        domain_name_field = project_page.project_domain_field()
        domain_name_field.send_keys('abra.com')
        project_name_field = project_page.project_name_field()
        project_name_field.send_keys('cadabra')
        create_project_button = project_page.create_project_button()
        create_project_button.click()
        dashboard_head = project_page.dashboard_header()
        timer = 6
        while timer: # эта конструкция появилась из за react подобного отображения dashboard_header
            try:
                assert 'cadabra' in dashboard_head.text
            except:
                sleep(1)
                timer -= 1
        dashboard_settings = project_page.dashboard_settings()
        dashboard_settings.click()
        delete_project = project_page.delete_project()
        delete_project.click()
        project_name_to_remove = project_page.project_name_to_remove()
        project_name_to_remove.send_keys('cadabra')
        approve_deleting = project_page.approve_deleting()
        approve_deleting.click()
        sleep(1)
        browser.close()


if __name__ == '__main__':
    unittest.main()



