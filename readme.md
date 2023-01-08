# 正方教务系统成绩查询助手
> 作者：AlwaysLazy21   
> 适配的教务系统版本：版权所有© Copyright 1999-2022 正方软件股份有限公司　　中国·杭州西湖区紫霞街176号 互联网创新创业园2号301   版本V-8.0.0

## 使用说明

### 注：仓库地址：https://github.com/AlwaysLazy21/zhengfang-result ，你在使用过程中如果有任何的问题，欢迎提出issue

### 首次使用

- 将 msedgedriver result 两个文件放到统一路径下
- 启动后会自动移动**msedgedriver**
- 会在 **C:/User/user/** 路径下创建一个 **result** 文件夹
- **result** 存放两个文件 **config.json, msedgedriver.exe** 

### 重复使用

- 每次启动前会自动检测**同级文件夹**和**桌面**是否存在**msedgedrive.exe**,并移动到目标位置，以便用户更新**msedgedriver.exe**
- 默认读取 **config.json** 获取用户信息进行登录
- 切换账号登录，登录成功后自动覆盖之前的用户信息

### 特别说明

- 该 msedgedriver 默认的版本类型是 windows x64，如果你使用的是其他架构的电脑，请在 [msedgedriver 官网](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)下载对应的文件，并查看下面 msedgedriver 的更新方法
- 碰到浏览器直接闪退，请尝试更新 msedgedriver.exe
- 将最新的 msedgedriver.exe 放到桌面，或者放到result程序所在的同个文件夹下，程序启动后会自动更新。

## 原理介绍

- 开发环境：win11、python 3.11、edge、msedgedriver
- 通过调用 edgedriver 操作 edge 浏览器模拟人操作
