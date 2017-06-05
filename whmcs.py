#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import requests
import hashlib
import config
import json

class WhmcsApi:
    def __init__(self):
        self.i = 2

    @staticmethod
    def invoke_whmcs_api(action, format, parameters):
        content_type = "application/%s" % format
        headers = {'content-type': content_type}
        payload = {
            'username': config.API_USER,
            'password': hashlib.md5(config.API_PASSWORD).hexdigest(),
            'responsetype': format,
            'action': action
        }
        payload.update(parameters)
        logging.info("PAYLOAD: %s" % payload)
        response = requests.post(config.API_URL, data=payload)
        if (response.status_code == 200):
            logging.info("%s" % response.text)
            result = json.loads(response.text)
            return result
        else:
            print "%s" % response.text
            return None
