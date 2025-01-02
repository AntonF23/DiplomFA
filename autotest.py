# Федоренко Антон, 25-ая когорта, Дипломный проект. Инженер по тестированию плюс
from sendor_stand_request import create_order, get_order
import data

#Автотест
def test_order_creation_and_number():
    response = create_order(data.order_body)

    track_number = response.json()["track"]

# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, "Ошибка: {order_response.status_code}"
    order_data = order_response.json()

