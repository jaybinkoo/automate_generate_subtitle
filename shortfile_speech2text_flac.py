#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:34:35 2019

@author: jeffrey
"""
import io
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=24000,
        language_code='en-US')

    response = client.recognize(config, audio)
#    print(response)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    with open('{}.txt'.format(speech_file),'w') as f:
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            f.write(result.alternatives[0].transcript+'\n')
            print('writed')
#        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

transcribe_file('audio_files/obama.flac')