import allure
from selene import have

from qa_guru_hw_10.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()

    with allure.step("Открываем форму"):
        registration_page.open_page()

    # WHEN
    with allure.step("Заполняем имя"):
        registration_page.type_first_name('Sergey')
    with allure.step("Заполняем фамилию"):
        registration_page.type_last_name('Bryazgin')
    with allure.step("Заполняем email"):
        registration_page.type_email('test_selene@gmail.com')
    with allure.step("Заполняем пол"):
        registration_page.select_male_gender()
    with allure.step("Заполняем телефон"):
        registration_page.type_phone_number('8999112233')
    with allure.step("Заполняем день рождения"):
        registration_page.select_Sergey_birthday()
    registration_page.scroll_to_submit_button()
    with allure.step("Заполняем предмет"):
        registration_page.type_subject('Computer Science')
    with allure.step("Заполняем хобби"):
        registration_page.select_sport_hobbie()
    with allure.step("Загружаем картинку"):
        registration_page.upload_picture('resources/image.jpg')
    with allure.step("Заполняем адрес"):
        registration_page.type_adress('Lenina', 28, 128)
        registration_page.scroll_to_submit_button()
    with allure.step("Выбираем штат"):
        registration_page.select_haryana_state()
    with allure.step("Выбираем город"):
        registration_page.select_karnal_city()
    with allure.step("Нажимаем сабмит"):
        registration_page.submit()

    # THEN
    with allure.step("Проверяем заголовок таблицы"):
        registration_page.modal_header().should(have.exact_text('Thanks for submitting the form'))
    with allure.step("Проверяем заполненные данные"):
        registration_page.modal_table().should(have.texts(
            'Sergey Bryazgin',
            'test_selene@gmail.com',
            'Male',
            '8999112233',
            '10 July,1995',
            'Computer Science',
            'Sports',
            'image.jpg',
            'Lenina, dom 28, kv. 128',
            'Haryana Karnal'
        ))
