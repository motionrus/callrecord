#!/bin/bash
#
# Created by Ruslan Tyutin
# 
# Count Hours in year/2 is (365/2)*24 = 4380 hours
# COUNT_FILES="4380"
# COUNT_SECONDS="3600"
# if CallRecord (dumpcap) is not running, then start the process


COUNT_FILES="4380"
COUNT_SECONDS="3600"
CALLRECORD_PATH="/tmp/call_record/call_record.pcapng"
CALLRECORD_HOST="port 1719|5061"
CALLRECORD_INTERFACE="enp3s0"

let count_running_procces=$(ps aux | grep call_record | awk ' { print $2 } ' | wc -l)-1

if [[ "$count_running_procces" == 0 ]]; then
	/usr/bin/dumpcap -q -i ${CALLRECORD_INTERFACE} 	-b duration:${COUNT_SECONDS} \
													-b files:${COUNT_SECONDS} \
													-w $CALLRECORD_PATH \
													-f "${CALLRECORD_HOST}" call_record=true &
else
	echo "process already running"
fi

