from openai import OpenAI
from pathlib import Path

client = OpenAI()

def conn_whisper():
    return text_input

def conn_chatgpt(text_input):
    return text_output

def conn_tts(text_output):
    return audio_output_path

def main():
    # 마이크 inpiut => audio_input_path
    text_input = conn_whisper()
    text_output = conn_chatgpt(text_input)
    audio_output_path = conn_tts(text_output)
    #audio_output_path의 mp3를 play
    return

main()