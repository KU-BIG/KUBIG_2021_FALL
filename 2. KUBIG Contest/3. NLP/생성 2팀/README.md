# 📚 CV_Generator
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/GoogleColab-F9AB00?style=flat-square&logo=GoogleColab&logoColor=white"/></a>&nbsp 
</p>

## 프로젝트 소개
- 프로젝트 주제: 자기소개서 생성 및 한 줄 요약기
- 기간: 2021.08.14 ~ 2021.09.02
- 팀명: MPTI (Make self-PR Through AI)
- 팀원: 기다연, 전지우, 이현규
<br>

## 사용 데이터셋/모델
- 합격자기소개서 데이터 : 잡코리아/링커리어 크롤링 <br>
- 생성모델 : GPT3
- 추출요약모델 : LexRank
<br>

## 디렉토리

### _algorithms_
- **train**: 데이터 전처리, GPT3 fine-tuning
- **generate**: fine-tuning된 모델 불러와 자기소개서 생성


### _data_
- **preprocessed_data**: 잡코리아/링커리어에서 크롤링 후 전처리한 데이터 csv 파일

### _ppt_
- 1차 발표자료
- 2차 발표자료
- 최종 발표자료


## 데모
Google Colab을 통해 구현해본 데모 버전입니다: 
<a href='https://colab.research.google.com/drive/1D5DCA-ulr_J_h6H12ZgcotHRfmIzSOBA?usp=sharing'><b>자기소개서 생성기</b></a>


## 프로젝트 진행 일정  
*매주 목요일 오전/월요일 오전에 주 2회의 정기 회의를 가졌습니다.*

|   no   |   일정   |   내용   |   과제 및 논의   | 
|:----------------------------|:----------------------------:|:--------------------:|:-------------------:|
|  1  | 2021.08.16 | 아이디어 회의 | 데이터 크롤링 (링커리어/잡코리아), Github 코드 공부, 데이터 전처리 방안 생각해오기 |
|  2  | 2021.08.19 | 데이터 크롤링/전처리 회의 | 각자 진행한 크롤링 내용/이슈사항 공유, 각자 생각해본 데이터 전처리 방안 공유 |
|  3  | 2021.08.23 | 데이터 전처리 방안/GPT-3 fine-tuning | Github 모델 코드 심화 공부 | 
|  4  | 2021.08.26 | GPT-3 fine-tuning | 모델 코드 공유, 각자 짜놓은 모델 코드 논의, GPT-3 fine-tuning 방법 확정 |
|  5  | 2021.08.30 | 텍스트 생성 알고리즘 완성/텍스트 요약 모델 학습 | TextRank/LexRank 텍스트 요약 모델 공부, GPT-3 하이퍼파라미터 튜닝 | 
|  6  | 2021.08.31 | 최종 발제 회의 | 최종 발제 자료 준비, 텍스트 요약 모델 적용 |

