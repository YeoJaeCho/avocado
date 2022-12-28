# 아보카도
- 동작 인식 기반 어린이 율동 프로그램

## Project
- 분석 팀원 : 조여재, 엄대용, 최창수
- 개발 팀원 : 송소정, 전희진, 오유경
- 기간 : 2022/12/08 - 2023/01/?
- 발표 : 2023/01/?
- Model : mediapipe, fastdtw
 
## Data
- pinkpong1.mp4 : https://www.youtube.com/watch?v=VwzJOCHNH54
- dtw_sample_train.mp4 : pinkpong1.mp4 수정본1
- dtw_sample_test.mp4 : pinkpong1.mp4 수정본2
- clap_clap.mp4 : pinkpong1.mp4 수정본3 -> error data로 사용
- foot_stamp_clap.mp4 : pinkpong1.mp4 수정본4 -> error data로 사용
- verse1.mp4 : pinkpong1.mp4 수정본5
- verse2.mp4 : pinkpong1.mp4 수정본6
- 추가 예정
 
## Process
- sample data extract : pinkpong1 영상 내에서 1초 동안(3~4초) frame capture를 진행하여 이미지 파일을 출력하고 골격 데이터를 csv로 저장 (fps 30으로 설정)
- dtw using sample data :
 dtw_sample_train 과 dtw_sample_test 영상에서 skeleton 추출을 하여 csv로 저장하고,
 1. 12개의 각도 변수를 만들어서 fastdtw로 시계열 유사도를 구한 후 그 평균 값으로 score를 판단
 2. x, y 좌표를 flatten 해서 fastdtw로 시계열 유사도를 구한 후 그 평균 값으로 score를 판단
- cosine similarity using sample data : train과 test data 간의 코사인 유사도를 구하고 error data와 train data 간의 코사인 유사도 구하기 (코사인 유사도 값이 너무 높게 나와서 수정 필요함)
- dtw using longer sample data: 이전에 1초짜리 영상들 비교를 넘어서 긴 영상들 사이의 비교를 위해 보다 긴 verse1, verse2 data를 이용해서 dtw 구하기
