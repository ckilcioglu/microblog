import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        current_app.logger.warning('translator service is not configured')
        return _('Error: translator service is not configured')
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        current_app.logger.warning('translator service failed')
        return _('Error: the translation service failed')
    return json.loads(r.content.decode('utf-8-sig'))