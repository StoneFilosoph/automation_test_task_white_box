# Этот код описывает локаторы элементов на сайте semrush.com

class PageElement(object):
    def __init__(self,browser):
        self.browser = browser
        self.locator = ""


class MainPage(PageElement):
    """MainPage - Описывает элементы находящиеся на главной странице сайта

    """

    def login_button(self):
        self.locator = "//button[contains(@class,'srf-btn -xs -success srf-login-btn')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element


class LoginFrame(PageElement):
    """LoginFrame - модальное окно с полями для ввода и кнопкой для входа на сайт

    """

    def login_form(self):
        self.locator = "//div[contains(@class,'sso-base-popup-form')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def email_field(self):
        self.locator = "//input[contains(@class,'sc-input__control') and contains(@name,'email')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def password_field(self):
        self.locator = "//input[contains(@class,'sc-input__control') and contains(@name,'password')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def button_to_log_in(self):
        self.locator = "//button[contains(@data-test,'auth-popup__submit')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element


class UserMainPage(PageElement):
    """UserMainPage - Главная страница залогиненого пользователя
    """

    def profile_dropdown(self):
        self.locator = "//div[contains(@data-test,'header-menu__user')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def notes_button(self):
        self.locator = "//a[contains(@data-ga-label, 'notes')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def project_button(self):
        self.locator = "//a[contains(@data-ga-label, 'projects')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element


class NotesPage(PageElement):
    """NotesPage - Элементы на странице заметок

    """

    def add_note_button(self):
        self.locator = "//button[contains(@data-cream-action,'add-note')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def add_note_frame(self):
        self.locator = "//div[contains(@class,'cream-popup notes-editor')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def add_note_name(self):
        self.locator = "//input[contains(@data-cream-ui,'input-title')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def save_note_button(self):
        self.locator = "//button[contains(@data-cream-action,'save')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def lastesl_created_note(self,name):
        self.locator = "//tbody[contains(@data-cream-ui,'items')]/tr[1]/td[2]/span/span[text()=" + name + "]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element


class ProjectPage(PageElement):
    """ProjectPage - Описывает элементы на странице/страницах проектов

    """

    def add_project_button(self):
        self.locator = "//div[contains(@class,'project-create')]/button"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def add_new_project_frame(self):
        self.locator = "//div[contains(@role,'document')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def project_domain_field(self):
        self.locator = "//input[contains(@placeholder,'Enter project domain')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def project_name_field(self):
        self.locator = "//input[contains(@placeholder,'Enter project name')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def create_project_button(self):
        self.locator = "//div[contains(@class,'sc-1_4_7-project-create-modal__actions-buttons')]/button[1]/div"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def dashboard_header(self):
        self.locator = "//span[contains(@class,'pr-page__title-name')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def dashboard_settings(self):
        self.locator = "//span[contains(@class,'s-icon -s -settings')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def delete_project(self):
        self.locator = "//a[contains(@class,'js-remove')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def project_name_to_remove(self):
        self.locator = "//input[contains(@class,'s-input__control js-remove-input')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element

    def approve_deleting(self):
        self.locator = "//button[contains(@class,'s-btn -s -danger js-remove')]"
        element = self.browser.find_element_by_xpath(self.locator)

        return element


