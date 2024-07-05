#!/bin/bash

# compile home
cd ./jemdoc
python2.7 ../jemdoc.py -c jemdoc.conf -o ../index.html index.jemdoc
cd -

# compile readings
cd ./jemdoc
python2.7 ../jemdoc.py -c jemdoc.conf -addmd ../posts/reading-list.md -o ../readings.html readings.jemdoc
cd -