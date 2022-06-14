#!/usr/bin/env bash

xrandr --output DP-3 --rotate inverted
picom --experimental-backends &
nitrogen --restore &
nm-applet &
blueman-applet &
ibus-daemon -drxR
kdeconnect-indicator &
/usr/lib/notification-daemon-1.0/notification-daemon &
# /usr/bin/ulauncher --hide-window --hide-window --hide-window --hide-window --hide-window --hide-window
ulauncher &
numlockx &
fusuma &
powerkit &
xss-lock -- /usr/bin/slock &
# optimus-manager-qt &
i8kmon &

sh /home/tunx404/.scripts/power_saving.sh off