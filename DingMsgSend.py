import SQLExec
import DingTalkRobot
import ConstSettings
import Common.Const
CONST = Common.Const
import datetime
import time


def sub_function():
    #第三方代理库地址（正式环境）
    s_server = '39.108.58.237'
    s_port = '1433'
    s_database = 'TpO2OProxyConfigDB'
    s_user = 'sa'
    s_password = 'Zl84519741'
    # 第三方代理库地址（测试环境）
    # s_server = '123.57.226.114'
    # s_port = '2433'
    # s_database = '20171012FBProxy'
    # s_user = 'sa'
    # s_password = '84519741'

    sSQL = "select  datediff( MINUTE,min(a.updatetime),GETDATE()) from pushmessagecache a inner join zlapptpappconfigmapping b on a.tpapptype = b.tpapptype and a.tpappauthkey = b.tpappauthkey where b.zlusercode = '105'"
    # print(sSQL)
    #订单时间
    row_count = SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             sSQL)
    # print(row_count)
    count = row_count[0]
    # print(count)

    #订单条数
    sSQL1 = "select count(*) from pushmessagecache a inner join zlapptpappconfigmapping b on a.tpapptype = b.tpapptype and a.tpappauthkey = b.tpappauthkey where b.zlusercode = '105'"
    row_count1 = SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             sSQL1)
    # print(row_count1)
    count1 = row_count1[0]
    # print("24小时格式：" + time.strftime("%H:%M"))
    if count == None:
        print("很棒，没问题")
    elif count > 20 :
        msg = ''
        msg = "长沙多喜来" + msg + ": 存在20分钟前订单未推送；待推送订单条数：" + str(count1)
        print(msg)
        # # DingTalkRobot.send_text(msg)
    else :
        print("订单未达20分钟，忽略")







