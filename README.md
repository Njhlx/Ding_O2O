# Ding_O2O

* 检查第三方代理库，作业待接收订单
* 待推送订单和当前时间对比：
**无订单：返回打印“很棒”，无报警
**订单未达20分钟，返回打印“忽略”，无报警
**订单达到20分钟，报警订单条数
* 监控轮询：从早上7:50-20:10,20分钟检查一次
