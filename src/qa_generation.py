# src/qa_generation.py

import openai

# 请确保已设置 OPENAI_API_KEY 环境变量，或者在此处直接设置 API 密钥
# openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_qa_pair(sentence):
    """
    利用 GPT-4 为给定的句子生成一个问答对。

    参数：
        sentence (str): 输入的句子。

    返回：
        qa_pair (dict): 包含 'question' 和 'answer' 的字典。
    """
    prompt = f"根据以下句子生成一个相关的、有深度的乳腺癌领域问题，并给出详细的答案：\n\n{sentence}"
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content'].strip()
        # 假设答案中包含问答对，解析之
        question, answer = parse_qa(answer)
        return {'question': question, 'answer': answer}
    except Exception as e:
        print(f"Error generating QA pair: {e}")
        return None

def parse_qa(text):
    """
    从 GPT-4 的响应中解析出问答对。

    参数：
        text (str): GPT-4 的响应文本。

    返回：
        question (str): 解析出的问题。
        answer (str): 解析出的答案。
    """
    # 简单的解析逻辑，实际情况可能需要更复杂的处理
    parts = text.split('\n', 1)
    question = parts[0].replace('问题：', '').strip()
    answer = parts[1].replace('答案：', '').strip() if len(parts) > 1 else ''
    return question, answer

def generate_qa_pairs(sentences):
    """
    为一组句子生成问答对。

    参数：
        sentences (list): 句子列表。

    返回：
        qa_pairs (list): 问答对列表。
    """
    qa_pairs = []
    for sentence in sentences:
        qa_pair = generate_qa_pair(sentence)
        if qa_pair:
            qa_pairs.append(qa_pair)
    return qa_pairs
