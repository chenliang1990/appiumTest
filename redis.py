import redis
# python连接redis并读取里面的token
conn = redis.Redis(host='192.168.132.136', port=6379,password='cl2188218')

p1 = conn.keys()
for i in p1:
    a = eval(conn.get(i))
    print(a['userinfo']['token'])
 
    

