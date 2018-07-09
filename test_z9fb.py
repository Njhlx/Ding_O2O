import pymssql

# server 数据库服务器名称或IP
# user 用户名
# password 密码
# database 数据库名称

#数据库连接
conn = pymssql.connect(host='192.168.10.202',user='sa',password='',database='z9tongd0')

#打开游标
cur = conn.cursor()

if not cur:
  raise Exception('数据库连接失败！')

#查询操作

#查询语句
# sSQL = 'select * from [dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801huiz]'
sSQL = 'select * from [dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801huiz];select * from [dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801kuc];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801caiw];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801dd];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801dhk];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801hsq];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801mdkd];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801mdxs];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801trfv3];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801wul];select * from[dbo].[dtv5dtchdanz9njzlkj20180205cs_ywdata-801zaixzhh]'

#执行
cur.execute(sSQL)
result=cur.fetchall()

#result是list，而其中的每个元素是 tuple
print(type(result),type(result[0]))

#打印总行数
print('\n\n总行数：'+ str(cur.rowcount))

#通过enumerate返回行号，打印每行
# for i,(id,name,v) in enumerate(result):
#   print('第 '+str(i+1)+' 行记录->>> '+ str(id) +':'+ name+ ':' + str(v) )

# #修改数据
# cur.execute("insert into tb(id,name,score) values(2,'物理',88)")
# cur.execute("update tb set score=95 where id=7")
# conn.commit() #修改数据后提交事务
# #再查一次
# cur.execute(sSQL)
# #一次取一条数据,cur.rowcount为-1
# r=cur.fetchone()
# i=1
# print('\n')
# while r:
#   id,name,v =r #r是一个元祖
#   print('第 '+str(i)+' 行记录->>> '+ str(id) +':'+ name+ ':' + str(v) )
#   r=cur.fetchone()
#   i+= 1
conn.close()