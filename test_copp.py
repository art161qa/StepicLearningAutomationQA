from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time

class TestAuth:
    def test_authorization(self, browser):
        browser.implicitly_wait(5)
        browser.get("https://test.copp23.ru/")
        login = "t0r1n88@mail.ru"
        password = "}6VhVfw3iC"
        login_field = browser.find_element_by_name("USER_LOGIN")
        login_field.click()
        login_field.send_keys(login)
        password_field = browser.find_element_by_name("USER_PASSWORD")
        password_field.click()
        password_field.send_keys(password)
        button_auth = browser.find_element_by_xpath("//img[@alt = 'Вход']").click()
        time.sleep(3)

    def test_add_adress(self, browser):

        open_adresses = browser.get("https://test.copp23.ru/opp_region_mngmnt/?page=matr/my-addresses-add")
        region_filter = browser.find_element_by_xpath("(//div[@class = 'click_reports_header'])[1]")
        region_filter.click()
        list_of_region = browser.find_element_by_xpath("(//div[@class='scroll-item'])[1]")
        list_of_region.click()
        select_region = browser.find_element_by_xpath("//div[contains(@class, 'scroll-item') and text() = 'Краснодарский край']")
        municip_education = browser.find_element_by_xpath("(//div[@class = 'click_reports_header'])[2]")
        municip_education.click()
        select_municip_education = browser.find_element_by_xpath("//div[contains(@class, 'scroll-item') and text() = 'город-курорт Анапа']")
        select_municip_education.click()
        list_of_organization = browser.find_element_by_xpath("(//div[@class = 'click_reports_header'])[3]")
        list_of_organization.click()
        select_organization = browser.find_element_by_xpath("//div[contains(@class, 'scroll-item') and text() = 'Академ-медиа']")
        select_organization.click()
        input_country = browser.find_element_by_name("COUNTRY")
        input_country.click()
        input_country.send_keys('Test country')
        index_field = browser.find_element_by_name("INDEX")
        index_field.click()
        index_field.send_keys("Test index")
        input_street = browser.find_element_by_name("STREET")
        input_street.click()
        input_street.send_keys('Test street')
        input_town = browser.find_element_by_name("LOCALITY")
        input_town.click()
        input_town.send_keys('Test town')
        input_house = browser.find_element_by_name("HOUSE")
        input_house.click()
        input_house.send_keys('Test town')
        input_name = browser.find_element_by_name("NAME")
        input_name.click()
        input_name.send_keys('Test subvision')
        input_subdivision = browser.find_element_by_name("SUBDIVISION")
        input_subdivision.click()
        input_subdivision.send_keys('Test subvision')
        button_save = browser.find_element_by_xpath("//button[(contains(text(),'Сохранить'))]").click()
        time.sleep(10)









