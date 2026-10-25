import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

testUserName = "Anastasia Diominskaya"
testUserEmail = "anastasia@test.com"
currentUserAddress = "Batumi, Georgia"
permanentUserAddress = "Minsk, Belarus"


def test01():
    print("Тест  Current Address")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys(testUserName)

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(testUserEmail)

        # Находим поле Current Address по его ID и вводим текст
        email_field = driver.find_element(By.ID, "currentAddress")
        email_field.send_keys(currentUserAddress)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert currentUserAddress in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test02():
    print("Тест  Permanent Address")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys(testUserName)

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(testUserEmail)

        # Находим поле Permanent Address по его ID и вводим текст
        email_field = driver.find_element(By.ID, "permanentAddress")
        email_field.send_keys(permanentUserAddress)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert permanentUserAddress in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


test01()
test02()