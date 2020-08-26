from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome("/Python34/chromedriver.exe")
    yield browser
    # browser.find_element_by_tag_name('textarea').send_keys()
    browser.quit()


class TestMainPage():
    @pytest.mark.parametrize('webpage', ["https://stepik.org/lesson/236895/step/1",
                                         "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
                                         "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
                                         "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1",
                                         "https://stepik.org/lesson/236905/step/1"])
    def test_send_answer(self, browser, webpage):
        link = "https://stepik.org/lesson/{webpage}/step/1"
        browser.get(webpage)
        answer_number = math.log(int(time.time()))
        time.sleep(3)
        # input_answer = browser.find_element_by_xpath('//textarea')
        input_answer = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//textarea")))
        input_answer.send_keys(str(answer_number))

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class = 'submit-submission']")))
        button.click()
        time.sleep(5)
        check_msg = browser.find_element_by_xpath("//pre[@class = 'smart-hints__hint']").text

        assert check_msg == 'Correct!', 'Your answer is not correct'




