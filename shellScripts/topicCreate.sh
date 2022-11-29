#!/bin/sh

export BROKER_FAIL=500
export TOPIC_FAIL=100

p=$1

a() {
	cd	
	mkdir "brokerFS" && cd "$_" || return $BROKER_FAIL
	mkdir $p && cd "$_" || return $TOPIC_FAIL 
	echo "Topic $p created successfully."
}

a

if [[ $a == $BROKER_FAIL ]] 
then
	echo "BROKER FS CREATION FAILED"
elif [[ $a == $TOPIC_FAIL ]]
then
	echo "TOPIC CREATION FAILED"
fi
