#!/bin/sh

export BROKER_FAIL=500
export TOPIC_FAIL=100

p=$1

a() {
	cd	
	mkdir -p "brokerFS" && cd "$_" || return $BROKER_FAIL
	mkdir -p $p && cd "$_" || return $TOPIC_FAIL 
	echo "Topic $p created successfully."
}

a
l=$?

cd ~/Desktop/BD_Project/shellScripts

if [[ $l == $BROKER_FAIL ]] 
then
	echo "BROKER FS CREATION FAILED"
elif [[ $l == $TOPIC_FAIL ]]
then
	echo "TOPIC CREATION FAILED"
fi
