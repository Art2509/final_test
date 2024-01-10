# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# a = driver.find_element_by_link_text('My Account')
# a.click()
# username = driver.find_element_by_css_selector("#username")
# username.send_keys("1@ya.ru")
# password = driver.find_element_by_css_selector("#password")
# password.send_keys("Hit777711119999hit")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# b = driver.find_element_by_link_text('Shop')
# b.click()
# book = driver.find_element_by_css_selector(".post-181 :nth-child(2)")
# book.click()
# title = driver.find_element_by_css_selector(".product_title.entry-title")
# title_get_text = title.text
# assert title_get_text == "HTML5 Forms"
# if title.text == title_get_text:
#     print("Название книги:", title.text)
# driver.quit()
import time

# ***************************************

# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# a = driver.find_element_by_link_text('My Account')
# a.click()
# username = driver.find_element_by_css_selector("#username")
# username.send_keys("1@ya.ru")
# password = driver.find_element_by_css_selector("#password")
# password.send_keys("Hit777711119999hit")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# b = driver.find_element_by_link_text('Shop')
# b.click()
# html = driver.find_element_by_css_selector(".cat-item.cat-item-19 :nth-child(1)")
# html.click()
# items_count = driver.find_elements_by_css_selector("a > h3")
# if len(items_count) == 3:
#     print("В категории 3 товара")
# else:
#     print("Ошибка. Количество товаров в категории: " + str(len(items_count)))
# driver.quit()

# ***********************************************

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# a = driver.find_element_by_link_text('My Account')
# a.click()
# username = driver.find_element_by_css_selector("#username")
# username.send_keys("1@ya.ru")
# password = driver.find_element_by_css_selector("#password")
# password.send_keys("Hit777711119999hit")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# b = driver.find_element_by_link_text('Shop')
# b.click()
# sorting_check = EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, ".orderby"), "Default sorting")
# sorting_check_get_text = sorting_check.text
# if sorting_check.text == sorting_check_get_text:
#     print("Сортировка:", sorting_check.text)
# time.sleep(3)
# sorting_check = driver.find_element_by_css_selector(".orderby")
# select = Select(sorting_check)
# select.select_by_value("price-desc")
# sorting_check2 = EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, ".orderby"),
#                                                        "Sort by price: high to low")
# sorting_check2_get_text = sorting_check2.text
# if sorting_check2.text == sorting_check2_get_text:
#     print("Сортировка:", sorting_check2.text)
# driver.quit()

# *********************************************

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# a = driver.find_element_by_link_text('My Account')
# a.click()
# username = driver.find_element_by_css_selector("#username")
# username.send_keys("1@ya.ru")
# password = driver.find_element_by_css_selector("#password")
# password.send_keys("Hit777711119999hit")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# b = driver.find_element_by_link_text('Shop')
# b.click()
# book = driver.find_element_by_css_selector(".post-169 :nth-child(3)")
# book.click()
# old = driver.find_element_by_css_selector(".price > del > span")
# old_get_text = old.text
# assert old_get_text == "₹600.00"
# if old.text == old_get_text:
#     print("Старая цена:", old.text)
# new = driver.find_element_by_css_selector(".price > ins > span")
# new_get_text = new.text
# assert new_get_text == "₹450.00"
# if new.text == new_get_text:
#     print("Новая цена:", new.text)
# book2 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
# book2.click()
# close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close.click()
# driver.quit()

# *************************************************

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# b = driver.find_element_by_link_text('Shop')
# b.click()
# driver.execute_script("window.scrollBy(0, 500);")
# book = driver.find_element_by_css_selector('.post-182 .add_to_cart_button')
# book.click()
# time.sleep(5)
# cartcontent = driver.find_element_by_css_selector(".cartcontents")
# cartcontent_get_text = cartcontent.text
# assert cartcontent_get_text == "1 Item"
# if cartcontent.text == cartcontent_get_text:
#     print("Количество товаров:", cartcontent.text)
# price = driver.find_element_by_css_selector(".wpmenucartli .amount")
# price_get_text = price.text
# assert price_get_text == "₹180.00"
# if price.text == price_get_text:
#     print("Стоимость товаров:", price.text)
# cart = driver.find_element_by_id('wpmenucartli')
# cart.click()
# subtotal = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"),
#                                             "₹180.00"))
# total = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"),
#                                             "₹183.60"))
# driver.quit()

# ************************************************************


# from selenium import webdriver
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# b = driver.find_element_by_link_text('Shop')
# b.click()
# driver.execute_script("window.scrollBy(0, 500);")
# book1 = driver.find_element_by_css_selector('.post-182 .add_to_cart_button')
# book1.click()
# time.sleep(2)
# book2 = driver.find_element_by_css_selector('.post-180 .add_to_cart_button')
# book2.click()
# cart = driver.find_element_by_id('wpmenucartli')
# cart.click()
# time.sleep(2)
# remove_book1 = driver.find_element_by_class_name("remove")
# remove_book1.click()
# undo = driver.find_element_by_css_selector('.woocommerce-message > a')
# undo.click()
# quantity = driver.find_element_by_css_selector(".input-text.qty.text")
# quantity.clear()
# quantity2 = driver.find_element_by_css_selector(".input-text.qty.text")
# quantity2.send_keys("3")
# update_btn = driver.find_element_by_name("update_cart")
# update_btn.click()
# quantity_check = driver.find_element_by_css_selector(".input-text.qty.text")
# quantity_check_value = quantity_check.get_attribute("value")
# assert quantity_check_value == "3"
# time.sleep(5)
# apply_btn = driver.find_element_by_css_selector(".coupon :nth-child(3)")
# apply_btn.click()
# message = driver.find_element_by_css_selector(".woocommerce-error > li")
# message_get_text = message.text
# assert message_get_text == "Please enter a coupon code."
# if message.text == message_get_text:
#      print("Активно следующее сообщение:", message.text)
# driver.quit()

# *******************************************************

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
b = driver.find_element_by_link_text('Shop')
b.click()
driver.execute_script("window.scrollBy(0, 500);")
book = driver.find_element_by_css_selector('.post-182 .add_to_cart_button')
book.click()
time.sleep(2)
cart = driver.find_element_by_id('wpmenucartli')
cart.click()
proceed_btn = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
proceed_btn.click()
time.sleep(3)
first_name = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
first_name.send_keys("Artem")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Sv")
email = driver.find_element_by_id("billing_email")
email.send_keys("1@ya.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("222332232")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country2 = driver.find_element_by_id("s2id_autogen1_search")
country2.send_keys("Russia")
country3 = driver.find_element_by_css_selector(".select2-match")
country3.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Broadwey")
city = driver.find_element_by_id("billing_city")
city.send_keys("Tex")
state = driver.find_element_by_id("billing_state")
state.send_keys("Lux")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("23232323222")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
pay = driver.find_element_by_css_selector("#payment_method_cheque")
pay.click()
order_btn = driver.find_element_by_id("place_order")
order_btn.click()
order_received = WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
                                             "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"),
                                             "Check Payments"))
driver.quit()