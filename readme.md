# 正方教务系统成绩查询助手
> 作者：AlwaysLazy21

## 使用说明

### 首次使用

- 将 msedgedriver result 两个文件放到统一路径下
- 首次启动后会自动移动 edgedriver 
- 会在 **C:/User/user/** 路径下创建一个 **result** 文件夹
- **result** 存放两个文件 **config.json, msedgedriver** 

### 重复使用

- 默认读取 **config.exe** 获取用户信息进行登录
- 切换账号登录，登录成功后自动覆盖之前的用户信息

### 特别说明

- 该 msedgedriver 默认的版本类型是 windows x64，如果你使用的是其他架构的电脑，请在 [msedgedriver 官网]('https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/')下载对应的文件，并查看下面 msedgedriver 的更新方法
- 碰到浏览器直接闪退，请尝试更新 msedgedriver.exe
- 将最新的 msedgedriver.exe 放到桌面，或者放到程序所在的同个文件夹下，程序启动后会自动更新。

## 原理介绍

- 开发环境：win11、python 3.11、edge、edgedriver
- 通过调用 edgedriver 操作 edge 浏览器模拟人操作