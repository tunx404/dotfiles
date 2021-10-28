#!/usr/bin/env bash
xrandr --output DP-3 --rotate inverted
picom &
nitrogen --restore &
# volumeicon &
nm-applet &
blueman-applet &
ibus-daemon -drxR
kdeconnect-indicator &
/usr/lib/notification-daemon-1.0/notification-daemon &
ulauncher &