## Human Protein Atlas Image Classification


### 프로젝트 목적
microscope image에서 mixed patterns of protein을 분류


### 프로젝트 개요
1. 데이터셋: 
https://www.kaggle.com/c/human-protein-atlas-image-classification/data 

2. 데이터 imbalance 문제 해결을 위해 Augmentation Library를 이용하여 데이터 증강

3. 최적의 모델 찾기: ResNet50 fine-tune, VGG16 fine-tune, InceptionResNetV3 fine-tune의 validation f1 score를 비교.
InceptionResNetV3 선택

4. 채널 조절: 최적의 모델인 InceptionResNetV3에 4종류의 채널을 적용하여 validation f1 score를 비교. (R/2+Y/2, G/2+Y/2, B), (R=0, G, B=0), (R, G, B), (B/2+Y/2, R/2+Y/2, G)

5. 결과 및 결론
