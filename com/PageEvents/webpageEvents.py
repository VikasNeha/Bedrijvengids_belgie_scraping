from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import *
import config
from Utilities.constants import IDMODE
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import Select


# noinspection PyBroadException
class WebpageEvents(object):
    def __init__(self):
        if config.RunInBrowser:
            ffProfile = FirefoxProfile()
            ffProfile.set_preference('permissions.default.image', 2)
            self.driver = webdriver.Firefox(ffProfile)
        else:
            service_args = ['--load-images=false', '--ignore-ssl-errors=true', '--proxy-type=none']
            phantomBinary = config.get_main_dir() + "\\Resources\\phantomjs.exe"
            dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
            self.driver = webdriver.PhantomJS(executable_path=phantomBinary, desired_capabilities=dcap,
                                              service_args=service_args)
        self.driver.implicitly_wait(10)

    def destroy(self):
        self.driver.quit()

    def navigate(self, url):
        self.driver.get(url)

    def findElement(self, idMode, idValue):
        try:
            webElement = None
            self.waitUntilElementIsPresent(idMode, idValue)
            if idMode == IDMODE.ID:
                webElement = self.driver.find_element_by_id(idValue)
            elif idMode == IDMODE.NAME:
                webElement = self.driver.find_element_by_name(idValue)
            elif idMode == IDMODE.CLASS:
                webElement = self.driver.find_element_by_class_name(idValue)
            elif idMode == IDMODE.PARTIAL_LINK_TEXT:
                webElement = self.driver.find_element_by_partial_link_text(idValue)
            elif idMode == IDMODE.LINK_TEXT:
                webElement = self.driver.find_element_by_link_text(idValue)
            return webElement
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            raise

    def waitUntilElementIsPresent(self, idMode, idValue):
        try:
            wait = ui.WebDriverWait(self.driver, config.webElementTimeOut)
            if idMode == IDMODE.ID:
                wait.until(lambda driver: self.driver.find_element_by_id(idValue))
            elif idMode == IDMODE.NAME:
                wait.until(lambda driver: self.driver.find_element_by_name(idValue))
            elif idMode == IDMODE.CLASS:
                wait.until(lambda driver: self.driver.find_element_by_class_name(idValue))
            elif idMode == IDMODE.PARTIAL_LINK_TEXT:
                wait.until(lambda driver: self.driver.find_element_by_partial_link_text(idValue))
            elif idMode == IDMODE.LINK_TEXT:
                wait.until(lambda driver: self.driver.find_element_by_link_text(idValue))
            elif idMode == IDMODE.XPATH:
                wait.until(lambda driver: self.driver.find_element_by_xpath(idValue))
        except:
            raise

    def getElementText(self, idMode, idValue):
        try:
            return self.findElement(idMode, idValue).text
        except:
            raise

    def clickPartialLink(self, idValue):
        try:
            self.findElement(IDMODE.PARTIAL_LINK_TEXT, idValue).click()
        except:
            raise

    def takeScreenshot(self, fileName):
        try:
            self.driver.get_screenshot_as_file(fileName)
        except:
            return

    def enterText(self, idMode, idValue, text):
        textbox = self.findElement(idMode, idValue)
        textbox.clear()
        textbox.send_keys(text)

    def clickButton(self, buttonText):
        allButtons = self.driver.find_elements_by_tag_name('button')
        buttonFound = False
        for currButton in allButtons:
            if currButton.text == buttonText:
                currButton.click()
                buttonFound = True
                break
        if not buttonFound:
            raise Exception('Problem in finding and clicking button: ' + buttonText)

    def assertLinkPresent(self, linkText):
        try:
            self.waitUntilElementIsPresent(IDMODE.PARTIAL_LINK_TEXT, linkText)
        except:
            raise

    def select_option_from_dropdown(self, parentIdMode, parentIdValue, optionText):
        try:
            select = Select(self.findElement(parentIdMode, parentIdValue))
            select.select_by_visible_text(optionText)
        except:
            raise