#!/bin/bash

#redis_comm=/usr/bin/redis-cli
#redis_ser=172.31.0.58
#port_1=7000
#port_2=7001
#port_3=7002
#$redis_comm -c -h $redis_ser -p $port_1  keys $1 | xargs -i ./redis-cli -h $redis_ser -p $port_1 del {}
#$redis_comm -c -h $redis_ser -p $port_2  keys $1 | xargs -i ./redis-cli -h $redis_ser -p $port_2 del {}
#$redis_comm -c -h $redis_ser -p $port_3  keys $1 | xargs -i ./redis-cli -h $redis_ser -p $port_3 del {}




redis_host=
redis_ports=()
redis_keys_input=("")

echo > ./keys.txt
for port in ${redis_ports[@]}
#Afferent parameters 
#do
# redis-cli -h $redis_host -p $port keys $1 >> ./keys.txt
#done

#use redis_keys_input
do 
echo "get keys"
for keys in ${redis_keys_input[@]}
 do 
  redis-cli -h $redis_host -p $port keys $keys >> ./keys.txt
  grep -v "^$" ./keys.txt >> ./keys_1.txt
 done
done

for line in $(cat ./keys_1.txt)
 do
  echo "begin delete $line"
  for port in ${redis_ports[@]}
  do
   redis-cli -c -h $redis_host -p $port del $line
  done
done
