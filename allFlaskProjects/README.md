# 这是一个基于 Flask 框架的项目“爱家租房网站（移动端）”

爱家租房项目采用前后端分离的模式开发.后端返回的结果都是json格式.

实现的功能如下：
1. 图片验证码
2. 短信验证码
3. 注册、登陆、退出
4. 个人中心显示
5. 修改用户名
6. 上传、修改头像
7. 实名认证
8. 后端加载城市信息
9. 主页显示用户信息与房源图片、搜索
10. 房屋详情页
11. 预定房源
12. 发布房源 
13. 我的订单、客户订单
14. 接单、拒单
15. 支付（支付宝）
16. 订单评价

以下1-15是开发过程中的每个版本,其中都有对应的博客解说,博客地址：https://blog.csdn.net/geek_xiong/article/details/100108834

### 项目开发说明：
1. 整体是在ubuntu18.04上开发完成
2. python版本为3.7
3. mysql
4. redis
5. 图片上传到七牛服务器
6. 短信采用的是容联云（云通讯）

### 安装说明
在用pip安装一些工具时可能会出错,这里建议先安装conda,然后使用conda安装,博客地址（或自行百度）：https://www.jianshu.com/p/edaa744ea47d

### 安装依赖包requirements.txt
> pip install -r requirements.txt
