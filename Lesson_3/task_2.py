"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


# Так и не понял каким именно способом нужно сделать задание!!

def user_data_output1(**kwargs):
    print(*kwargs.values())


def user_data_output(**kwargs):
    return " ".join(kwargs.values())


my_data = {
    "name": "Daniil",
    "surname": "Kapileti",
    "year": "9984",
    "citi": "LifeCity",
    "email": "Chebyrec_ryt@mail.ru",
}

user_data_output1(**my_data)
print(user_data_output(**my_data))
