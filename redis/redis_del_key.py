import redis
redis_port = ['','']
# redis_port = ['7000','7001','7002']
# redis_delete = [""]
redis_delete = [""]
for i in redis_port:
    r = redis.StrictRedis(host=i, port='6379', db=0)
    # r = redis.StrictRedis(host='10.155.90.164', port=i, db=0)
    for m in  redis_delete:
        tms = r.keys(m)
        if tms == []:
            continue
        else:
            for key_0 in tms:
                print key_0
                try:
                    r.delete(key_0)
                    print "delete complate"
                except Exception,e:
                    print e

