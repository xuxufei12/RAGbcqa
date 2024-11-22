# src/main.py

from data_input import load_seed_documents
from preprocessing import preprocess_documents
from qa_generation import generate_qa_pairs
from reference_generation import add_references
from dataset_builder import build_dataset
from evaluation import evaluate_dataset

def main():
    # 1. 加载种子文档
    print("加载种子文档...")
    documents = load_seed_documents('data/seed_documents')

    # 2. 预处理
    print("预处理文档...")
    processed_docs = preprocess_documents(documents)

    # 3. 问答生成
    print("生成问答对...")
    all_qa_pairs = []
    for sentences in processed_docs:
        qa_pairs = generate_qa_pairs(sentences)
        all_qa_pairs.extend(qa_pairs)

    # 4. 生成参考文献
    print("添加参考文献...")
    all_qa_pairs = add_references(all_qa_pairs, documents)

    # 5. 构建数据集
    print("构建数据集...")
    build_dataset(all_qa_pairs, 'data/output_dataset/ragbcqa_dataset.csv')

    # 6. 评估数据集
    print("评估数据集...")
    evaluate_dataset(all_qa_pairs)

if __name__ == '__main__':
    main()
