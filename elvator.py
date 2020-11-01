import selenium
from selenium.webdriver import Chrome

def getl():
    driver=Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.get("https://plantigrade-scope.000webhostapp.com/")
    link=driver.find_elements_by_class_name("alanBtn-root alan-a1f67070ae885c19049f4dc1c47d03712e956eca572e1d8b807a3e2338fdd0dc")
    link.click()
