from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 读取任务一保存的txt文件
input_file = 'poems.txt'

# 读取数据并存储为列表
poems_data = []
with open(input_file, 'r', encoding='gbk') as f:
    for line in f:
        line = line.strip()
        if line:
            poems_data.append(line.split('\t'))

# 提取诗内容
poems_contents = [poem[0] for poem in poems_data]

# TF-IDF向量化
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(poems_contents)

# 获取特征词列表
feature_names = vectorizer.get_feature_names_out()

# 将TF-IDF结果与原始数据合并
output_data = []
for i, poem in enumerate(poems_data):
    tfidf_values = X[i].toarray().flatten()
    tfidf_string = '\t'.join([str(value) for value in tfidf_values])
    output_data.append(poem + [tfidf_string])

# 保存为txt文件
output_file_tfidf = 'poems_tfidf.txt'
with open(output_file_tfidf, 'w', encoding='utf-8') as f:
    for poem_data in output_data:
        f.write('\t'.join(poem_data) + '\n')
