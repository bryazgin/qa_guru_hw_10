from qa_guru_hw_10.pages.registration_page import HighLevelRegistrationPage

from qa_guru_hw_10.user.user import User


def test_complete_form():
    registration_page = HighLevelRegistrationPage()
    Sergey = User(first_name='Sergey',
                  last_name='Bryazgin',
                  email='test_selene@gmail.com',
                  phone_number='8999556677',
                  gender='Male',
                  year_of_birth='1995',
                  month_of_birth='July',
                  day_of_birth='10',
                  subject='Computer Science',
                  hobby='Sports',
                  photo='image.png',
                  address_street='Lenina',
                  address_house='28',
                  address_flat='128',
                  state='Haryana',
                  city='Karnal'
                  )

    registration_page.open_page()

    # WHEN
    registration_page.register(Sergey)

    # THEN
    registration_page.should_have_success_text()
    registration_page.should_have_registered(Sergey)
