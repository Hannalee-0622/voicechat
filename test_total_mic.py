from openai import OpenAI
from pathlib import Path
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

client = OpenAI()

def record_audio():
    fs = 44100  # 샘플레이트
    seconds = 3  # 녹음 시간
    print('녹음을 시작합니다.')
    record = sd.rec(int(seconds * fs), samplerate=fs, channels=1)  # 스테레오 문제를 피하기 위해 모노로 변경
    sd.wait()
    print('녹음을 종료합니다.')

    audio_input_path = 'audio_input.wav'
    write(audio_input_path, fs, record)  # numpy 배열을 WAV 파일로 저장
    return audio_input_path

def conn_whisper(audio_input_path):
    with open(audio_input_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    print(response.text)  # 'response' 객체의 'text' 속성에 접근
    return response.text


def conn_chatgpt(text_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": text_input
        }
    ]
    )
    return response.choices[0].message.content

def conn_tts(text_output):
    response = client.audio.speech.create(
        model="tts-1",
        voice='alloy',
        input=text_output
    )
    audio_output_path = 'audio_output.mp3'
    with open(audio_output_path, 'wb') as f:
        f.write(response.content)
    return audio_output_path

def main():
    audio_input_path = record_audio()
    text_input = conn_whisper(audio_input_path)
    text_output = conn_chatgpt(text_input)
    audio_output_path = conn_tts(text_output)
    playsound(audio_output_path)

main()
