# -*- coding: utf-8 -*-
"""
@Project: Git_Study_Project 
@File   : first.py
@IDE    : PyCharm
@Author : Mming
@Time   : 2024/2/27 18:07
@Description: 测试pytorch环境
"""
import numpy as np
import pandas as pd
import torch


print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.is_available())
