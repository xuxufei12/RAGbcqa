# src/reference_generation.py

def generate_reference(question, answer, source_texts):
    """
    为给定的问答对生成参考文献。

    参数：
        question (str): 问题文本。
        answer (str): 答案文本。
        source_texts (list): 原始文档的文本列表。

    返回：
        reference (str): 参考文献字符串。
    """
    # 简单匹配答案中的关键词以寻找相关文献，这里仅为示例
    for text in source_texts:
        if answer[:50] in text:
            # 假设文档有标题或其他可用作参考的信息
            return "参考文献：原始文档标题或其他信息"
    return "参考文献：无匹配"

def add_references(qa_pairs, source_texts):
    """
    为问答对列表添加参考文献。

    参数：
        qa_pairs (list): 问答对列表。
        source_texts (list): 原始文档的文本列表。

    返回：
        qa_pairs_with_refs (list): 包含参考文献的问答对列表。
    """
    for qa in qa_pairs:
        reference = generate_reference(qa['question'], qa['answer'], source_texts)
        qa['reference'] = reference
    return qa_pairs
