import remove_comments
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from version import __version__

print('제작자 : samo623')
print('Github : https://github.com/samo623/everytime-comment-deleter')
print('본 프로그램은 GNU General Public License v3.0을 적용받고 있습니다.')
print('Version : ',__version__)

id = input('에브리타임 아이디를 입력해주세요 : ')
password = input('에브리타임 비밀번호를 입력해주세요 : ')
id = str(id)
password = str(password)

driver = webdriver.Chrome()

def run(id, password, driver):
    try:
        remove_comments.login(id, password, driver)
        count = remove_comments.remove_comments(driver)
        return count
    except UnexpectedAlertPresentException:
        print('로그인 오류발생. 오류가 지속된다면 아이디와 비밀번호가 맞는지 확인해보세요')
        run(id, password, driver)
    except Exception as e:
        print('오류발생 오류내용 : ', e)

print('제작자 : samo623')
print('Github : https://github.com/samo623/everytime-comment-deleter')
print('Version : 1.0')
print('본 프로그램은 GNU General Public License v3.0을 적용받고 있습니다.')
print('Version : ',__version__)
count = run(id, password, driver)
print('삭제가 완료되었습니다.')
print('삭제된 댓글개수 : ', str(count))
