### 破解验证码初级

#### 验证码分类

+ 图片验证码
  1. 识别图片信息
  2. 点触验证码
  3. 计算题
+ 滑动验证码
  + 滑动轨迹

#### 图片验证码

##### 机器视觉(分支)-->文字识别

+ 光学文字识别 OCR (Optical Character Recognition) : 将图像翻译成文字

##### OCR 库概述 (了解/自学)

+ **Tesseract** : 由 Google 赞助
+ Tesseract 缺点 : 读取硬盘中图片里的文字不是很好,但是对于 网络爬虫使用会很强大

#### Selenium 手动打码

#### 打码平台

##### 简介

+ 验证码打码 : 区别用户是计算机还是人的公共全自动程序
+ 工作原理 : 协助通过 图灵测试

##### 超级鹰平台实例

+ 使用<br>
  1. 注册打码平台
  2. 查看开发文档 --> Python 语言 --> 选择跨平台 HTTP 标准 WEB 接口
  3. 在开发文档中寻找 接口地址、请求方式、参数设置等
  
+ 实例

  ```python
  import time
  from PIL import Image
  from selenium import webdriver
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.wait import WebDriverWait
  import chaojiying
  
  def main():
  	driver = webdriver.Ie()
  	driver.get("https://inv-veri.chinatax.gov.cn/")
  	wait = WebDriverWait(driver, 20)
  	wait.until(EC.presence_of_element_located((By.XPATH, '//tr/td/input[@id="fpdm"]'))).send_keys("041001900111")
  	wait.until(EC.presence_of_element_located((By.XPATH, '//tr/td/input[@id="fphm"]'))).send_keys("46160592")
  	wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kprq"]'))).send_keys("20191225")
  	wait.until(EC.presence_of_element_located((By.XPATH, '//tr/td/input[@id="kjje"]'))).send_keys("678071")
  
  	# selenium操作ie浏览器的click()不起作用，只能使用js点击方式
  	# 点击加载图片验证码
  	# driver.execute_script('document.getElementById("yzm_img").click()')
  	driver.execute_script('document.getElementById("yzm_img").click()')
  	time.sleep(2)
  	# yzm_code = input("请输入验证码:\t")
  	# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yzm"]'))).send_keys(yzm_code)
  	# # 点击查验按钮
  	# driver.execute_script('document.getElementsByClassName("blue_button")[0].click()')
  	yzm_position = driver.find_element_by_xpath('//*[@id="yzm"]')
  	size = yzm_position.size
  	location = yzm_position.location
  	print(location, size)
  	cp_position = (
  		location['x']-15,
  		location['y'],
  		location['x'] + size['width'] + 230,
  		location['y'] + size['height'] + 80
  	)
  	# print(f"验证码四边坐标左上{location['x'], location['y']}\t"
  	#       f"右上{location['x']+size['width'], location['y']}\t"
  	#       f"左下{location['x'], location['y']+size['height']}\t"
  	#       f"右下{location['x']+size['width'], location['y']+size['height']}")
  	driver.save_screenshot("a.png")
  	image = Image.open('a.png')
  	image_pic = image.crop(cp_position)
  	image_pic.save("b.png")
  	c = chaojiying.Chaojiying_Client()
  	im = open("b.png", "rb").read()
  	yzm_code = c.PostPic(im, 5000)['pic_str']
  	print(yzm_code)
  	input("回车继续")
  
  	wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yzm"]'))).send_keys(yzm_code)
  	driver.execute_script('document.getElementsByClassName("blue_button")[0].click()')
  
  if __name__ == '__main__':
  	main()
  ```

  

#### 综合项目 RPA

##### 项目背景

+ RPA (Robitic Process Automation 机器人流程自动化): 是一款软件产品,可以模拟人在电脑上的不同系统之间操作行为,替代人在电脑前执行具有规律且重复性高的办公流程
+ RPA 能有效的优化传统办公流程、提升工作效率,间接优化企业劳动资源配置、助力企业数字化升级
+ RPA 价值
  1. 降低人力资源花费
  2. 解决繁杂的运行和业务逻辑,合理的回应单位专业知识基本建设,解决人员变化的风险性
  3. 让职工从复杂、低价值的劳动中解脱出来,从业高价值、创造力的工作中
  4. RPA 机器人可以二十四小时工作、提升单位服务能力

##### 项目描述

+ RPA 财务机器人可以对收付款、审批、纳税申报、对账等多个环节进行 RPA 作业
+ 该项目主要对发票真伪验证这个子功能的实现,主要对 百度 AI 财务机器人接口实现对发票信息的提取,结合 selenium 进入发票真伪检验的网站对发票真伪验证

##### 技术要点

+ 结合第三方平台对发票内容识别
+ 结合 selenium 进入发票真伪检验的网站对发票真伪验证
+ 打码平台进行发票真伪验证码识别