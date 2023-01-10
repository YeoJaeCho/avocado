# 아보카도
- 동작 인식 기반 어린이 율동 프로그램

## Project
- 분석 팀원 : 조여재, 엄대용, 최창수(sub)
- 개발 팀원 : 송소정, 오유경
- 기획 팀원 : 최창수
- 기간 : 2022/12/08 - 2023/01/18
- 발표 : 2023/01/19
- Model : mediapipe, cosine similarity, fastdtw, LSTM
 
## Data
- pinkpong1.mp4 : https://www.youtube.com/watch?v=VwzJOCHNH54
 ○. dtw_sample_train.mp4 : pinkpong1.mp4 수정본1
 ○. dtw_sample_test.mp4 : pinkpong1.mp4 수정본2
 ○. clap_clap.mp4 : pinkpong1.mp4 수정본3 -> error data로 사용
 ○. foot_stamp_clap.mp4 : pinkpong1.mp4 수정본4 -> error data로 사용
 ○. verse1.mp4 : pinkpong1.mp4 수정본5
 ○. verse2.mp4 : pinkpong1.mp4 수정본6
- head.mp4 : https://youtu.be/pd6qiaR0640
- shoulder.mp4 : https://youtu.be/LEgXDugKw1M
- knee.mp4 : https://youtu.be/pLNstNjTarc
- clap.mp4 : https://youtu.be/rrr7ORmElOQ
- left_foot.mp4 : https://youtu.be/2xljBk4qkjo
- right_foot.mp4 : https://youtu.be/qGZuYcRJoqs
- both_foot.mp4 : https://youtu.be/8QuVoz8fg2g
- yeah.mp4 : https://youtu.be/DOMnnqTTXjI
- 추가 예정
 
## Process
- sample data extract : 
 ○. data : pinkpong1.mp4
 ○. 1초 동안(3~4초) frame capture를 진행하여 이미지 파일을 출력하고 
 ○. 골격 데이터를 csv로 저장 (fps 30으로 설정)
- dtw using sample data :
 ○. data : dtw_sample_train.mp4, dtw_sample_test.mp4
 ○. skeleton 추출을 하여 csv로 저장
 ○. 12개의 각도 변수를 만들어서 fastdtw로 시계열 유사도를 구한 후 그 평균 값으로 score를 판단
 ○. x, y 좌표를 flatten 해서 fastdtw로 시계열 유사도를 구한 후 그 평균 값으로 score를 판단
- cosine similarity using sample data : 
 ○. data : dtw_sample_train.mp4, dtw_sample_test.mp4
 ○. train과 test data 간의 코사인 유사도를 구하고 
 ○. error data와 train data 간의 코사인 유사도 구하기 
 ○. 코사인 유사도 값이 너무 높게 나와서 수정 필요함
- dtw using longer sample data: 
 ○. data : verse1.mp4, verse2.mp4
 ○. 이전에 1초짜리 영상들 비교를 넘어서 긴 영상들 사이의 비교를 위해 위의 영상을 이용하여 dtw 구하기
 - LSTM model version1 :
 ![v1_skeleton_information](https://user-images.githubusercontent.com/109574182/211456133-044905fd-415d-4de4-9870-4c19f648aadd.jpg)
 ○. data : head.mp4, shoulder.mp4, knee.mp4, clap.mp4, left_foot.mp4, right_foot.mp4, both_foot.mp4, yeah.mp4
 ○. create_data : 영상 내의 각 프레임을 불러와서 mediapipe를 이용하여 그림에 표시된 벡터를 구하고 벡터 간의 각도를 구한 data를 생성
 ○. model : 생성한 data를 가지고 LSTM model에 학습
 ○. test_model : 영상을 넣어서 pose estimation이 잘 되는지 확인해보고, 직접 캠을 연결해서도 확인
 ○. 모델 성능이 12% 정도 밖에 되지 않음, pose estimation이 잘 되지 않음
 - LSTM model version2 :
 ![v2_skeleton_information](https://user-images.githubusercontent.com/109574182/211456698-d79636fd-3f8c-4117-a618-16391783a932.jpg)
 ○. data : head.mp4, shoulder.mp4, knee.mp4, clap.mp4, left_foot.mp4, right_foot.mp4, both_foot.mp4, yeah.mp4
 ○. create_data : 영상 내의 각 프레임을 불러와서 mediapipe를 이용하여 그림에 표시된 벡터를 구하고 벡터 간의 각도를 구한 data를 생성
 ○. model : 생성한 data를 가지고 LSTM model에 학습
 ○. test_model : 영상을 넣어서 pose estimation이 잘 되는지 확인해보고, 직접 캠을 연결해서도 확인
 ○. 모델 성능이 90%가 넘었고, 완벽하지는 않지만 대부분의 동작들이 모두 인식됨
 ○. both_foot의 경우 가만히 서있는 것과 유사한 skeleton이기 때문에 가만히 서있을 때 both_foot이라고 인식한다는 단점이 존재
 
