#!/bin/bash

killall conky

sleep 10

conky -c ~/.conky/conkyleft &
conky -c ~/.conky/conkyright ;
exit 0
