# automate_generate_subtitle
Use speech2text from googleAPI
Use text_translator from NaverAPI

- 다음팟 인코더로 동영상에서 오디오만 추출함


그 오디오를 mono채널 flac파일로 변환함
#오디오 mono채널로 추출하는 사이트
https://trac.ffmpeg.org/wiki/AudioChannelManipulation

이후 구글 gs에 오디오 파일 올리고
구글api로 텍스트 추출하기

그 후 네이버 API로 번역


## json 파일로 credential 파일 받아가지고 환경변수 추가해줘야함


