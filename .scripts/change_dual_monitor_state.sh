#!/usr/bin/env bash

state=$(cat /tmp/dual_monitor_state)

if [[ "$state" = 2 ]];
then
  echo "Monitor 1";
  echo "0" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
  xrandr --output DP-3  --off;

elif [[ "$state" = 0 ]];
then
  echo "Monitor 2";
  echo "1" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --off;
  xrandr --output DP-3  --mode 1920x1080 --pos 0x0 --rotate inverted;

else
  echo "Extended";
  echo "2" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
  xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate inverted;
fi