
# Faster R-CNN을 이용한 폐 x-ray detection

 <br /> 
 <br />  
 
## 프로젝트 배경
:point_up: 흉부 사진을 object detection을 통해 사전에 판단함으로써 효율적인 진료가 가능해짐   
:v: faster rcnn을 이용한 object detection  

 <br /> 
 <br />  
 
## 프로젝트 목적
   Mission 1 
 -  x-ray 이미지를 학습해 이상이 있는 이미지(Opacity)와 없는 이미지(None) 구분
 - 이상이 있는 경우 이상이 있는 곳의 위치 detection

 Mission 2 
 - x-ray 이미지를 학습해 Negative for Pneumonia, Typical Appearance, Indeterminate Appearance,  
   Atypical Appearance 중 어느 class에 속하는지 구분
 - Negative for Pneumonia (이상 없음) 이 아닌 모든 경우 각각의 모습을 나타내는 부분 detection


<br /> 
<br />  
 
## 프로젝트 개요 

 1.  ` 데이터 셋 `: https://www.kaggle.com/c/siim-covid19-detection    
 2.  ` 최종 df 생성 `: train_image_level.csv 와 train_study_level.csv를 studyID 기준으로 합친 후 바운딩 박스 좌표 및 클래스 값 변수 생성  
 3.  ` 학습 `: faster rcnn 을 이용 + 다양한 옵티마이저 이용  
 4.  ` mAP 계산 및 결과 시각화 `    

<br /> 
<br />  

## 결과
- Mission 1    
![image](https://user-images.githubusercontent.com/79436275/131669744-56c361aa-4dc4-4976-a2ea-2966c9758809.png)  
- Mission 2  
![image](https://user-images.githubusercontent.com/79436275/131672168-1f07a166-7e37-483d-94b4-32a2f5b1ebd1.png)


<br /> 

- reference :   
https://nuggy875.tistory.com/20  
https://www.kaggle.com/c/siim-covid19-detection/data  
https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173  
https://towardsdatascience.com/breaking-down-mean-average-precision-map-ae462f623a52  
