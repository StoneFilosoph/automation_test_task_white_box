
# This code check what search service is available
"""Этот код проверяет доступность сервиса, однако в коде нет ни одной обработки если сервис таки недоступен это 1.
2 в тексте задания написано что это граббер ссылок, в моем понимании граббер ссылок это инструмент позволяющий забирать
ссылки откуда-то. тут же мы забираем всё тело по урл. очень странно.
"""
# coding: utf-8
NEEDED_URLS = ['https://google.com/', 'https://www.semrush.com/', 'https://yandex.ru/time/', 'https://yandex.ru/time/']
# Нужен двойной отступ
def get_fetch_urls(urls, cache={}): # Добавить комментарий по функции, и так со всеми функциями,кассами
    """Это комментарий описывающий, что делает функция

    :param urls: параметр принимает список урл для проверки
    :param cache:
    :return: Что возвращает функция
    """
    import requests
    """
    Импорты поместить в начале файла, до объявления переменных, так далее для всех импортов
    """
    urls_size = len(urls)
    result = []

    while urls_size:
        url = urls.pop()
        if url in cache:
            print('url in cache ' + url)
            result.append(cache[url])

        response = requests.get(url) # может быть добавим try catch если что-то пойдет не так?
        body = response.content
        cache[url] = body
        result.append(body)
        urls_size -= 1

    return result
def get_full_moon_phase(): # Снова описание функции + двойной отступ.
    import time # Унести импорт в начало файла
    time.sleep(5) # Явно ненужный слип 1
    import random # Унести импорт в начало файла
    time.sleep(5) # Явно ненужный слип 2
    return random.choice([True, False])
# Здесь нужно 2 отступа
class UrlGetter:
    debug_mode_by_moon_phase = get_full_moon_phase() # Во всем классе данный метод используется один раз можно оставить
    # просто random.choice([True, False]) и не плодить лишних сущностей

    fetched_urls = []

    def __init__(self, fetched_urls):
        self.fetched_urls.extend(fetched_urls)

    def get_urls_data(self, urls):
        not_fetched_urls = []
        if self.debug_mode_by_moon_phase:
            for url in urls:
                print(url)
        for url in urls:
            if url not in self.fetched_urls:
                not_fetched_urls.append(url)
        data = get_fetch_urls(not_fetched_urls)
        self.fetched_urls.extend(not_fetched_urls)
        return data

    def check_url_not_fetched(self, url):
        if self.debug_mode_by_moon_phase:
            print(url in self.fetched_urls)
        return bool(url in self.fetched_urls)

# my tests
"""
В тестах совершенно непонятно что и где проверяется, если не использовать фреймворк для юниттестов, то лучше всего
оформить их в виде методов класса с говорящими названиями. 
например:
class checkUrlsAvailabilityTests:
       def check_get_fetch_urls()
таким образом даже в сложном коде можно будет разобрать какой тест какой метод проверяет.
"""
fetched_urls = ['https://google.com/']
getter = UrlGetter(fetched_urls)
for url in NEEDED_URLS:
    print(getter.check_url_not_fetched(url))
reuzuult1 = getter.get_urls_data(NEEDED_URLS)

import time
time.sleep(5) # не очень понятный слип

fetched_urls = ['https://google.com/'] # Зачем снова объявлять эту переменную? тем более если дальше используется
# NEEDED_URLS
getter = UrlGetter(fetched_urls)
reuzuult2 = getter.get_urls_data(NEEDED_URLS)


import os # Импорт унести вверх
file = open(os.getcwd()+'/data1.html', 'wb') # Для работы с файлами лучше использовать оператор контекста with
file.writelines(reuzuult1) # file не закрыт
file2 = open(os.getcwd()+'/data2.html', 'wb')
file2.writelines(reuzuult2) # то же самое file2 остается не закрытым

assert reuzuult1 == reuzuult2 # А должны ли данные быть одинаковыми?

if __name__ == '__main__':
    getter = UrlGetter() # Нельзя создать экземпляр класса без указания переменных прокинутых в __init__
    print(getter.get_urls_data(NEEDED_URLS))
