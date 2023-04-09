#!/usr/bin/env bash

xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
xrandr --output DP-1 --mode 1920x1080 --pos 1920x0 --rotate normal;
# xrandr --output DP-2  --mode 1920x1080 --pos 1920x840 --rotate normal;
# xrandr --output DP-3  --mode 1920x1080 --pos 3840x0   --rotate left

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
ulauncher &
# /usr/bin/ulauncher --hide-window --hide-window --hide-window --hide-window --hide-window --hide-window

sh /home/tunx404/.scripts/power_saving.sh off