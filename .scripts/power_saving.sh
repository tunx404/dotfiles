#!/usr/bin/env bash

echo "Power saving $1!"
if [ $1 == "on" ]
then
	brightnessctl set 50%
	insync quit
elif [ $1 == "off" ]
then
	brightnessctl set 100%
	insync start
fi