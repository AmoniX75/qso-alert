#!/usr/bin/python3

import requests
import time
from datetime import datetime
from os import path
from os import system

actives = ['tec','exp']
timer   = 600
last    = 0
current = ''
rooms = {
    'rrf':'RRF', 'tec':'TECHNIQUE', 'bav':'BAVARDAGE', 'fon':'FON',
    'exp':'EXPERIMENTAL', 'int':'INTERNATIONAL', 'loc':'LOCAL', 'reg':'REGIONAL',
}

def log(msg):
    print(datetime.now(), '-', msg)

while True:
    try:
        time.sleep(5)
        f = open('/etc/spotnik/network'); network = f.read(); f.close()
        current = rooms[network.strip()]
        #api = f"http://192.168.1.3:8049?room={current}"
        api = f"http://rrf.f5nlg.ovh:8080/RRFTracker/{current}-today/rrf_tiny.json"
        data = requests.get(api).json()
        for room in actives:
            room = rooms[room]
            if not room in data['elsewhere'][1]: continue
            if data['elsewhere'][1][room] == 'Aucune émission': continue
            if time.time() < last: continue
            f = open('/tmp/RRFRaptor_scan.tcl','w')
            f.write('set RRFRaptor "'+room+'"'); f.close()
            last = time.time() + timer
            log("QSO: " + room)
            system('echo 203# > /tmp/dtmf_uhf')    
    except KeyboardInterrupt: exit(0)
    except Exception as err: print(err); continue
                                                                               