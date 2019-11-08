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
def hash(redis_obj, key):
    return redis_obj.hgetall(key)


'''

class GetMethod(object):
    def list(self,redis_obj,key):
        return redis_obj.lrange(key,0,-1)
    def zset(self,redis_obj,key):
        return redis_obj.zrange(key, 0, -1)
    def string(self,redis_obj,key):
        return redis_obj.get(key)
'''
'''
redis_port = [7000,7001,7002,7003,7004,7005]
for i in redis_port:
    r = redis.StrictRedis(host='', port=i, db=0)
    result = r.keys("")
'''

# redis_port = ['']  #test
redis_port = ['']  #beta
for i in redis_port:
    # r = redis.StrictRedis(host=i, port='', db=0)
    r = redis.StrictRedis(host='', port=i, db=0)
    # result = r.keys("")
    result = r.keys("")
    for key_0 in result:
        print "%s\t%s"%(i,key_0)  #获取redis地址和key
        try:
            count = 0
            type_key = r.type(key_0)
            '''
            if type_key == "hash":
                values = r.hgetall(key_0)
                print values
                fields = r.hkeys(key_0)
                for field in fields:
                    values = r.hget(key_0,field)
                    print values
                '''
            cur_obj = sys.modules[__name__]
            values = getattr(cur_obj,type_key)(r,key_0)
            if type_key == "string" or type_key == "hash":
                print values
            #m = GetMethod()
            #values = getattr(m,type_key)(r,key_0)
            else:
                for value in values:
                    print value  #获取value
                    count += 1
            print count
        except:
            pass




'''
redis_port = [7000,7001,7002,7003,7004,7005]
for i in redis_port:
    r = redis.StrictRedis(host='172.31.0.58', port=i, db=0)
    result = r.keys("")
    for key_0 in result:
        print "%s\t%s"%(i,key_0)  #获取redis地址和key
        try:
            count = 0
            type_key = r.type(key_0)
            if type_key == "string":
                values = r.get(key_0)
                print values
            if type_key == "list":
                values = r.lrange(key_0,0,-1)
                for value in values:
                    print value  #获取value
                    count += 1
                print count
            if type_key == "set":
                values = r.smembers(key_0)
                for value in values:
                    print value  #获取value
                    count += 1
                print count
            if type_key == "zset":
                values = r.zrange(key_0,0,-1)
                for value in values:
                    print value  #获取value
                    count += 1
                print count
            if type_key == "hash":
                values = r.hget(hash1,key_0)
                for value in values:
                    print value  #获取value
                    count += 1
                print count
        except:
            pass
'''
