#!/usr/bin/env bash

# xrandr --output DP-3 --rotate inverted


xrandr --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal

# xrandr --output DP-2 --mode 1920x1080 --pos 1920x0 --rotate normal
# xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate left

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