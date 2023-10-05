import os

from selene import browser, be, have


def test_complete_todo():
    browser.open('/automation-practice-form') # Открываем страницу
    browser.element('[placeholder="First Name"]').type('Bob')
    browser.element('#lastName').type('Dylan')
    browser.element('#userEmail').type('test@mail.com')
    browser.element('[class="custom-control custom-radio custom-control-inline"]').click()
    browser.element('#userNumber').type('8800112299')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1990"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="0"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--026"]').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[class="custom-control custom-checkbox custom-control-inline"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/001.jpg'))
    browser.element('#currentAddress').type('hawaii')
    browser.element('#react-select-3-input').type('NCR').click().press_enter()
    browser.element('#react-select-4-input').type('Delhi').click().press_enter()
    browser.element('#submit').press_enter()

    browser.all('[class="table-responsive"]').should(have.texts(
        'Bob Dylan',
        'test@mail.com',
        'Male',
        '8800112299',
        '26 January,1990',
        'English',
        'Sports',
        '001.jpg',
        'hawaii',
        'NCR Delhi'
    ))





