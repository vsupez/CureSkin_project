from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger, MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from app.application import Application


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # s = Service('C:\\Users\\vsupe\QA\\Automation\\python-selenium-automation\\chromedriver')
    # context.driver = webdriver.Chrome(service=s)

# Using Firefox with headless browser mode
    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    s = Service('C:\\Users\\vsupe\\QA\\Automation\\python-selenium-automation\\geckodriver')
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Firefox(options=options, service=s)


    # Using Chrome with Headless Browser mode
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(chrome_options=options, service=s)

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=s),
    #     MyListener()
    # )

    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())

    # -------------------------------------------------------------------------------------------------------
    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # -------------------------------------------------------------------------------------------------------
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f"Started scenario:  {scenario.name}")
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f"Started step: {step}")


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
