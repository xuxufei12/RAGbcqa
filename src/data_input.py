# src/data_input.py

import os

def load_seed_documents(directory_path):
    """
    从指定目录加载所有种子文档。

    参数：
        directory_path (str): 种子文档所在的目录路径。

    返回：
        documents (list): 文本字符串列表，每个元素对应一个文档的内容。
    """
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt') or filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append(content)
    return documents
