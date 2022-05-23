#!/bin/bash

NAME="qso-alert"


# Installation de git.
if ! hash git || ! hash python3
then
    apt -y update
    apt -y install git python3
fi



if ! test -d /opt/$NAME
then
    git clone https://github.com/AmoniX75/$NAME.git
    mv $NAME /opt
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

echo "Installation terminée !"