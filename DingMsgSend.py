import SQLExec
import DingTalkRobot
import ConstSettings
import Common.Const
CONST = Common.Const


def sub_function():
    #将字段客户通道转为两个列表，分别为客户名称、客户CODE
    names = list(ConstSettings.CONST.TONGDAO_CODE.keys())
    codes = list(ConstSettings.CONST.TONGDAO_CODE.values())
    chans = CONST.TONGDAO_CHAINS
    # print(chans)

    # 通道库地址，两个通道库：
    for i in range(0, 2):
        # print(i)
        s_server = CONST.TONGDAO_SERVER[i]
        s_port = CONST.TONGDAO_PORT[i]
        s_database = CONST.TONGDAO_DATABASE[i]
        s_user = CONST.TONGDAO_USER[i]
        s_password = CONST.TONGDAO_PASSWORD[i]
        # print(s_server)

        for name in names:
            # print(name)
            code = ConstSettings.CONST.TONGDAO_CODE[name]
            # print(code)
            row_count = 0

            for chan in chans:
                # print(chan)
                sSQL = 'select * from [dtv5dtchdan' + code + '_' + chan + ']'
                # print(sSQL)
                row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             sSQL)
                # print(row_count)

            #增加判断，待接收数据包大于等于10才提示
            if row_count >= 10 :
                count = row_count
                msg = ''
                msg = "tongd" + str(i) + "_" + msg + name +  ": 业务数据仓库待接收数据包：" + str(count)
                # print(msg)
                DingTalkRobot.send_text(msg)



