# src/evaluation.py

def evaluate_dataset(qa_pairs):
    """
    对生成的问答对进行简单的质量评估。

    参数：
        qa_pairs (list): 问答对列表。

    返回：
        metrics (dict): 评估指标字典。
    """
    total = len(qa_pairs)
    valid = sum(1 for qa in qa_pairs if qa['question'] and qa['answer'])
    quality = valid / total if total > 0 else 0
    metrics = {
        'total_pairs': total,
        'valid_pairs': valid,
        'quality': quality
    }
    print(f"评估结果：总数 {total}，有效问答对 {valid}，质量得分 {quality:.2f}")
    return metrics
