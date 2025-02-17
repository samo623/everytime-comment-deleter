import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

id = '' #에브리타임 아이디 입력
password = '' #에브리타임 비밀번호 입력력

running = True
options = Options()

options.add_experimental_option('detach', True)
#로그인 파트
#TODO 로그인시 간헐적으로 발생하는 오류 고치기
driver = webdriver.Chrome(options=options)
driver.get('https://everytime.kr/mycommentarticle')
username_field = driver.find_element(By.NAME, 'id')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/input')

username_field.send_keys(id)
password_field.send_keys(password)

time.sleep(1)

login_button.click()
#댓글 제거 파트
while True:
    WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'article'))
    )
    comment_list = driver.find_elements(By.CLASS_NAME, 'article')

    if not comment_list:
        break
    comment_block = comment_list[0]
    comment_block.click()
    try:
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

    except Exception as e:
        print("오류 발생 :", e)
print('삭제가 완료되었습니다.')