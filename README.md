# automate_generate_subtitle
Use speech2text from googleAPI
Use text_translator from NaverAPI

- 다음팟 인코더로 동영상에서 오디오만 추출함


그 오디오를 mono채널 flac파일로 변환함
#오디오 mono채널로 추출하는 사이트
https://trac.ffmpeg.org/wiki/AudioChannelManipulation

이후 구글 gs에 오디오 파일 올리고 

json 파일로 credential 파일 받아가지고 환경변수 추가해wnrh

구글api로 텍스트 추출함 (히카루의 바둑 61화 text따봄 : hikaru_61_mono_flac.txt)

그 후 네이버 API로 번역 (결과물 : translated.json)


### 참고
구글 언어코드 보는 곳
https://cloud.google.com/speech-to-text/docs/languages
 en-US , ko-KR , ja-JP

네이버 언어코드

한국어(ko)-영어(en), 한국어(ko)-일본어(ja), 한국어(ko)-중국어 간체(zh-CN), 한국어(ko)-중국어 번체(zh-TW), 한국어(ko)-스페인어(es), 한국어(ko)-프랑스어(fr), 한국어(ko)-러시아어(ru), 한국어(ko)-베트남어(vi), 한국어(ko)-태국어(th), 한국어(ko)-인도네시아어(id), 한국어(ko)-독일어(de), 한국어(ko)-이탈리아어(it), 중국어 간체(zh-CN) - 중국어 번체(zh-TW), 중국어 간체(zh-CN) - 일본어(ja), 중국어 번체(zh-TW) - 일본어(ja), 영어(en)-일본어(ja), 영어(en)-중국어 간체(zh-CN), 영어(en)-중국어 번체(zh-TW), 영어(en)-프랑스어(fr)

### 결과물 요약

텍스트 따온거 : 
![speech2txt](C:\Users\User1\Documents\Python Scripts\OpenApi\speech2txt_result.png)
네이버 파파고 번역물
![JPN_KOR](C:\Users\User1\Documents\Python Scripts\OpenApi\JPN2KOR_result.png)







