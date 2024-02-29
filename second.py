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

"""查询真正的文件路径"""
# 将对应的摘要文件路径更换为论文路径, file为存储摘要文件的路径, file.kdh是存储实际论文的位置
base_url = "http://file.bigmodel.site/"
# 为每个路径生成完整的 URL
full_urls = [urljoin(base_url, path) for path in unique_source_paths]
print(full_urls)
full_urls = full_urls[0]
base_url, file_name_with_extension = full_urls.rsplit('/', 1)
file_name, _ = file_name_with_extension.rsplit('.', 1)
# 假设.kdh文件与.txt文件同名，只是扩展名不同
new_url = f"{base_url}.kdh/{file_name}.kdh"
print(new_url)
# 将路径信息添加到响应中
# response += "\n论文下载地址:\n" + "\n".join(new_url)
response += "\n论文下载地址:" + "".join(new_url)