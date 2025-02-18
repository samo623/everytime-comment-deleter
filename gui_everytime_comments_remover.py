import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from mainui import Ui_MainWindow  
import remove_comments  
from version import __version__

print (__version__)

class CommentThread(QThread):
    log_signal = Signal(str)  
    finished_signal = Signal(bool)  

    def __init__(self, user_id, user_pw, retry_count=0, max_retries=10):
        super().__init__()
        self.user_id = user_id
        self.user_pw = user_pw
        self.retry_count = retry_count  
        self.max_retries = max_retries  
        self.driver = None

    def run(self):
        try:
            if self.driver is None:  
                self.log_signal.emit("브라우저를 초기화합니다...")
                self.driver = webdriver.Chrome()  

            self.log_signal.emit("로그인 중입니다...")
            remove_comments.login(self.user_id, self.user_pw, self.driver)
            self.log_signal.emit("로그인 성공!")
            self.log_signal.emit("댓글 삭제를 시작합니다...")
            counts = remove_comments.remove_comments(self.driver)
            self.log_signal.emit("댓글 삭제가 완료되었습니다!")
            self.log_signal.emit("삭제된 댓글개수 : ", str(counts))
            self.finished_signal.emit(True)  

        except UnexpectedAlertPresentException:
            if self.retry_count < self.max_retries:
                self.log_signal.emit(f"로그인 오류 발생. 다시 시도합니다... (재시도 {self.retry_count + 1}/{self.max_retries})")
                self.retry_count += 1
                
                if self.driver:
                    self.driver.quit()
                    self.driver = None  

                self.run()  
            else:
                self.log_signal.emit("최대 로그인 시도 횟수를 초과했습니다. 아이디, 비밀번호 확인후에 다시 시도해주세요.")
                self.finished_signal.emit(False)  

        except Exception as e:
            self.log_signal.emit(f"오류 발생: {str(e)}")
            self.finished_signal.emit(False)  

        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None  
                self.log_signal.emit("브라우저를 닫았습니다.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.pushButton.clicked.connect(self.prepare_remove_comments)

        
        self.comment_thread = None
        

    def log_message(self, message: str):
        text_edit = self.ui.plainTextEdit

        
        current_text = text_edit.toPlainText()
        updated_text = current_text + message + "\n"
        text_edit.setPlainText(updated_text)

        
        cursor = text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)  
        text_edit.setTextCursor(cursor)  
        text_edit.ensureCursorVisible()  

    def prepare_remove_comments(self):
        
        user_id = self.ui.lineEdit.text()
        user_pw = self.ui.lineEdit_2.text()   

        if not user_id or not user_pw:
            self.log_message("ID 또는 비밀번호를 입력해주세요.")
            return

        
        if self.comment_thread and self.comment_thread.isRunning():
            self.log_message("작업이 이미 진행 중입니다. 잠시만 기다려주세요.")
            return

        
        self.start_comment_thread(user_id, user_pw)

    def start_comment_thread(self, user_id, user_pw):
        """
        새로운 댓글 삭제 스레드를 시작합니다.
        """
        self.comment_thread = CommentThread(user_id, user_pw)

        
        self.comment_thread.log_signal.connect(self.log_message)

        
        def handle_finished(success):
            if success:
                self.log_message("작업이 성공적으로 완료되었습니다.")
            else:
                self.log_message("작업이 실패했습니다. 프로그램을 종료하거나 설정을 확인하세요.")

        self.comment_thread.finished_signal.connect(handle_finished)

        
        self.comment_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
