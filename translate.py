#import json

import argparse

import six

""" Translates provided orig_text to target language string """
def translate(orig_text):
    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()
    target = "fr" #change this later
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    result = translate_client.translate(text, target_language = target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))

