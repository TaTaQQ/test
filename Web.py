from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.implicitly_wait(10)
    
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"q")))
    driver.find_element_by_xpath("//a[text()='活動專區']")
    driver.get_screenshot_as_file("screenshot1.png")

    driver.find_element(By.CLASS_NAME, "cubre-o-header__burger").click()
    driver.find_element(By.CLASS_NAME, "cubre-a-menuSortBtn -l1").click()
    cnt_list = len(driver.find_element(By.CLASS_NAME, "cubre-o-menuLinkList__content"))
    driver.get_screenshot_as_file("screenshot2.png")

    cnt_stop_card = driver.find_elements(By.CLASS_NAME, "cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets")
    print("停發卡數:" + str(len(cnt_stop_card)))
    driver.get_screenshot_as_file("screenshot3.png")
    
    driver.quit()