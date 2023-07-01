#!/usr/bin/env bash

xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --auto --right-of eDP-1
xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1-0 --auto --right-of eDP-1

picom --experimental-backends &
nitrogen --restore &
nm-applet &
blueman-applet &
ibus-daemon -drxR
kdeconnect-indicator &
/usr/lib/notification-daemon-1.0/notification-daemon &
numlockx &
fusuma &
powerkit &
xss-lock -- /usr/bin/slock &
i8kmon &

sh /home/tunx404/.scripts/power_saving.sh off