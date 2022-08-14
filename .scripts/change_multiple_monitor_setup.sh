#!/usr/bin/env bash

state=$(cat /tmp/dual_monitor_state)

# if [[ "$state" = 3 ]];
# then
#   echo "Monitor 1";
#   echo "0" > /tmp/dual_monitor_state;
#   xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
#   xrandr --output DP-3  --off;
# elif [[ "$state" = 0 ]];
# then
#   echo "Monitor 2";
#   echo "1" > /tmp/dual_monitor_state;
#   xrandr --output eDP-1 --off;
#   xrandr --output DP-3  --mode 1920x1080 --pos 0x0 --rotate inverted;
# elif [[ "$state" = 1 ]];
# then
#   echo "Extended";
#   echo "2" > /tmp/dual_monitor_state;
#   xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
#   xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate inverted;
# else
#   echo "Mirror";
#   echo "3" > /tmp/dual_monitor_state;
#   xrandr --output DP-3 --same-as eDP-1 --rotate inverted;

# if [[ "$state" = 2 ]];
# then
#   echo "Monitor 1";
#   echo "0" > /tmp/dual_monitor_state;
#   xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
#   xrandr --output DP-3  --off;
# elif [[ "$state" = 0 ]];
# then
#   echo "Extended";
#   echo "1" > /tmp/dual_monitor_state;
#   xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
#   xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate normal;
# else
#   echo "Mirror";
#   echo "2" > /tmp/dual_monitor_state;
#   xrandr --output DP-3 --same-as eDP-1 --rotate normal;
# fi

if [[ "$state" = 3 ]];
then
  echo "All";
  echo "0" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
  xrandr --output DP-2 --mode 1920x1080 --pos 1920x0 --rotate normal;
  xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate left
elif [[ "$state" = 0 ]];
then
  echo "Monitor 1";
  echo "1" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal;
  xrandr --output DP-2  --off;
  xrandr --output DP-3  --off;
elif [[ "$state" = 1 ]];
then
  echo "Monitor 2";
  echo "2" > /tmp/dual_monitor_state;
  xrandr --output eDP-1 --off;
  xrandr --output DP-2 --mode 1920x1080 --pos 1920x0 --rotate normal;
  xrandr --output DP-3  --off;
else
  echo "Mirror";
  echo "3" > /tmp/dual_monitor_state;
  xrandr --output DP-2 --same-as eDP-1 --rotate normal;
  xrandr --output DP-3 --same-as eDP-1 --rotate normal;
  xrandr --output DP-3  --off;
fi
