import requests
import unittest
"""
Объективно, самая сложная часть для меня. Не знал нужно ли комментить в коде или написать все замечания сюда, решил сюда
1. Перепутаны буквы K C F, фаренгейт указано верно, только с маленькой буквы, поэтому не матчится. 
2. Лимиты странные, где-то граничные значения дублируются в смежных отрезках, где-то нет.
3. Если использовать температуру без индекса то на запросы с отрицательными числами, будет валиться 500
4. Температура с точкой обрабатывается так: если без индекса - 500, если c индексом то unknown (что есть неправда) должно
быть Invalid temperature, как в случае с буквами например.
5. Ниже приведен список тестов. почти все, конечно, падают. Там еще должны быть тесты на граничные значения, я про них 
помню, но зачем-то взял себе слишком мало времени на тестовое задание и не успеваю :).
"""

class TestApiTemp(unittest.TestCase):

    def test_c_ice(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=-10C')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'ice'" == string)

    def test_c_liquid(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=10C')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'liquid'" == string)

    def test_c_steam(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=105C')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'steam'" == string)

    def test_k_ice(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=263K')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'ice'" == string)

    def test_k_liquid(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=283K')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'liquid'" == string)

    def test_k_steam(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=378K')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'steam'" == string)

    def test_f_ice(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=14F')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'ice'" == string)

    def test_f_liquid(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=50F')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'liquid'" == string)

    def test_f_steam(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=221F')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'steam'" == string)

    def test_c_ice_without_mark(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=-10')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'ice'" == string)

    def test_c_liquid_without_mark(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=10')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'liquid'" == string)

    def test_c_steam_without_mark(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=105')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'steam'" == string)

    def test_c_unknown_without_mark(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=0')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'unknown'" == string)

    def test_c_unknown(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=0C')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'unknown'" == string)

    def test_k_unknown(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=999K')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'unknown'" == string)

    def test_f_unknown(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=-9999F')
        self.assertTrue(response.status_code == 200)
        string = str(response.content)
        self.assertTrue("b'unknown'" == string)

    def test_not_int(self):
        response = requests.get('http://localhost:8888/temperature_check?temperature=abc')
        self.assertTrue(response.status_code == 400)






if __name__ == '__main__':
    unittest.main()
