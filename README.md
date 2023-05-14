fork [https://github.com/yihong0618/xiaogpt](https://github.com/yihong0618/xiaogpt)

在此基础上增加了语音控制电脑的功能

实现方案：
1. 在要被控制的电脑上部署一个服务，在这个服务中你可以自定义各种控制电脑的能力，然后通过接口暴露出来。 示例项目: [https://gitee.com/dccmmtop/PcCtrl](https://gitee.com/dccmmtop/PcCtrl)
2. 在xiaogpt中增加一个pc控制模块, 当与小爱的对话以“电脑”开头时，用Python调用 步骤1的控制接口。
