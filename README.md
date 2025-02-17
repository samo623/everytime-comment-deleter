# 에브리타임 댓글 자동 삭제 매크로
## 주의 : 기능들은 정상작동하지만  아직 개발중인 단계입니다.
 아이디와 비밀번호만 입력하면 에브리타임에서 내가 적은은 모든 댓글들을 빠르게 지워줍니다.
 
 ---

### 사용 방법

 #### 위 프로그램을 실행하기 위해서는 [Python](https://python.org/)과 [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/)를 필요로 합니다.

- [Python](https://python.org/)을 설치 후 selenium을 설치해주세요.
- [main.py](https://github.com/samo623/everytime-comment-deleter/blob/main/main.py)를 다운받고 8번, 9번줄의 ' ' <- 안에 각각 에브리타임 아이디와 비밀번호를 입력해주세요.
- 실행시 자동으로 로그인 후 댓글이 삭제되기 시작합니다.
- 로그인이 실패할 경우 프로그램을 다시 실행시키면 정상적으로 동작합니다.

### 위 프로그램은 Python의 selenium 패키지를 통해 로그인 후 삭제를 수행합니다. 

### 모든 정보는 에브리타임 측에만 전송됩니다.


# TODO
- [ ] 로그인시 버그 고치기
- [ ] UI 추가하기 