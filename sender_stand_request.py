import configuration
import requests


# Функция создания заказа
def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATE,
                         json=body)


# Функция получения заказа по трек-номеру
def get_order_by_number(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_GET,
                        params=parameters)
