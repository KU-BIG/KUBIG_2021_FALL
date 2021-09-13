# 뉴스 토픽 분류 AI 경진대회
![image](https://user-images.githubusercontent.com/77607220/133032810-85b353f3-c930-4be6-9226-d513a71c445d.png)


## 프로젝트 목적
: 연합뉴스 제목만으로 뉴스 토픽을 정확히 예측하는 것 
- 한국어 뉴스 헤드라인을 이용하여, 뉴스의 주제를 분류하는 알고리즘 개발


## 프로젝트 개요
 1. 데이터 특성 확인
 2. 데이터 전처리
 3. 사용 모델 결정
 4. 결과

### 데이터 특성 확인

![image](https://user-images.githubusercontent.com/77607220/133032530-a4fab1c2-83c9-452e-9e1e-f94b012bcf47.png)
![image](https://user-images.githubusercontent.com/77607220/133032555-19ca6d41-f99c-457b-a724-08c4cd6432be.png)

-훈련데이터 레이블 분포: 불균형 처리 필요없다고 판단
-형태소분석기 사전에 등록되지 않은 고유명사가 많음 -> 사전등록 필요

### 데이터 전처리
1. shuffle 후 train/test 데이터 분리
2. 데이터 정제: 한글, 영어, 한자, 숫자를 제외한 나머지 제거
3. 미등록 단어 사전등록 후 토큰화 진행: kiwipiepy 활용
4. 추가 불용어 지정 및 제거: 각 토픽별 상위 200 단어의 교집합 중에 지정
5. 정수인코딩: 빈도수 1회인 희귀단어 제외
6. 패딩: 최대 길이로 패딩 진행

### 사용 모델 결정 
- BiLSTM: 
- BiLSTM (양방향 LSTM)은 두 개의 독립적인 LSTM을 사용하는 구조. 
- 문장을 왼쪽에서 오른쪽으로 읽는 LSTM과는 달리 뒤의 문맥까지 고려하기 위해 문장의 오른쪽에서 반대로 읽는 역방향의 LSTM을 함께 사용. 
결과적으로 두 가지 정보를 모두 고려하여 출력층에서 보여줌
-BiLSTM 모델은 Public 0.8225, Private 0.7908의 성능을 보여줌

![image](https://user-images.githubusercontent.com/77607220/133032752-8ebad7fe-dc4c-47ad-b00b-a134e697536d.png)

- koBERT:
- KoBERT는 SKT에서 BERT를 기반으로 만든 모델. 구글의 BERT base multilingual cased에서 한국어 성능의 한계를 극복하기 위해 만들어짐.
- KoBERT는 모델 학습을 위해 한국어 위키에서 500만개의 문장과 5400만개의 단어를 사용함. 구글에서 한글 위키 기반으로 학습시킨 Setencepiece tokenizer와 8000개의 단어가 들어있는 사전 사용. 
결과적으로 네이버 영화 리뷰 데이터를 통한 감성 분류 결과, BERT와 KoGPT2 보다 좋은 성능을 보여줌. (출처: https://github.com/SKTBrain/KoBERT/blob/master/README.md)
- 이번 대회에서도 BiLSTM 모델(Public 0.8225, Private 0.7908) 대비 Public 0.8617, Private 0.8293 으로 더 좋은 성능을 보여줌.  


### 결과
![image](https://user-images.githubusercontent.com/77607220/133032708-0c5e4d2c-d879-4327-bd11-815a36c4c16e.png)

BiLSTM 모델: Public 0.8225, Private 0.7908
KoBERT 모델: Public 0.8617, Private 0.8293
