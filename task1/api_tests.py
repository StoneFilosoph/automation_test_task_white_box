import requests
import unittest
"""
Объективно, самая сложная часть для меня. Не знал нужно ли комментить в коде или написать все замечания сюда, решил сюда
1. Перепутаны буквы K C F, фаренгейт указано верно, только с маленькой буквы, поэтому не матчится. 
2. Лимиты странные, где-то граничные значения дублируются в смежных отрезках, где-то нет.
3. Если использовать температуру без индекса то на запросы с отрицательными числами, будет валиться 500
4. Температура с точкой обрабатывается так: если без индекса - 500, если c индексом то unknown (что есть неправда) должно
быть Invalid temperature, как в случае с буквами например.
5. переработан список тестов, разделен на группы, есть отдельные входные параметры (test_data) изменяя которые можно
менять и сами тесты, если что-то изменится в требованиях. Сейчас есть тестирование на граничные значения шкал температур,
тестирование состояний воды во всех шкалах температур, тестирование длинны вводимого значения, тестирование невалидных
данных. тестирование при вводе данных числа с точкой. 
6. Единственное неудобство, что сабтесты не определяются как отдельно прошедшие тесты. Но удобно что определяются 
как отдельное падение, без прерывания выполнения кода остальных вариантов. Отсюда в отчете можно увидеть что-то вроде
Ran 5 tests in 0.907s
FAILED (failures=61)
Однако информация по каждому падению есть, и довольно удобна, для выявления того "что не так"
 """
temp_limits_test_data = {
    'C': {
        'steam': [100, 999999],
        'liquid': [1, 99],
        'ice': [-999999, 0]},
    'K': {
        'steam': [373, 999],
        'liquid': [274, 373],
        'ice': [0, 273]},
    'F': {
        'steam': [212, 9999],
        'liquid': [33, 211],
        'ice': [-9999, 33]}
}
water_condition_test_data = {
    'not_specified': {
        'steam': '300',
        'liquid': '50',
        'ice': '-100',
        'unknown': '9999999'},
    'C': {
        'steam': '300C',
        'liquid': '50C',
        'ice': '-100C',
        'unknown': '9999999C'},
    'K': {
        'steam': '500K',
        'liquid': '300K',
        'ice': '100K',
        'unknown': '1000K'},
    'F': {
        'steam': '1000F',
        'liquid': '100F',
        'ice': '-500F',
        'unknown': '99999F'},

    }
length_test_data = [1, 10]
not_valid_test_data = ['10d', '', '10,5C', 'abc', '&%$', '010C']
float_number_test_data = ['10.5F']


def request_url_temp(temp, base_url='http://localhost:8888/temperature_check?temperature='):
    result_url = base_url + temp

    return result_url


class TestApiTemp(unittest.TestCase):

    def test_water_conditions(self):
        """test_water_conditions тестирование ожидаемых состояний воды

        :return:
        """
        for scale in water_condition_test_data:
            for condition in water_condition_test_data[scale]:
                response = requests.get(request_url_temp(water_condition_test_data[scale][condition]))
                with self.subTest(exp_condition=condition, recievd_condition=str(response.content), test_data=
                water_condition_test_data[scale][condition]):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), condition)

    def tests_of_limits(self):
        """tests_of_limits - Тестирование граничных значений

        :return:
        """
        for scale in temp_limits_test_data:
            for condition in temp_limits_test_data[scale]:
                limit = temp_limits_test_data[scale][condition]
                response = requests.get(request_url_temp(str(limit[0]) + scale))
                with self.subTest(expected_condition=condition, limit=limit[0], recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), condition)
                response = requests.get(request_url_temp(str(limit[0] + 1) + scale))
                with self.subTest(expected_condition=condition, limit=limit[0] + 1, recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), condition)
                response = requests.get(request_url_temp(str(limit[0] - 1) + scale))
                with self.subTest(expected_condition=condition, limit=limit[0] - 1, recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), 'unknown')
                response = requests.get(request_url_temp(str(limit[1]) + scale))
                with self.subTest(expected_condition=condition, limit=limit[1], recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), condition)
                response = requests.get(request_url_temp(str(limit[1] - 1) + scale))
                with self.subTest(expected_condition=condition, limit=limit[1] - 1, recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), condition)
                response = requests.get(request_url_temp(str(limit[1] + 1) + scale))
                with self.subTest(expected_condition=condition, limit=limit[1] + 1, recieved_condition=str(response.content)):
                    self.assertTrue(response.status_code == 200)
                    self.assertRegex(str(response.content), 'unknown')

    def test_input_length(self):
        """test_input_length - Тестирование длинны значения для ввода

        :return:
        """
        result_request_data = ''
        minimum = length_test_data[0] - 1
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0] - 1):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(400 == response.status_code)
            self.assertRegex(str(response.content), 'Invalid temperature')
        result_request_data = ''
        minimum = length_test_data[0]
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0]):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(200 == response.status_code)
        result_request_data = ''
        minimum = length_test_data[0] + 1
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0] + 1):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(200 == response.status_code)

        result_request_data = ''
        minimum = length_test_data[1] + 1
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0] - 1):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(400 == response.status_code)
            self.assertRegex(str(response.content), 'length of value must be at most')
        result_request_data = ''
        minimum = length_test_data[1]
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0]):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(200 == response.status_code)
        result_request_data = ''
        minimum = length_test_data[1] - 1
        while minimum:
            result_request_data += '9'
            minimum -= 1
        with self.subTest(minimum=length_test_data[0] + 1):
            response = requests.get(request_url_temp(result_request_data))
            self.assertTrue(200 == response.status_code)

    def test_not_valid_input(self):
        """test_not_valid_input - тестирование невалидного ввода

        :return:
        """
        for data in not_valid_test_data:
            response = requests.get(request_url_temp(data))
            with self.subTest(data=data, recieved_code=response.status_code):
                self.assertTrue(400 == response.status_code)

    def test_float_number_input(self):
        """test_float_number_input - тестирование ввода числа с точкой

        :return:
        """
        for data in float_number_test_data:
            response = requests.get(request_url_temp(data))
            with self.subTest(data=data, recieved_code=response.status_code):
                self.assertTrue(200 == response.status_code)









if __name__ == '__main__':
    unittest.main()
