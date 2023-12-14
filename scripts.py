from library.basic_selenium_actions import *
from constants.xpaths.saucedemo_login import *
from constants.xpaths.saucedemo_inventory import *
from constants.xpaths.items_description import *
from constants.xpaths.saucedemo_checkout import*
import time

web_url = "https://www.saucedemo.com/"
driver = open_browser_to_link(web_url)
time.sleep(3)
enter_text_in_element(driver, txt_box_username, "standard_user")
enter_text_in_element(driver, txt_box_password, "secret_sauce")
click_element(driver, btn_login)
time.sleep(1)
select_value_in_dropdown(driver, dropdown_sort, "lohi")
time.sleep(1)
item1 = get_element_text(driver, bike_light)
print("I am going to buy: ", item1)
click_element(driver, bike_light)
time.sleep(1)
click_element(driver, btn_add_to_cart)
time.sleep(1)
click_element(driver, btn_back_to_products)
time.sleep(1)
select_value_in_dropdown(driver, dropdown_sort, "lohi")
scroll_to_element(driver, fleece_jacket)
time.sleep(1)
item2 = get_element_text(driver, fleece_jacket)
print("I am going to buy: ", item2)
time.sleep(1)
click_element(driver, fleece_jacket)
time.sleep(1)
click_element(driver, btn_add_to_cart)
time.sleep(1)
click_element(driver, btn_back_to_products)
time.sleep(2)
click_element(driver, btn_go_to_cart)
time.sleep(1)
click_element(driver, btn_proceed_to_checkout)
time.sleep(1)
enter_text_in_element(driver, txt_box_firstname, "Shubham")
time.sleep(1)
enter_text_in_element(driver, txt_box_lastname, "Lohra")
time.sleep(1)
enter_text_in_element(driver, txt_box_zipcode, "560103")
time.sleep(1)
click_element(driver, btn_continue_to_payment)
time.sleep(1)
click_element(driver, btn_finish_payment)
time.sleep(1)
checkoutMessage = get_element_text(driver,txt_checkout_message)
success_message = 'Your order has been dispatched'
if success_message in checkoutMessage:
    print("Is payment successfull and Successfully checked out : "+ "Yes")
    print("checkout message : ", checkoutMessage)

else:
    print("Some error happened during payment and checkout Process!")
click_element(driver, btn_back_to_home)
