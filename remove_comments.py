from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login(id: str, password: str, driver):
    driver.get('https://everytime.kr/mycommentarticle')
    username_field = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.NAME, 'id'))
    )
    password_field = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.NAME, 'password'))
     )
    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form/input'))
        ) 
    username_field.send_keys(id)
    password_field.send_keys(password)
    login_button.click()

def remove_comments(driver):
    while True:
        WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'article'))
        )
        comment_list = driver.find_elements(By.CLASS_NAME, 'article')

        if not comment_list:
            break
        comment_block = comment_list[0]
        comment_block.click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, "//article[@class='parent' or @class='child']//li[@class='del']"))
        )            
        delete_buttons = driver.find_elements(By.XPATH, "//article[@class='parent' or @class='child']//li[@class='del']")
        for delete_button in delete_buttons:
            delete_button.click()
            alert = driver.switch_to.alert
            alert.accept()
        driver.back()
        driver.refresh()
    print('삭제가 완료되었습니다.')