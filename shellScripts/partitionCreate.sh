#!/bin/sh

export BROKER_FAIL=500
export TOPIC_FAIL=100
export PARTITION_FAIL=300
export MESSAGE_FAIL=400

p=$1
s=$2

a() {
	cd
	cd brokerFS || return $BROKER_FAIL
	cd $p || return $TOPIC_FAIL
	test -f partition1_1.txt || touch partition1_1.txt || return $PARTITION_FAIL
	test -f partition1_2.txt || touch partition1_2.txt || return $PARTITION_FAIL
	test -f partition1_3.txt || touch partition1_3.txt || return $PARTITION_FAIL
	python ~/Desktop/BD_Project/shellScripts/MessageDivide.py $s || return $MESSAGE_FAIL
	echo "Message sent successfully"	
}

a
l=$?

cd ~/Desktop/BD_Project/shellScripts

if [[ $l == $BROKER_FAIL ]]
then
        echo "BROKER ACCESS FAILED"
elif [[ $l == $TOPIC_FAIL ]]
then
        echo "TOPIC ACCESS FAILED"
elif [[ $l == $PARTITION_FAIL ]]
then
        echo "PARTITION CREATION FAILED"
elif [[ $l == $MESSAGE_FAIL ]]
then
        echo "MESSAGE CREATION FAILED"
fi


