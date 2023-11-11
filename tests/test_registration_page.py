from selene import have

from qa_guru_hw_10.pages.registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()

    registration_page.open_page()

    # WHEN
    registration_page.type_first_name('Sergey')
    registration_page.type_last_name('Bryazgin')
    registration_page.type_email('test_selene@gmail.com')
    registration_page.select_male_gender()
    registration_page.type_phone_number('8999112233')
    registration_page.select_Sergey_birthday()
    registration_page.scroll_to_submit_button()
    registration_page.type_subject('Computer Science')
    registration_page.select_sport_hobbie()
    registration_page.upload_picture('resources/image.jpg')
    registration_page.type_adress('Lenina', 28, 128)
    registration_page.select_haryana_state()
    registration_page.select_karnal_city()
    registration_page.submit()

    # THEN
    registration_page.modal_header().should(have.exact_text('Thanks for submitting the form'))
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
