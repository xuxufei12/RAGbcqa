# src/preprocessing.py

import nltk
import re

# 下载 punkt 句子分割模型
nltk.download('punkt', quiet=True)

def clean_text(text):
    """
    清洗文本，去除特殊字符和多余的空格。

    参数：
        text (str): 原始文本。

    返回：
        text (str): 清洗后的文本。
    """
    # 去除特殊字符
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # 去除多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def split_sentences(text):
    """
    将文本分割成句子列表。

    参数：
        text (str): 清洗后的文本。

    返回：
        sentences (list): 句子列表。
    """
    sentences = nltk.sent_tokenize(text)
    return sentences

def preprocess_documents(documents):
    """
    对文档列表进行预处理。

    参数：
        documents (list): 原始文档列表。

    返回：
        processed_docs (list): 每个文档对应句子列表的列表。
    """
    processed_docs = []
    for doc in documents:
        clean_doc = clean_text(doc)
        sentences = split_sentences(clean_doc)
        processed_docs.append(sentences)
    return processed_docs
