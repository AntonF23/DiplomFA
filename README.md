#DiplomFA

#Работа с базой данных Яндекс Самокат:

1. SQL-запрос в консоли проверяет, отображается ли созданный заказ в базе данных.
Для этого выведен список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

2. SQL-запрос для тестирования статусов заказов. 
Нужно убедиться, что в базе данных они записываются корректно.
Для этого выведены все трекеры заказов и их статусы. 

#Автоматизация тестирования Яндекс Самокат:
Автоматизация сценария: проверяется, что по треку заказа можно получить данные о созданном заказе.

#Требования для проведения автоматизированного тестирования: 
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск теста выполняется командой pytest autotest.py
