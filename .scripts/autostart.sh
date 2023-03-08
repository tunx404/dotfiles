#!/usr/bin/env bash

exmonitor

# picom --experimental-backends &
picom &
nitrogen --restore &
nm-applet &
blueman-applet &
ibus-daemon -drxR
# kdeconnect-indicator &
# /usr/lib/notification-daemon-1.0/notification-daemon &
numlockx &
fusuma &
powerkit &
xss-lock -- /usr/bin/slock &

# i8kmon &
# ulauncher &
# /usr/bin/ulauncher --hide-window --hide-window --hide-window --hide-window --hide-window --hide-window

# sh /home/anhlh33/.scripts/power_saving.sh off
insync start

# Error loading GUI apps
# slack
# teams-for-linux
