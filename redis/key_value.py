# -*- coding:utf-8 -*-
import redis
import traceback
import sys


def list(redis_obj, key):
    return redis_obj.lrange(key, 0, -1)
def zset(redis_obj, key):
    return redis_obj.zrange(key, 0, -1)
def string(redis_obj, key):
    return redis_obj.get(key)

#test
#redis_host = []
#beta
redis_host = []
for i in redis_host:
    r = redis.StrictRedis(host='', port=i, db=0)
    result = r.keys("TMS:TRACKINGNO:NAQEL")
    for key_0 in result:
        print "%s\t%s"%(i,key_0)  #获取redis地址和key
        try:
            count = 0
            type_key = r.type(key_0)
            if type_key == "hash":
                fields = r.hkeys(key_0)
                for field in fields:
                    values = r.hget(key_0,field)
                    print values
            cur_obj = sys.modules[__name__]
            values = getattr(cur_obj,type_key)(r,key_0)
            if type_key == "string":
                print values
            else:
                for value in values:
                    print value  #获取value
                    count += 1
            print count
        except:
            pass
