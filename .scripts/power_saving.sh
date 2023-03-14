#!/usr/bin/env bash

echo "Power saving $1!"
if [ $1 == "on" ]
then
	brightnessctl set 30%
	# balooctl suspend
	# balooctl disable
	insync quit
elif [ $1 == "off" ]
then
	brightnessctl set 50%
	# balooctl resume
	# balooctl enable
	insync start
fi