# (가제) 동작 인식 기반 어린이 율동 프로그램

## Project
- 분석 팀원 : 조여재, 엄대용, 최창수
- 기간 : 2022/12/08 - 2023/01/?
- 발표 : 2023/01/?
- Model : mediapipe, LSTM
 
## Data
- pinkpong1
  핑크퐁 [머리 어깨 무릎 짝] (2:59) 
  https://www.youtube.com/watch?v=VwzJOCHNH54
- 추가 예정
 
## Process
- sample data extract : pinkpong1 영상 내에서 1초 동안(3~4초) frame capture를 진행하여 이미지 파일과 골격 데이터를 csv로 저장 (fps 30으로 설정)
