# Voicechat

> **An AI-powered voice conversation mobile app with Python backend and Flutter front end.**  
> **AI 기반 음성 대화 모바일 앱 (Python 백엔드 + Flutter UI)**

---

## Overview / 개요

This project implements a mobile app that lets users speak, analyze, and receive voice responses via OpenAI APIs.  
본 프로젝트는 사용자의 음성을 OpenAI API를 통해 텍스트로 변환(STT), GPT로 분석, TTS로 다시 음성 응답을 제공하는 모바일 앱입니다.

- **Backend**: Python Flask server  
  **백엔드**: Python Flask 서버
- **Frontend**: Flutter mobile UI  
  **프론트엔드**: Flutter 모바일 UI
- **APIs**: Whisper STT, GPT Text Analysis, TTS Response  
  **사용된 API**: Whisper STT, GPT 언어 분석, TTS 음성 합성

---

## Features / 주요 기능

1. **Voice-to-Text (STT)**  
   - Captures user speech in real time and converts to text via Whisper API.  
   - Whisper API를 활용해 사용자 음성을 실시간 텍스트로 변환합니다.

2. **Natural Language Understanding**  
   - Sends the converted text to GPT API for semantic analysis and intent detection.  
   - 변환된 텍스트를 GPT API로 전송하여 의미 분석 및 의도 파악을 수행합니다.

3. **Text-to-Speech (TTS) Response**  
   - Generates a voice response from GPT output using TTS API.  
   - GPT 분석 결과를 TTS API로 음성 응답으로 생성합니다.

4. **Separated Architecture for Performance & Stability**  
   - **Monolithic → Microservices**: Initially all features ran in the Flutter app, causing latency & instability.  
   - **분리 구조**: 초기에는 Flutter 앱 내에서 모든 처리를 수행했으나, 지연과 오류 발생이 잦았습니다.
   - **Solution**: Speech processing & model calls moved to Python server; Flutter handles UI only.  
   - **해결책**: 음성 처리 및 모델 호출을 Python 서버로 이전하고, Flutter 앱은 UI/UX에 집중하도록 구조를 분리했습니다.

5. **60% Faster Responses**  
   - Reduced average round-trip time from **7.2 s → 2.9 s**.  
   - 평균 응답 시간이 **7.2초 → 2.9초**로 약 60% 단축되었습니다.

6. **Cross-Platform Support**  
   - Android & iOS compatible via Flutter.  
   - Flutter를 통해 Android 및 iOS 지원.

7. **Simple & Intuitive UI**  
   - Clean, voice-driven interface with minimal buttons: Record, Stop, Play Response.  
   - 기록, 정지, 재생 버튼만 있는 깔끔한 음성 중심 UI를 제공합니다.

---

## Project Structure / 디렉터리 구조

```

/
├── backend/
│   ├── app.py           # Flask server entrypoint
│   ├── requirements.txt # Python dependencies
│   └── utils/           # Whisper, GPT, TTS helper modules
└── mobile/
├── lib/
│   ├── main.dart    # Flutter app entrypoint
│   └── widgets/     # UI components
└── pubspec.yaml     # Flutter dependencies

````

---

## Setup & Run / 설치 및 실행

1. **Backend**  
   
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```
   
3. **Mobile**
   ```bash
   cd mobile
   flutter pub get
   flutter run
   ```
---

## Performance / 성능 지표

| Metric             | Before / 이전 | After / 이후 |
| ------------------ | ----------- | ---------- |
| Avg. Response Time | 7.2 s       | 2.9 s      |
| Latency Reduction  | —           | ↓ 60%      |
| System Stability   | Unstable    | Improved   |

---

## Contributors / 기여자

* **Hanna Lee** – Project lead & mobile UI
  프로젝트 리드 & 모바일 UI 개발
* **Hanna Lee, Jaehee Kim, Seungyeon Lee, Hyungwoo Kim** – Python server & API integration
  백엔드 팀 – Python 서버 및 API 연동

---

## License / 라이선스

This project is licensed under the MIT License.

---
