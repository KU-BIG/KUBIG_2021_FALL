# 서울시 따릉이 자전거 이용 예측 프로젝트 :chart_with_upwards_trend:
2021-2 KUBIG CONTEST - ML SESSION

## :bowtie: 팀 소개
- 13기 박재찬
- 14기 김유민
- 14기 오화진
- 14기 제갈예빈

## :memo:프로젝트 소개
> 데이콘에서 제공하는 공공 빅데이터인 서울시 따릉이 데이터를 이용하여 인공지능 모델 개발 
- 2017년 4월 1일부터, 5월 31일까지 시간별로 서울시 따릉이 대여수와 기상상황 데이터가 주어진다.
- 각 날짜의 1시간 전의 기상상황을 바탕으로 1시간 후의 따릉이 대여수를 예측한다.

### :paperclip: 데이터 설명 
- 데이터 셋 : https://dacon.io/competitions/open/235576/data
- id :날짜와 시간 별 id
- hour : 시간
- hour_bef_temperature : 1시간 전 기온
- hour_bef_precipation : 1시간 전 비 정보, 비가 오지 않았으면 0, 비가 오면 1 => dummy!
- hour_bef_windspeed : 1시간 전 풍속(평균)
- hour_bef_humidity : 1시간 전 습도
- hour_bef_visibility : 1시간 전 시정(視程), 시계(視界)(특정 기상 상태에 따른 가시성을 의미)
- hour_bef_ozone : 1시간 전 오존
- hour_bef_pm10 : 미세먼지(머리카락 굵기의 1/5에서 1/7 크기의 미세먼지)
- hour_bef_pm2.5 : 미세먼지(머리카락 굵기의 1/20에서 1/30 크기의 미세먼지)
- count : 시간에 따른 따릉이 대여 수

##  :mag_right: 프로젝트 개요

* [x]  결측치 처리 - 새벽 1시 데이터를 포함한 mice imputation 진행, IQR, LOF 방법으로 이상치 처리
* [x]    피쳐 엔지니어링 - hour를 peak 기준으로 카테고리 변수 추가 생성, 23시와 01시를 고려한 sin 처리
* [x]  학습 모델 : ScikitLearn - ExtraTreesRegressor, LightGBM
* [x]  오토ML 사용

## :calendar: 프로젝트 일정 
|주차| 일정  | 세부 내용 | 
|:---:|:---:|:---:| 
|   1주차   | EDA 및 전처리| 결측치 처리 방법 스터디 : delete, simple imputation(regression, constant num), multiple imputation(mice 등)| 
|   2주차   | 데이터 전처리| 이상치 제거 스터디  : IQR, Isolation Forest, LOF, Minimum Covariance Determinant 등| 
|   3주차   | scaler 선택, feature engineering | minmax, standard, robust scaler / skewed 변환, 시간 변수에 대한 sin화, category범주화 등 | 
|   4주차   | 모델링 & 하이퍼파라미터 튜닝 | ML세션에서 익힌 regression model 활용한 예측 모델링 |
|   5주차   | 경진대회 발표 | :microphone: | 


