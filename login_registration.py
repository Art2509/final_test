# import time
# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# a = driver.find_element_by_link_text('My Account')
# a.click()
# mail = driver.find_element_by_css_selector("#reg_email")
# mail.send_keys("tema-inc@yandex.ru")
# password = driver.find_element_by_css_selector("#reg_password")
# password.send_keys("Hit777711119999hit")
# time.sleep(3)
# reg = driver.find_element_by_name("register")
# reg.click()

# *********************************

from selenium import webdriver
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
a = driver.find_element_by_link_text('My Account')
a.click()
username = driver.find_element_by_css_selector("#username")
username.send_keys("1@ya.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("Hit777711119999hit")
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link:nth-child(6)")
logout_get_text = logout.text
assert logout_get_text == "Logout"
if logout.text == logout_get_text:
    print("Элемент присутствует:", logout.text)
else:
    print("Элемент отсутствует:", logout.text)

