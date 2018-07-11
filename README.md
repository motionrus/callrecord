# CallRecord

Record conversations using the dumpcap program
for work it is necessary to have the installed program dumpcap which is a part of the program wireshark-common

### Files

 - CallRecord.sh contain the start command. For work you need to run this file as a process
 - wrapper.sh root wrapper
 - call-record init process


### Installation

for work you need to place the call-record file in the /etc/init.d/ directory and make it executable. Add the file to startup and change the path to the executable script.

### Roadmap

 - (-) It is necessary to implement a daemon that will monitor the child process and restart each time the process drops
 - (-) Collect logs
 - (+) Archive Dumps