import pytest
from pytest_bdd import given, then, scenario, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from re import sub
from decimal import Decimal

@scenario('allegro.feature', 'Find highest price of Iphone 11 black')
def test_allegro():
    pass


@given("User open the allegro site", target_fixture="allegro_site")
def allegro_site_s():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("http://www.allegro.pl")
    return firefox_driver

@when("User type Iphone 11 in search box and click search")
def search_result(allegro_site):
    allegro_site.find_element_by_xpath("//button[@class='_13q9y _8hkto munh_56_m m7er_k4 m7er_56_m']").click()
    search_box = allegro_site.find_element_by_name("string")
    search_box.send_keys("iphone 11")
    search_box.send_keys(Keys.RETURN)


@when('User choose black color from the color list')
def pickup_color(allegro_site):
    element = WebDriverWait(allegro_site, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[10]/div[1]/ul[1]/li[1]/label[1]")))
    element.click()

@then('User can see number of results, highest price with and without tax')
def black_iphones_page(allegro_site):
    results = WebDriverWait(allegro_site, 10).until(EC.presence_of_element_located((By.XPATH, "//section[contains(@class, '_9c44d_3pyzl')]")))
    number_of_offers = len(results.find_elements_by_tag_name('article'))
    logger.info(f'We have {number_of_offers} offers of black iphones')
    prices_list = [x.text for x in results.find_elements_by_xpath("//div[contains(@class, 'msa3_z4 _9c44d_2K6FN')]")]
    list_of_prices = [Decimal(sub(r'[^\d.]', '', x)) for x in prices_list]
    highest_price = max(list_of_prices)
    highest_price_index = list_of_prices.index(highest_price)
    highest_price_with_tax = float(highest_price) * 1.23 / 100
    logger.info(f'The highest prices is {prices_list[highest_price_index]} including tax {highest_price_with_tax} zł')
    allegro_site.quit()
