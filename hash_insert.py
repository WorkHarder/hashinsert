# coding = utf-8
dict = {}
N = 3
conn = []
host = ['223.3.41.18','223.3.39.17','223.3.40.197']
import sys
import string
import HashRing
import MySQLdb
#���ڵ�3��������ڵ�1000��
ring = HashRing.HashRing(host,1000)
#������ÿ��������������
for i in range(0,3):
    try:
        conn_temp=MySQLdb.connect(host=host[i],user='root',passwd='123456',db='weibo',port=3306,charset='utf8')
        conn.append(conn_temp)
    except Exception,e:
        print e
#���ļ�
file = open('user.txt','r')
alllines = file.readlines()
#���в��뵽���ʵ����ݿ���
for eachline in alllines:
    dict = eval(eachline)
    uid = dict['uid']
    server = ring.get_node_pos(uid)
    host_temp = server[0]
    pos = server[1]
    index_temp = host.index(host_temp)
    if conn[index_temp]:
         cursor = conn[index_temp].cursor()
         sql_1 = "CREATE TABLE  IF NOT EXISTS USER%s (uid INT NOT NULL,bi_followers_count INT NOT NULL,PRIMARY KEY(uid)) DEFAULT CHARSET=UTF8"
         value1=[pos]
         cursor.execute(sql_1,value1)
         sql_2="INSERT INTO USER%s VALUES(%s,%s)"
         value2=[pos,uid,dict['bi_followers_count']]
         cursor.execute(sql_2,value2)
         print "one is ok"
#�ر����ݿ�����utfu
for i in range(1,4):
    conn[i].close()
