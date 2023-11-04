from selene import have
from qa_guru_hw_10.pages.registration_page import HighLevelRegistrationPage


def test_complete_form():
    registration_page = HighLevelRegistrationPage
    Sergey = User()

    registration_page.open_page()

    registration_page.register()

    registration_page.should_have_registered(Sergey)
