#!/bin/sh

export BROKER_FAIL=500
export TOPIC_FAIL=100

p=$1

a() {
        cd
        cd "brokerFS" || return $BROKER_FAIL
        rm -r $p || return $TOPIC_FAIL
        echo "Topic $p deleted successfully."
}

a
l=$?
cd ~/Desktop/BD_Project/shellScripts

if [[ $l == $BROKER_FAIL ]]
then
        echo "BROKER FS DOESN'T EXIST"
elif [[ $l == $TOPIC_FAIL ]]
then
        echo "TOPIC DELETION FAILED"
fi

