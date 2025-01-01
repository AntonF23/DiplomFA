# Федоренко Антон, 25-ая когорта, Дипломный проект. Инженер по тестированию плюс
import configuration
import requests
import data

#Создаем заказ
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)

#Получаем номер трекера созданного заказа
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

#Автотест
def test_order_creation_and_number():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Номер трека Вашего заказа:", track_number)

# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, "Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)
