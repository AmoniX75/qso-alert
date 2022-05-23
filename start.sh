#!/bin/bash

nohup $(pwd)/main.py > /var/log/qso-alert.log 2>&1 &