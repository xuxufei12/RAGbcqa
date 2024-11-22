# RAGbcqa

**RAGbcqa** 是一个能够快速生成乳腺癌场景的 RAG 评估数据集的通用框架，专为科研人员设计，通过结合 GPT-4 等大语言模型，能够根据用户给定的若干种子文档（乳腺癌医学论文，治疗手册等），生成问题、答案和参考文献作为评估样本。

## 项目结构

\`\`\`
RAGbcqa/
├── data/
│   ├── seed_documents/
│   └── output_dataset/
├── src/
│   ├── data_input.py
│   ├── preprocessing.py
│   ├── qa_generation.py
│   ├── reference_generation.py
│   ├── dataset_builder.py
│   ├── evaluation.py
│   └── main.py
├── requirements.txt
└── README.md
\`\`\`

## 安装与使用

1. **克隆或下载项目**

   \`\`\`bash
   git clone https://github.com/yourusername/RAGbcqa.git
   cd RAGbcqa
   \`\`\`

2. **安装依赖**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **设置 OpenAI API 密钥**

   请确保已设置 \`OPENAI_API_KEY\` 环境变量，或者在 \`src/qa_generation.py\` 中直接设置 API 密钥。

4. **添加种子文档**

   将您的乳腺癌相关种子文档（如医学论文、治疗手册等）添加到 \`data/seed_documents/\` 目录下。

5. **运行主程序**

   \`\`\`bash
   python src/main.py
   \`\`\`

   生成的评估数据集将保存在 \`data/output_dataset/\` 目录下。

## 贡献

欢迎提出问题、建议或提交 Pull Request。

## 许可证

请在此处添加许可证信息。
