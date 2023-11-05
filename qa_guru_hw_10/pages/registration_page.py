import os

from selene import browser, have, be, command, by


class HighLevelRegistrationPage:

    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.all('.custom-control').element_by(have.exact_text(user.gender)).click()
        browser.element('#userNumber').should(be.blank).type(user.phone_number)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(user.month_of_birth)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(user.year_of_birth)).click()
        browser.element('.react-datepicker__month').element(by.text(user.day_of_birth)).click()

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-control-label').element_by(have.exact_text(user.hobby)).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/image.png'))
        browser.element('#currentAddress').should(be.blank).type(
            f'{user.address_street}, dom {user.address_house}, kv. {user.address_flat}')
        browser.element('#state').click().element(by.text(user.state)).click()
        browser.element('#city').click().element(by.text(user.city)).click()
        browser.element('#submit').click()

    def should_have_success_text(self):
        browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))

    def should_have_registered(self, user):
        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobby,
            user.photo,
            f'{user.address_street}, dom {user.address_house}, kv. {user.address_flat}',
            f'{user.state} {user.city}',
        ))
