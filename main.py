import remove_comments
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

id = '' #에브리타임 아이디 입력
password = '' #에브리타임 비밀번호 입력

driver = webdriver.Chrome()

def run(id, password, driver):
    try:
        remove_comments.login(id, password, driver)
        remove_comments.remove_comments(driver)
    except UnexpectedAlertPresentException:
        print('로그인 오류발생. 오류가 지속된다면 아이디와 비밀번호가 맞는지 확인해보세요')
        run(id, password, driver)
    except Exception as e:
        print(e)

run(id, password, driver)
