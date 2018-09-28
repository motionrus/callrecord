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

### How to use

Утилита Dumpcap требует root права, по этому при настройке делаем все от рута. 
клонируем:
```bash
rus@coder:~/$ sudo su
root@coder:~# cd /tmp/
root@coder:/tmp# git clone https://github.com/motionrus/callrecord.git
Клонирование в «callrecord»…
remote: Enumerating objects: 17, done.
remote: Total 17 (delta 0), reused 0 (delta 0), pack-reused 17
Распаковка объектов: 100% (17/17), готово.
root@coder:/tmp# cd callrecord/
root@coder:/tmp/callrecord#
```

Указываем в файле call-record `PATH_CALLRECORD="/tmp/callrecord/"` путь до нашего проекта
Перемещаем файл в инит дирректорию и делаем исполняемым
```bash
root@coder:/tmp/callrecord# cp call-record /etc/init.d/
root@coder:/tmp/callrecord# chmod +x /etc/init.d/call-record 
root@coder:/tmp/callrecord# chmod +x CallRecord.sh compression.py
```
Глобальные переменные файла `CallRecord.sh`
| Variable | README |
| ------ | ------ |
| `COUNT_FILES="4380"` | Количество файлов в дирректории. Параметр `COUNT_FILES` будет ротироваться при переполнении в дирректории файлов |
| `COUNT_SECONDS="3600"` | Количество прошедших секунд после которых будет создан новый файл с новым именем. 4380 * 3600 = полгода. В случае если будет использоваться сжатие данных, эти параметры можно оставить по умолчанию. |
| `CALLRECORD_PATH="/tmp/call_record/call_record.pcapng"` | Путь до файла |
| `CALLRECORD_HOST="portrange 1719-1720 or 1720-1723 or 5060-5063 or 10000-15999 or 16000-19999"` | Для меры указываем range по портам, которые будут использоваться для голоса. Еще можно добавить в фильтр только UDP |
| `CALLRECORD_INTERFACE="enp3s0"` | Указываем интерфейс |

Глобальные переменные `compression.py`
| Variable | README |
| ------ | ------ |
| `FULL_PATH_TO_DIR = '/tmp/call_record'` | Путь до дирректории |
| `EXTENSION_FILE = 'pcapng'` | Расширение файла |

Добавляем в `crontab` примерно следующую строчку `0 * * * * /tmp/callrecord/compression.py > /dev/null 2>&1`
Каждый час мы ищем файлы с расширением pcapng, создаем архив и удаляем те файлы, из которых сделали архив.