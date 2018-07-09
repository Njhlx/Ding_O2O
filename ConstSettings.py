import Common.Const
CONST = Common.Const


# 配置值（手工输入）
def define():
    # 钉钉机器人地址
    CONST.DINGTALK_ROBOT = "https://oapi.dingtalk.com/robot/send?access_token=" \
                           "801fbba15f1b0559be1c81de38ae4ba2290549a67004cd590cffd9e87c45605e"
    #通道库地址
    CONST.TONGDAO_SERVER = ['szbj1dat.sqlserver.rds.aliyuncs.com','njsz1dat.sqlserver.rds.aliyuncs.com']
    CONST.TONGDAO_PORT = ['3433', '3433']
    CONST.TONGDAO_DATABASE = ['szbj02data','njsz02data']
    CONST.TONGDAO_USER = ['szbj02data','njsz02data']
    CONST.TONGDAO_PASSWORD = ['szbj02_8289986','njsz02_8289986']

    #客户名称+客户通道授权码
    CONST.TONGDAO_CODE = {'郑州金麦':'20170728zzjm','合肥超港':'z9cggs20171124','淮安金鸡':'z9hajj20180418','长沙多喜来':'z9csdxl20171127','巩义花儿':'z9gyhe20180504','宁德艾宁檬':'z9ndanm20171222','南宁一品轩':'z9nnypx20180116','无锡咔芙美':'z9wxkfm20180518','广州绿叶居':'z9gzlyj20180626'}
    #信道
    CONST.TONGDAO_CHAINS = ['ywdata-801huiz','ywdata-801kuc','ywdata-801caiw','ywdata-801dd','ywdata-801dhk','ywdata-801hsq','ywdata-801mdkd','ywdata-801mdxs','ywdata-801trfv3','ywdata-801wul','ywdata-801zaixzhh']

