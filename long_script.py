#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:55:09 2019

@author: jeffrey
"""

def transcribe_gcs(uri_gs):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()



    audio = types.RecognitionAudio(uri = uri_gs)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code='ja-JP')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=9000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    with open('{}.txt'.format(uri_gs.split('/')[-1]),'w') as f:
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            f.write(result.alternatives[0].transcript)
#            print(u'Transcript: {}'.format(result.alternatives[0].transcript))
#            print('Confidence: {}'.format(result.alternatives[0].confidence))

transcribe_gcs('gs://jeffrey_audio_files/hikaru_61_mono.flac')