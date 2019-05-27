#!/usr/bin/env python
#-*- encoding : UTF-8 -*-

import json
import os


def get_config_parameters():
    wpath = os.path.dirname(__file__)
    wconfig = os.path.join(wpath, 'settings.json')
    with open(wconfig, 'r') as f:
        wdata = json.loads(f.read())
        outcome = wdata.copy()
        for wkey, wvalue in wdata.items():
            if wvalue == '':
                del outcome[wkey]
        return outcome
    return {}
