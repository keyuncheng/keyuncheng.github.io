#!/bin/bash

# compile home
cd ./jemdoc
python ../jemdoc.py -c jemdoc.conf -o ../index.html index.jemdoc
cd -

# compile readings
cd ./jemdoc
python ../markdown.py
cd -