from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--ignore-certificate-errors')
prefs = {"profile.managed_default_content_settings.images": 2, 
         "profile.default_content_setting_values.notifications": 2,
         "profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
#    "download.default_directory":r"D:\no_copyright_music",
    "download.prompt_for_download": False,
    "download.directory_upgrade":True,
    "safebrowsing.enabled":True   
})

driver_path = ChromeDriverManager().install()
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
driver = webdriver.Chrome(service=ChromeService(executable_path=correct_driver_path), options=chrome_options)