# -*- coding:utf-8 -*-

# Name:          test
# Description:
# Author:        jianbo.jia
# Date:          2022/1/13 11:10
# 1642046887.168921
import time

timeStamp = 1642046887.168921
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)