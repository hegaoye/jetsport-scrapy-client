from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import BROWSER_PATH


class Browser:
    """
    浏览器对象
    """

    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(executable_path=BROWSER_PATH, chrome_options=chrome_options)
        # self.browser.fullscreen_window()

    def get_brower(self):
        return self.browser
