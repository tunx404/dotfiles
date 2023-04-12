#!/usr/bin/env bash

xrandr --output DP-1-1 --auto --right-of eDP-1-1 --output HDMI-0 --auto --right-of DP-1-1 --rotate left

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
