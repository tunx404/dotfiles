#!/usr/bin/env bash

echo "Power saving $1!"
if [ $1 == "on" ]
then
	brightnessctl set 50%
	balooctl suspend
	balooctl disable
	insync quit
elif [ $1 == "off" ]
then
	brightnessctl set 70%
	balooctl resume
	balooctl enable
	# balooctl suspend
	# balooctl disable
	insync start
fi