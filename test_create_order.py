# Сергей Цой, 4-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Функция изменения и запроса трек-номера заказа
def get_number_track(body):
    order_response = sender_stand_request.post_order(body)
    t_number = data.t_number
    t_number["t"] = order_response.json()["track"]
    return t_number


# Функция для позитивной проверки
def positive_assert(params_order):
    response = sender_stand_request.get_order_by_number(params_order)
    assert response.status_code == 200
    print(response.status_code)


# Тест 1: "Получение заказа по трек-номеру заказа"
def test_create_order_with_t_number():
    param_order = get_number_track(data.order_body)
    positive_assert(param_order)
