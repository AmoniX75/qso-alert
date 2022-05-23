#!/bin/bash

DIR=$(dirname $(readlink -f $0))
NAME=$(basename $DIR)


# Installation de git.
if ! hash git || ! hash python3
then
    apt -y update
    apt -y install git python3
fi


git clone https://github.com/AmoniX75/qso-alert.git


if ! test -d /opt/$NAME
then
    mv $DIR /opt
    cd /opt/$NAME
else
    exit 0
fi


if ! test -f /etc/$NAME.conf
then
    cp $NAME.conf /etc
else
    exit 0
fi
