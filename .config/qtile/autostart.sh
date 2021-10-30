#!/usr/bin/env bash
xrandr --output DP-3 --rotate inverted
picom --experimental-backends &
nitrogen --restore &
# volumeicon &
nm-applet &
blueman-applet &
ibus-daemon -drxR
kdeconnect-indicator &
/usr/lib/notification-daemon-1.0/notification-daemon &
# /usr/bin/ulauncher --hide-window --hide-window --hide-window --hide-window --hide-window --hide-window
ulauncher &
numlockx &
fusuma &
# plank &
powerkit &
xss-lock -- /usr/bin/slock &
# xss-lock -- /usr/bin/xscreensaver-command -lock &
