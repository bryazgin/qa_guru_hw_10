import os

from selene import have, be, command, by, browser

import tests


class RegistrationPage():

    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def type_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').should(be.blank).type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def select_male_gender(self):
        browser.all('.custom-control').element_by(have.exact_text('Male')).click()

    def type_phone_number(self, phone_number):
        browser.element('#userNumber').should(be.blank).type(phone_number)

    def select_Sergey_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('July')).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1995')).click()
        browser.element('.react-datepicker__day--010').click()

    def scroll_to_submit_button(self):
        browser.element('#submit').perform(command.js.scroll_into_view)

    def type_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_sport_hobbie(self):
        browser.all('.custom-control-label').element_by(have.exact_text("Sports")).click()

    def upload_picture(self, path):
        # исправил
        # browser.element('#uploadPicture').send_keys(os.path.abspath(path))
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), path)))

    def type_adress(self, street, house, flat):
        browser.element('#currentAddress').should(be.blank).type(f'{street}, dom {house}, kv. {flat}')

    def select_haryana_state(self):
        browser.element('#state').click().element(by.text('Haryana')).click()

    def select_karnal_city(self):
        browser.element('#city').click().element(by.text('Karnal')).click()

    def submit(self):
        browser.element('#submit').click()

    def modal_header(self):
        return browser.element('.modal-header')

    def modal_table(self):
        return browser.element('.table-responsive').all('td:nth-of-type(2)')
