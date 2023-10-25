# auto-labsafe-exam 
本程序用于自动完成湖大实验室安全考试答题  
推荐在虚拟环境中运行本程序  
## 环境配置  
1. 确保安装Google Chrome浏览器和对应版本的驱动  
   [谷歌浏览器下载](https://www.google.com/intl/zh-CN/chrome/)  
   [谷歌浏览器驱动下载(请下载对应大版本)](https://googlechromelabs.github.io/chrome-for-testing/)  
   完成后，请将谷歌浏览器驱动放置到您电脑上Chrome的安装目录下
   [安装教程](https://www.cnblogs.com/lfri/p/10542797.html)
2. 所需Python库
   在电脑终端依次输入  
  * selenium `pip install selenium`
  * lxml `pip install lxml`

## 使用方法
1. 下载本项目的压缩包并解压在合适位置
2. 在您的IDE中运行**main.py**,您应当会被要求输入信息
 ![输入示意图](https://github.com/JesterHey/img_file/blob/main/%E6%88%AA%E5%B1%8F2023-10-25%2016.46.18.png)
   
4. 完成后，您只需稍作等待，在程序执行到最后一页时，您就可以提交试卷了
## 演示视频  

https://github.com/JesterHey/auto-labsafe-exam/assets/144512889/1f0f81f0-fdc7-4c27-a26f-7e22bde012aa

## 注意事项  
1. 尽管经过多次提取，本项目的题库仍然有部分缺陷，不能保证每次执行都在85分以上，但经过统计，在5次内就可通过考试的概率接近99%
2. 使用本程序即代表您愿意承担使用此程序带来的相应后果

## 致谢  
本程序的答案点击部分受到[HunterJ-Lin](https://github.com/HunterJ-Lin/AutoAnswer2XMU)的项目启发。
