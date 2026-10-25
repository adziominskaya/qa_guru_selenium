import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Первый шаг - выделение каждого теста в отдельную функцию и ее последующий вызов

testUserName = "Anastasia Diominskaya"
testUserEmail = "anastasia@test.com"
UserEmailWithNumbers = "anastasia123@test.com"
UserEmailWithPoint = "anastasia.test@test.com"
UserEmailWithCapital = "Anastasia@test.com"
html_payload = "<b>Anastasia</b>"


def test01():
    print("Проверяет email с цифрами")

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
        email_field.send_keys(UserEmailWithNumbers)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert testUserName in result_box.text and UserEmailWithNumbers in result_box.text
        print("Тест успешно пройден! Email с цифрами успешно принят!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test02():
    print("Проверяет email с точкой в имени пользователя")

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
        email_field.send_keys(UserEmailWithPoint)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert UserEmailWithPoint in result_box.text
        print("Тест успешно пройден! Email с точкой успешно принят")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test03():
    print("Проверяет email с заглявными буквами")

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
        email_field.send_keys(UserEmailWithCapital)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert UserEmailWithCapital in result_box.text
        print("Тест успешно пройден! Email с заглавной буквой успешно принят")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test04():
    print("Валидация поля Email - поле не принимает значения без @")

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
        email_field.send_keys("test.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Проверяем, что браузер считает email некорректным
        is_valid = driver.execute_script(
            "return arguments[0].validity.valid;",
            email_field
        )
        assert is_valid is False
        print("Тест успешно пройден! Поле Email не принимает значения без @")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test05():
    print("Валидация поля Email - Нет имени пользователя до @")

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
        email_field.send_keys("@test.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Проверяем, что браузер считает email некорректным
        is_valid = driver.execute_script(
            "return arguments[0].validity.valid;",
            email_field
        )
        assert is_valid is False
        print("Тест успешно пройден! Поле Email не принимает значения без имени пользователя до @")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test06():
    print("Валидация поля Email - Нет домена после @")

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
        email_field.send_keys("test@")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Проверяем, что браузер считает email некорректным
        is_valid = driver.execute_script(
            "return arguments[0].validity.valid;",
            email_field
        )
        assert is_valid is False
        print("Тест успешно пройден! Поле Email не принимает значения без домена после @")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test07():
    print("Валидация поля Email - Пробел внутри адреса")

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
        email_field.send_keys("test test@test.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Проверяем, что браузер считает email некорректным
        is_valid = driver.execute_script(
            "return arguments[0].validity.valid;",
            email_field
        )
        assert is_valid is False
        print("Тест успешно пройден! Поле Email не принимает значения с пробелом внутри адреса")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test08():
    print("Валидация поля Email - текст кириллица")

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
        email_field.send_keys("тест@test.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Проверяем, что браузер считает email некорректным
        is_valid = driver.execute_script(
            "return arguments[0].validity.valid;",
            email_field
        )
        assert is_valid is False
        print("Тест успешно пройден! Поле Email не принимает кириллицу")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test09():
    print("Валидация поля Name - текст кириллица")

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

        full_name_field.send_keys("Анастасия")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(testUserEmail)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Анастасия" in result_box.text
        print("Тест успешно пройден! Поле Name принимает значения кириллица")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test10():
    print("Провеяет HTML-инъекцию")

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

        full_name_field.send_keys(html_payload)

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(testUserEmail)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert html_payload in result_box.text
        print("Тест успешно пройден! HTML инъекция не работает!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

test01()
test02()
test03()
test04()
test05()
test06()
test07()
test08()
test09()
test10()