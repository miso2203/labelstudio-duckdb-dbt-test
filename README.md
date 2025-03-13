## Directory

```
.
├── data
│   ├── json_data            : 타이어 샘플 여러 개가 들어있는 json 파일
│   ├── json_data_one_task   : 타이어 샘플 1 개씩 들어있는 json 파일
│   ├── json_done            : json_data 폴더 라벨링 결과
│   ├── pre_annotation_json  : Python SDK test json 파일
│   ├── samples              : 타이어 샘플 이미지 10장
│   └── samples_done         : samples 폴더 라벨링 결과
└── src
    ├── sdk_test             : Python SDK test 코드
    └── yolo_pred_test       : YOLO prediction test 코드
```
<br>


## Label Studio
:link:[라벨스튜디오 notion](https://dahye0322.notion.site/1af5a87878ee80c689b2f32fdcec332f?pvs=4)
- 빠른 시작
- 환경 변수 세팅
- 프로젝트 데이터의 로컬 경로 설정
- 라벨링 인터페이스 설정
- JSON 형식으로 데이터 import
- JSON 형식 데이터를 Source Cloud Storage 연동
- 데이터 확인
