# src/dataset_builder.py

import pandas as pd
import os

def build_dataset(qa_pairs, output_path):
    """
    将问答对保存为 CSV 格式的数据集。

    参数：
        qa_pairs (list): 问答对列表。
        output_path (str): 输出 CSV 文件的路径。
    """
    df = pd.DataFrame(qa_pairs)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"数据集已保存到 {output_path}")
