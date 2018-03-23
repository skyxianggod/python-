#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
#基本变量
source = ["F:\\ftp"]
target_dir = "F:\\"

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime("%H%M%S")

touch = today_dir + os.sep + time_dir + '.zip'
print(touch)
command_touch = "zip -qr " + touch +' '+ ''.join(source)
print(command_touch)
#逻辑思路判断
# if os.path.exists(today_dir)==0:
#     os.mkdir(today_dir)
# if os.system(command_touch)==0:
#     print('Success backup Up')
# else:
#     print('Failed backup')