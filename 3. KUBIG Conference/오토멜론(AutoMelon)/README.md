# 오토멜론(AutoMelon)
### 멜론 플레이리스트에 어울리는 곡 추천시스템 구축
![image](https://user-images.githubusercontent.com/91919178/149716795-ca9f8ad0-e24e-463f-912c-107fcb1b80f1.png)
<br>

## 프로젝트 소개
- **목적:** 멜론 플레이리스트에 어울리는 곡과 태그 목록을 추천
- **기간:** 2021.09.09 ~ 2022.01.08.
- **팀원:** 13기 배은지, 14기 김수경, 14기 남이량, 14기 오화진  <br>
<br>

## 사용 데이터셋
- Kakao arena의 Melon Playlist Continuation 대회에서 제공하는 데이터셋
- 플레이리스트 데이터(train.json, val.json)
- 곡 메타 데이터(song_meta.json): 곡 장르 리스트 컬럼 활용
- 장르 메타 데이터(genre_gn_all.json)
- **출처:** https://arena.kakao.com/c/8/data 
<br> 

## 사용한 모델
**1. Playlist-based Collaborative filtering**
- 빈도수 기반 weighting 기법(bm25) 활용
- 유사도 계산: 내적, 자카드 계수 <br>
**2. Collaborative filtering + 곡 장르 데이터 추가**
- 협업 필터링 모델에 각 플레이리스트별 장르 빈도수 데이터 추가 활용
**3. Word2Vec: 플레이리스트 제목 활용**
- 플레이리스트 제목 토큰화: KoNLPy의 okt, Khaiii 형태소 분석기 활용
- Word2Vec으로 플레이리스트 제목과 곡, 태그 임베딩
**4. 협업필터링 + Word2Vec** (가장 높은 성능)
- 협업필터링(곡 추천) + Word2Vec(태그 추천)
**5. AutoEncoder**
- train data에서 특정 횟수 이상 등장한 곡과 태그를 one-hot encoding하여 학습에 활용
**6. AutoEncoder with Like_cnt + Word2Vec**
- 플레이리스트별 좋아요 수 데이터 추가
- 오토인코더의 곡 예측 결과 + Word2Vec의 태그 예측 결과
**7. LightFM**
- Collaborative 모델과 Content-based 모델의 장점을 결합한 모델
<br>

## 프로젝트 진행 일정  

|   주차   |   일정   |   내용   |   과제 및 논의   |
|:----------------------------|:----------------------------:|:--------------------:|:-------------------:|
|  1주차  | 2021.01.01 |  |  |
|  2주차  | 2021.01.01 |  |  |
|  3주차  | 2021.01.01 |  |  |
|  4주차  | 2021.01.01 |  |  |
|  5주차  | 2021.01.01 |  |  | 
<br>

## Reference
