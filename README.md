# ai26

## 테스트

##### 2023-04-14 일기쓰기, 공지사항, 공개일기장, 로그인/회원가입 기능이 포함된 flask 파일 넣음 (채원)
##### 2023-04-17 (전체 공유) 일기쓰기에 문법교정 기능, 일기 내용 태그 생성(문장 요약) 미완성, 공개일기장 형태 수정. 
##### 2023-04-19 (for 상준, 진혁) 공유를 위해서 깃허브에 myproject 업로드. 폴더 청소함. (채원)
##### 2023-04-24 (for 전체공유) 
##### (해결함) "Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`." <br>
grammar.py 관련 문제 : 검토+저장하기를 클릭했을 때, 문장이 모두 문법 검사된 상태로 배출되지 않고, 50%는 생략되서 나오는 문제가 발생. <br>
max_length, truncation 문제로 추측 진행. <br>
~~현시점까지 오류를 해결하지 못해서 공유.(채원)~~
##### 2023-04-26 (for 전체공유) 04-25까지 작업한 코드 덮어씌우기로 삭제됨. 회원정보 수정기능, 일기 문법검사 기능 복구중.
##### 2023-04-26 + 공개일기장 정렬기능 추가

##### 2023-04-27 (for 전체공유) 회원정보 수정기능 완료
##### 2023-04-28 Paraphrases 기능 오류 수정(+ 닫기 버튼)


#### 2023-05-04 실험
amazon lightsail : ubuntu 무료버전 라이트세일 고정 IP 주소 : 43.200.159.39
flask를 받아들이질 못함
### "killed"
![image](https://user-images.githubusercontent.com/114221089/236110364-b4756e50-4b26-488d-a248-d4748725e582.png)

### cpu가 2배 큰 ubuntu를 구매해도 20분간 중지됨
![image](https://user-images.githubusercontent.com/114221089/236158068-80e9da2e-8a43-4339-a07a-6c825343c69e.png)


AWS EC2 : t2.micro(무료버전)(ubuntu) 
CPU 가용률 99% 이상으로 flask를 받아들이질 못함
> torch, transformer, torch library
### "killed" 
![image](https://user-images.githubusercontent.com/114221089/236109639-3d24b224-3437-4658-bfea-b623245e248e.png)

#### 2023-05-08 실험A
lightsail 2GB 서버로 실행

### stop
![image](https://user-images.githubusercontent.com/114221089/236973858-109dfba9-6287-4bfb-912e-9a9261e74c93.png)
pytorch_model.bin 100% 이후로 진행 불가

#### 2023-05-09 실험B
lightsail 4GB(20$ 버전)으로 사용 시도
![image](https://user-images.githubusercontent.com/114221089/236977560-41173804-5911-49e8-b117-a5ad437fe02f.png)
### "killed"

- 현재 실행중인 Gunicorn 프로세스에서 계속해서 "CRITICAL WORKER TIMEOUT" 메시지와 함께 Worker 프로세스가 종료되었다는 메시지가 출력되고 있습니다. 이러한 메시지는 Worker 프로세스가 응답하지 않거나 일정 시간 내에 작업을 완료하지 못했을 때 발생할 수 있습니다.

- 일반적으로 이러한 문제는 웹 애플리케이션의 처리 시간이 너무 오래 걸려서 발생할 수 있습니다. 이 경우에는 코드를 최적화하거나, 처리 시간이 오래 걸리는 작업을 백그라운드 작업으로 분리하는 등의 방법을 사용하여 문제를 해결할 수 있습니다. 또는 Gunicorn 설정을 조정하여 Worker 프로세스의 개수를 늘리거나 요청 대기 시간(timeout)을 조정할 수도 있습니다.

- 따라서 이 경우에는 Gunicorn 설정을 조정하거나 애플리케이션 코드를 분석하여 원인을 파악하고 해결해야 합니다


#### 2023-05-09 수정
- navbar, sidebar의 제목 순서 변경 : 공지사항, 사용설명서, 공개일기장, 일기쓰기

### 도커로 이동
![image](https://user-images.githubusercontent.com/114221089/237052505-e6fbf005-6c52-4ef0-a4b2-ee53518ca937.png)

### 홈페이지 도커 오픈 성공
![image](https://user-images.githubusercontent.com/114221089/237060539-8d0a2950-b9b4-4373-ada6-b68ca426f9a3.png)


### 230511 도커 테스트

### 신원 미상의 접근 불가
#### ex) 502 bad gateway, 504 gateway timeout 송출

![image](https://github.com/ChaeWonIm0/englishdiary/assets/114221089/07addaf1-fc1e-48be-a8c4-c4557a4ded43)

### 230512 docker 기록

![image](https://github.com/ChaeWonIm0/englishdiary/assets/114221089/8d4ff3bc-9763-4983-ab46-6695aec70af2)

#### EWS_diary 초기버전 서버 환경 가능
