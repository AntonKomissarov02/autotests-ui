from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.registration_course_title = page.get_by_test_id('authentication-ui-course-title-text')
        self.registration_user_already_exists_alert = page.get_by_test_id('registration-page-user-already-exists-alert')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()

    def check_visible_registration_user_already_exists_alert(self):
        expect(self.registration_user_already_exists_alert).to_be_visible()
        expect(self.registration_user_already_exists_alert).to_have_text('User already exists')

    def check_visible_registration_course_title(self):
        expect(self.registration_course_title).to_be_visible()
        expect(self.registration_course_title).to_have_text('UI Course')




