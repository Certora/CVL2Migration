#!/bin/sh

if test -n "$1"
then
    RULE="--rule $1"
fi

certoraRun \
    conf/ERC20.conf \
    $RULE \
    --msg "ERC20 verification $RULE $2" \

