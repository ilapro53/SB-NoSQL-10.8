
## SB. NoSQL. 10.8 Практическая работа

### Решение ошибки hdfs "Connection refused" в Яндекс Облаке

> :warning: **После выполнения команд по ssh можно подключится только после перезапуска сервера**. Также ssh может отключиться через некоторое время. Также в яндекс облаке могут возникать ошибки. Если возникла ошибка, остановите сервер, если ошибка не исчезнет -- подождать несколько минут и проверить сайт снова.

Решение. Выполнить команды:
```sh
ssh -i <путь_до_ssh_ключа> admin@<ip_сервера>
docker stop $(docker ps -a -q)
sudo systemctl stop ssh.service
docker start <id_контейнера>
```

Прмер выполнения:
```sh
> ssh -i <путь_до_ssh_ключа> admin@<ip_сервера>
admin@vm1:~$ docker stop $(docker ps -a -q)
<id_контейнера>
admin@vm1:~$ sudo systemctl stop ssh.service
admin@vm1:~$ docker start <id_контейнера>
<id_контейнера>
admin@vm1:~$ 
```
