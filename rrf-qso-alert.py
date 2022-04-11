#!/usr/bin/python3

import time
import requests

from os import path
from os import system

timer   = 600
last    = 0
current = ''
actives = {
    'rrf' : 'RRF',
    'tec' : 'TECHNIQUE',
    'bav' : 'BAVARDAGE',
    'fon' : 'FON',
    'exp' : 'EXPERIMENTAL',
    'int' : 'INTERNATIONAL',
    'loc' : 'LOCAL',
    'reg' : 'REGIONAL',
}

while True:
    try:
        time.sleep(5)
        f = open('/etc/spotnik/network'); network = f.read(); f.close()
        current = actives[network.strip()]
        api = f"http://home.local:8049?room={current}"
        data = requests.get(api).json()
        for room in actives.values():
            if not room in data['elsewhere'][1]: continue
            if data['elsewhere'][1][room] == 'Aucune émission': continue
            if time.time() < last: continue
            f = open('/tmp/RRFRaptor_scan.tcl','w'); f.write('set RRFRaptor "'+room+'"'); f.close()
            last = time.time() + timer
            system('echo 203# > /tmp/dtmf_uhf')
    
    except KeyboardInterrupt: exit(0)
    except Exception as err: print(err); continue
