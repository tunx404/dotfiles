#!/usr/bin/env bash

exmonitor2k

picom &
nitrogen --restore &
nm-applet &
blueman-applet &
ibus-daemon -drxR
# kdeconnect-indicator &
numlockx &
fusuma &
powerkit &
xss-lock -- /usr/bin/slock &

# sh /home/anhlh33/.scripts/power_saving.sh off
insync start

# Error loading GUI apps
# slack
# teams-for-linux
