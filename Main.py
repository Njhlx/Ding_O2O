import time
import datetime

import DingMsgSend
import  decimal
import ConstSettings
import Common.Const
CONST = Common.Const


def main():
    print("Begin")
    ConstSettings.define()
    counter = 0
    #获取当前时分
    t = time.strftime("%H:%M")
    # print(t)
    #开始执行时间
    a = '07:50'
    #结束执行时间
    b = '20:10'
    while a < t < b:
        DingMsgSend.sub_function()
        counter = counter + 1
        i = datetime.datetime.now()
        print(str(i) + " " + str(counter))
        #间隔查询时间，秒
        time.sleep(1200)
        t = time.strftime("%H:%M")
    else:
        print("该时段无需执行")

    print("End")


if __name__ == "__main__":
    main()
