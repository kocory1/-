# 옷마카세 (Otma Case)

FastAPI를 사용한 옷장 관리 시스템 API

## 프로젝트 구조

```
옷마카세/
├── src/
│   ├── main.py          # FastAPI 앱 메인 파일
│   ├── routers/         # API 라우터들
│   └── services/        # 비즈니스 로직 서비스들
├── requirements.txt     # Python 의존성 패키지
├── .gitignore          # Git 무시 파일 목록
└── README.md           # 프로젝트 설명서
```

## 설치 및 실행

1. **가상환경 생성 및 활성화**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **의존성 패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **서버 실행**
   ```bash
uvicorn src.main:app --host=127.0.0.1 --port=8080 --reload --reload-dir src --log-level=info   ```

4. **API 문서 확인**
   - Swagger UI: http://127.0.0.1:8080/docs
   - OpenAPI 문서: http://127.0.0.1:8080/open-api-docs

## API 엔드포인트

- `GET /`: Hello World 메시지 반환

## 개발 환경

- Python 3.12.4
- FastAPI 0.116.1
- Uvicorn 0.35.0
- watchfiles 