#!/usr/bin/env bash

if [ $VIRTUAL_ENVIRONMENT ]
then
    deactivate
fi
source .venv/bin/activate    #Linux or MacOS
#. venv/Scripts/activate    #windows
# https://stackoverflow.com/questions/45554864/permission-denied-when-activating-venv
