from selene import have, be, command
from selene.support.shared import browser

def test_submit_form():
    # GIVEN ...
    # WHEN
    browser.open('/text-box')
    # THEN
    browser.should(have.title('ToolsQA'))
    browser.should(have.title_containing('QA'))
    browser.element('[class~=main-header]').should(have.exact_text('Text Box'))
    browser.element('.main-header').should(have.text('Box'))

    # WHEN
    browser.element('#userName').type('Feofan')
    browser.element('#userEmail').type('sobaka@mail.ru')
    browser.element('#currentAddress').type('Moscow')
    browser.element('#permanentAddress').type('Earth')
    # browser.element('#submit').scroll_to().click()
    browser.element('#submit').perform(command.js.scroll_into_view).click()
    # THEN
    # TODO: IMPLEMENT ASSERTION
