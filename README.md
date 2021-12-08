## Data Augmentation

Yolo 학습할때 .txt 파일이 필요. (.txt 파일은 이미지 경로가 담긴 파일)  
이미지 라벨을 마친 뒤에 Yolo 학습전에 .txt 파일을 쉽게 만들어주는 프로그램
  </br></br>

## 사용법
### 파라미터
```yaml
origin_img_path: ./img # 원본 이미지 경로
txt_file_name: yolo # txt 파일 이름
txt_save_path: ./ #txt 저장 경로
```
</br>

### 명령어
conda 환경설치 방법은 상위 폴더를 참조
```
(base) $ conda activate 3w

(3w) $ python src/yolo_txt_generator.py
```