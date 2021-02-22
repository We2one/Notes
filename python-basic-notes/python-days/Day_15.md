## 坦克大战面向对象设计思路

### 分析

1. #### 导入 pygame 包用于程序主体框架设计与实现
   #### 导入 random 模块用于生成随机三个位置的敌人

2. #### 分析所需要的对象及其行为

    + ##### 我方坦克 (射击、移动、固定出生、移动速度)
    + ##### 敌方坦克 (射击、移动、随机出生、移动速度)
    + ##### 背景类(主题背景，背景上放入障碍物 [草、河流、墙壁] )
    + ##### 子弹(普通子弹、道具强化子弹、子弹弹道、弹速)
    + ##### 障碍物(与地图边缘设置的状况一致)
    + ##### 引擎类(控制游戏的开始结束)
    
### 编写

1. #### 创建公共精灵类，将共同对象放入进行初始化 
    ```
   import pygame
   import random
   
   class GameSprite(pygame.sprite.Sprite):
       
      def __init__(self, images, position=None, speed=None):
           super().__init__()
           if speed is None:
               speed = {"x": 0, "y": 0}
           if position is None:
   		    position = {"x": 0, "y": 0}
	        self.image = images  # 传进来的图片
           self.position = position  # 图片的位置
           self.rect = self.image.get_rect()  # 区域 图像宽度 坐标位置
           self.rect.x = self.position["x"]  # 设置元素的坐标
           self.rect.y = self.position["y"]
           self.speed = speed
   
def move(self):
		pass
	
def event(self):
		pass
	
def stop(self):
		pass
	
def update(self):
		"""我们在去调用分组的update时,会自动执行"""
		self.event()
		self.move()
	```
   
2. #### 创建引擎类，初始化项目的标题信息、坦克数量等、对各种元素进行分组
    + 创建游戏开始与游戏结束标志
    + 加载游戏背景地图
    + 对游戏退出添加事件处理
    + 加载坦克移动时图片移动
    + 创建敌方坦克
   
3. #### 创建坦克父类，对按键添加监听，添加坦克移动时的边界判断

4. #### 创建我方坦克与敌方坦克共同继承坦克父类
    + 为敌方坦克增加随机移动与随机生成
    
5. #### 对图片进行地图编辑，添加地图障碍物元素