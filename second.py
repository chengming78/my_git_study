# -*- coding: utf-8 -*-
"""
@Project: Git_Study_Project 
@File   : second.py
@IDE    : PyCharm
@Author : Mming
@Time   : 2024/2/29 15:20
@Description: 论文检索
"""

qa_result = qa({"query": message})
# print(qa_result)
response = qa_result['result']

# 获取相关文档的路径
source_documents = qa_result.get('source_documents', [])
# print(source_documents)
# 假设文档字典中有路径信息
source_paths = [doc.metadata['source'] for doc in source_documents if 'source' in doc.metadata]
print(source_paths)
# 使用set去重路径
unique_source_paths = list(set(source_paths))