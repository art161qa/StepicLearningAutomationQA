from selenium import webdriver
import unittest
import time

browser = webdriver.Chrome()
browser.maximize_window()

class TestRegistration(unittest.TestCase):
    def test_first_page(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser.get(link)
        field_firstName = browser.find_element_by_xpath("//div[@class = 'first_block']//div[@class = 'form-group first_class']//input[@class = 'form-control first']")
        field_firstName.send_keys('Test')
        field_lastName = browser.find_element_by_xpath("//div[@class = 'first_block']//div[@class = 'form-group second_class']//input[@class = 'form-control second']")
        field_lastName.send_keys('Test')
        field_email = browser.find_element_by_xpath("//div[@class = 'first_block']//div[@class = 'form-group third_class']//input[@class = 'form-control third']")
        field_email.send_keys('Test')
        time.sleep(3)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_second_page(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser.get(link)
        field_firstName = browser.find_element_by_xpath(
            "//div[@class = 'first_block']//div[@class = 'form-group first_class']//input[@class = 'form-control first']")
        field_firstName.send_keys('Test')
        field_lastName = browser.find_element_by_xpath(
            "//div[@class = 'first_block']//div[@class = 'form-group second_class']//input[@class = 'form-control second']")
        field_lastName.send_keys('Test')
        field_email = browser.find_element_by_xpath(
            "//div[@class = 'first_block']//div[@class = 'form-group third_class']//input[@class = 'form-control third']")
        field_email.send_keys('Test')
        time.sleep(3)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()