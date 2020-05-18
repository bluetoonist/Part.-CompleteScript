# 완성된 스크립트 저장소
완성된 스크립트만 그룹화

<h2>chromeHistoryScript</h2>
<p>
&nbsp; MNU 네트워크 보안 프로젝트 1, chrome 브라우저 사용자의 history 파일의 내용을 파싱해 보여주는 파이썬 코드
</p>
<h4>Requirement</h4>
&nbsp;[+] Python : psutil, sqlite3, os 
<hr>

<h2>FileChase</h2>
<p>
&nbsp; 실행 중인 파일의 경로를 추적해 특정 폴더에 추적된 파일의 '복사본'을 저장하는 스크립트, 코드에서는 "AcroRd32.exe"로 현재 열려있는 pdf를 추적함.
</p>
<h4>Requirement</h4>
&nbsp; [+] Python : psutil,
<hr>


<h2>IBookCrawler</h2>
<p>
&nbsp; table 태그를 요소로 쓰는 'http://www.ibookland.com/home/userguide/bookSearch.htm' 에서 동적 크롤링을 시도해봄
</p>
<h4>Requirement</h4>
&nbsp;[+] Python : BeautifulSoup, Selenium<br>
&nbsp;[+] chromedriver.exe
<hr>

<h2>MNU_MAIL_LIST</h2>
<p>
&nbsp; urllib와 cookie로 인증하는 방식에서 동적 크롤링 요소를 쓰지 않고 크롤링을 해보기 위해 MNU의 메일 시스템에 로그인해 내용을 가져오는 스크립트
</p>
<h4>Requirement</h4>
&nbsp;[+] Python : getpass, BeautifulSoup, urllib
<hr>

<h2>MokpoCityHall_Project</h2>
<p>
&nbsp; 목포시 공공일자리 참여 사업에 참가 중 네이버 밴드에 업로드 된 자료를 더 편히 다운로드 받고 목포 시청 사이트에 업로드 시키기 위해 만든 크롤링 소스 (데모 영상 존재)
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  BeautifulSoup, urllib, selenium, shutil
<hr>

<h2>News_Capture</h2>
<p>
&nbsp; 다음 뉴스 실시간 캡쳐 코드 데모 영상은 "New_macro_capture.py" 는 https://klonic.tistory.com/39?category=764442, "News_macro_live.py"는 https://klonic.tistory.com/41?category=764442 를 참조
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  BeautifulSoup, requests, selenium
<hr>

<h2>Open API</h2>
<p>
&nbsp; open API의 사용 숙지를 위해 KaKao, Vworld OPEN API를 이용해 위도와 경도를 응답 받는 코드
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  urllib,
<hr>

<h2>Sinagong Download</h2>
<p>
&nbsp; IDOR 취약점은 안전하지 않은 객체를 직접 참조해 사이트 상으로는 숨겨져있지만 r,w,x 권한은 오픈되어 있어 URI를 참조하면 객체를 다운로드 할 수 있음, 해당 스크립트를 이용하는 사이트에서는 IDOR은 발견되지 않았지만(필자 지식으로는) IDOR를 이용할 수 있는 요소는 이렇게 만들어지지 않을까하는 느낌으로 작성한 코드
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  zipfile, wget
<hr>

<h2>SuSan Mokpo</h2>
<p>
&nbsp; 파이썬을 배우고 무언가 처음 만들어 본 게 있다면 해당 디렉터리안의 소스 코드이다. 해양 수산청에서 직원 목록이 공개된 사이트에서 크롤링을 시도해보기 위해 필자가 가장 처음 만들었던 소스 코드
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  selenium, BeautifulSoup
<hr>

<h2>MNU PROJECT 3th</h2>
<p>
&nbsp; 윈도우 로그를 파싱해주는 라이브러리인 python-evtx를 이용해 만들어둔 코드, 해당 코드를 실행 시키기 위해 필요로 하는 라이브러리가 다수 존재
</p>
<h4>Requirement</h4>
&nbsp;[+] Python :  pyqt, evtx, mulitiprocessing
<hr>

<p>
<h4>#Note</h4>
https://github.com/bluetoonist/Part_-Python/tree/master/MiniProject 저장소에 모아둔 코드도 정리요망
</p>