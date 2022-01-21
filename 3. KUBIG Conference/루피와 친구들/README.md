# 루피와 친구들
### 백투더퓨처 - 과거 흑백사진을 컬러사진으로 변환하기
<br>

## 프로젝트 소개
- **목적:** 과거 흑백사진을 컬러사진으로 변환하여 그때의 역사 현장을 생생하게 되돌리기
- **기간:** 2021.09 ~ 2021.12
- **팀원:** 이나윤, 윤정현, 구은아   <br>
<br>

## 사용 데이터셋
- 1번째 모델: COCO Dataset
- 2번째 모델: image-net
- test에서 사용한 역사사진: 오픈아카이브
- **출처:**  https://archives.kdemo.or.kr/photo-archives/main
<br>

## 프로젝트 진행 일정  

|   회차   |   일정   |   내용   |   과제 및 논의   |
|:----------------------------|:----------------------------:|:--------------------:|:-------------------:|
|  1  | 2021.09.09 ~ 2021.10.07 | 주제 결정 | 적절한 주제와 사용할 모델 논의 | 
|  2  | 2021.09.30 ~ 2021.10.31| GAN 스터디 | GAN, pix2pix 논문 리뷰 |
|  3  | 2021.11.12 ~ 2021.11.18 | baseline 코드 작성 | 다양한 pix2pix 코드를 찾아보고 <br>우리 주제와 가장 적절한 코드 선정 |
|  4  | 2021.11.18 ~ 2021.11.27 | 이미지 크롤링 | 실제 모델에 적용할 역사 이미지 크롤링 후 <br>모델에 적용하여 성능 확인 |
|  5  | 2021.11.27 ~ 2021.12.28 | 모델 성능 개선 | 두 버전의 모델 작성 및 성능 비교, <br>모델 성능을 높이기 위해 다양한 시도 | 
|  6  | 2022.01.05 | 최종발표 | <a href="">PPT</a> | 
<br>

## 컬러 변환 샘플 
- 1번째 모델
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2eced919-61e1-4d98-bcae-b7cd73efd36c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220114T155715Z&X-Amz-Expires=86400&X-Amz-Signature=fedf031907d22fadf84ebb4a35b182165781868695ce8cbef67ed7f1f44f2f71&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">

- 2번째 모델
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/019a58c5-838b-458c-9e84-7b54b35816ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220114T155752Z&X-Amz-Expires=86400&X-Amz-Signature=201579d39d645353a20cb05a023e6c0f556e36d1b7ccee6c62f00bd132bd91a6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject">
