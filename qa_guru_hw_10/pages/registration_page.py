import os

from selene import browser, have, be, command, by


class RegistrationPage:

    def open_page(self, url):
        browser.open(url)

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
        browser.all('.custom-control-label').element_by(have.exact_text('Sports')).click()

    def upload_picture(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))

    def type_adress(self, street, house, flat):
        browser.element('#currentAddress').should(be.blank).type(f'{street}, dom {house}, kv. {flat}')

    def select_haryana_state(self):
        browser.element('#state').click().element(by.text('Haryana')).click()

    def select_karnal_city(self):
        browser.element('#city').click().element(by.text('Karnal')).click()

    def submit(self):
        browser.element('#submit').click()


class HighLevelRegistrationPage:

    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.all('.custom-control').element_by(have.exact_text('Male')).click()
        browser.element('#userNumber').should(be.blank).type(user.phone_number)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('July')).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1995')).click()
        browser.element('.react-datepicker__day--010').click()

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-control-label').element_by(have.exact_text('Sports')).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(user.path))
        browser.element('#currentAddress').should(be.blank).type(f'{street}, dom {house}, kv. {flat}')
        browser.element('#state').click().element(by.text('Haryana')).click()
        browser.element('#city').click().element(by.text('Karnal')).click()
        browser.element('#submit').click()

    def should_have_registered(self, user):
        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.date_of_birth,
            user.subject,
            user.hobby,
            user.photo,
            user.current_address,
            f'{user.state} {user.city}',
        ))
