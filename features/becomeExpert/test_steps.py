from pytest import fixture
from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, sync_playwright, Browser


@fixture
def page(browser: Browser):
    return browser.new_context(ignore_https_errors=True).new_page()


@scenario('become_expert.feature', 'An expert joins the eond')
def test_expert_join():
    pass


@given('Exp opens eond website')
def goto_page(page: Page):
    page.goto("http://localhost:3000/becomeexpert")


@when('Exp fills username and password')
def fill_login_password(page: Page):
    page.locator("[placeholder=\"Enter your e-mail address\"]").click()
    page.locator("[placeholder=\"Enter your e-mail address\"]").fill("test---test@test.com")
    page.locator("[placeholder=\"Enter your e-mail address\"]").press("Tab")
    page.locator("[placeholder=\"Must be at least 8 characters\"]").fill("qwer1234qwer4r3e2w1q")
    page.locator("input[name=\"personal_data_consent\"]").check()
    page.locator("input[name=\"tc_and_privacy_consent\"]").check()
    page.locator("button:has-text(\"Create an account\")").click()


@when('Exp chooses engagement type')
def engagement_type(page: Page):
    page.locator("text=Expert Advisory").click()
    page.locator("text=Next").click()


@when('Exp uploads cv and fills skills')
def cv_skills(page: Page):
    page.locator("text=Skip this step").click()
    page.locator("text=​Describe your area of expertise (e.g. project management, cybersecurity inciden >> [aria-label=\"Open\"]").click()
    page.locator("[placeholder=\"Type or drag and drop\"]").click()
    page.locator("[placeholder=\"Type or drag and drop\"]").fill("test0")
    page.locator("input[type=\"checkbox\"]").first.check()
    page.locator("[placeholder=\"Type or drag and drop\"]").fill("test1")
    page.locator("input[type=\"checkbox\"]").check()
    page.locator("[placeholder=\"Type or drag and drop\"]").fill("test2")
    page.locator("input[type=\"checkbox\"]").check()
    page.locator("[placeholder=\"Type or drag and drop\"]").fill("test3")
    page.locator("input[type=\"checkbox\"]").check()
    page.locator("[placeholder=\"Type or drag and drop\"]").fill("test4")
    page.locator("input[type=\"checkbox\"]").check()
    page.locator("[aria-label=\"Open\"]").click()
    page.locator("text=Cybersecurity and Information Security >> input[type=\"checkbox\"]").check()
    page.locator("text=Next").click()


@when('Exp fills experience')
def jobs_projects(page: Page):
    page.locator("text=Next").click()


@when('Exp chooses engagemend models')
def engagemend_models(page: Page):
    page.locator("div[role=\"button\"]:has-text(\"Few months projects\")").click()
    page.locator("div[role=\"button\"]:has-text(\"On-site\")").click()
    page.locator("input[name=\"relocate\"]").nth(1).check()
    page.locator("text=What is your hourly rate in US dollars?​ >> [placeholder=\"Type in number\"]").click()
    page.locator("text=What is your hourly rate in US dollars?​ >> [placeholder=\"Type in number\"]").fill("33")
    page.locator("text=What is your daily rate in US dollars?​ >> [placeholder=\"Type in number\"]").click()
    page.locator("text=What is your daily rate in US dollars?​ >> [placeholder=\"Type in number\"]").fill("33")
    page.locator("text=Next").click()


@when('Exp fills personal data')
def fill_name_surname(page):
    page.locator("[placeholder=\"Name\"]").click()
    page.locator("[placeholder=\"Name\"]").fill("testowich")
    page.locator("[placeholder=\"Surname\"]").click()
    page.locator("[placeholder=\"Surname\"]").fill("testonowski")
    page.locator("text=Location *​ >> [aria-label=\"Open\"]").click()
    page.locator("text=American Samoa").click()
    page.locator("#root div:has-text(\"Final detailsShare your contact info Name *​Surname *​E-mail *​Location *​Citize\")").nth(3).click()
    page.locator("text=Phone number *​​ >> [aria-label=\"Open\"]").click()
    page.locator("text=Antigua and Barbuda (AG) +1-268").click()
    page.locator("[placeholder=\"Enter your phone number\"]").click()
    page.locator("[placeholder=\"Enter your phone number\"]").fill("12345678")
    page.locator("[aria-label=\"Open\"]").nth(3).click()
    page.locator("text=Ashante").click()
    page.locator("[aria-label=\"Open\"]").nth(4).click()
    page.locator("text=Independent").click()
    page.locator("text=Citizenship and Legal residence (multiple choice) *​ >> [aria-label=\"Open\"]").click()
    page.locator("text=American Samoa >> input[type=\"checkbox\"]").check()
    page.locator("text=Finish").click()


@then('Exp sees the page profile created')
def final_page(page):
    page.locator("text=Congratulations on joining the EonD platform!").click()
    page.locator("text=You can now visit your profile here:").click()
    page.locator("text=For latest news and updates follow us on Social Media").click()
