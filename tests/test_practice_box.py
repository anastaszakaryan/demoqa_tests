from selene import have, be, command
from selene.support.shared import browser
from demoqa_tests.utils import sources

def test_submit_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Practice Form'))

    browser.element('#firstName').type('Feofan')
    browser.element('#lastName').type('Grek')
    browser.element('#userEmail').type('feofangrek@gmail.com')
    browser.all('.custom-radio').element_by(have.exact_text('Male')).click() # я не знаю, что происходит в этой строке
    browser.element('#userNumber').type('8913225674')
    # browser.element('#dateOfBirthInput').click()
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__year-select [value="2007"]').click()
    browser.element('.react-datepicker__month-select [value="6"]').click()
    browser.element('.react-datepicker__day--007').click()

    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('Arts').press_tab()

    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    # browser.element('#uploadPicture').click()

    # загрузить картинку
    # browser.element('#uploadPicture').send_keys(upload_source('JJ.jpg'))
    browser.element('#uploadPicture').send_keys(sources('JJ.jpg')) # или в этой

    # browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element('#currentAddress').type('I live here! :\'(')
    browser.element('#state').element('input').type('Haryana').press_enter()
    browser.element('#city').element('input').type('Panipat').press_enter()

    # browser.element('#submit').click()




