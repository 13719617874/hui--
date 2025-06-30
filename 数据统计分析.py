import jieba
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud as wc

# 读取任务一保存的txt文件
input_file = 'poems.txt'

# 读取数据并存储为列表
poems_data = []
with open(input_file, 'r', encoding='gbk') as f:
    for line in f:
        line = line.strip()
        if line:
            poems_data.append(line.split(','))


#


type_counts = {}
for poem in poems_data:
    type_name = poem[0]
    if type_name in type_counts:
        type_counts[type_name] += 1
    else:
        type_counts[type_name] = 1

# 转换为DataFrame格式
df_types = pd.DataFrame(list(type_counts.items()), columns=['诗歌类型', '数量'])

# 保存为Excel文件
excel_file = '诗类型统计.xlsx'
df_types.to_excel(excel_file, index=False)
print(f'诗类型统计已保存到 {excel_file}')
# 统计每个作者的诗数量
author_counts = {}
for poem in poems_data:
    author_name = poem[2]
    if author_name in author_counts:
        author_counts[author_name] += 1
    else:
        author_counts[author_name] = 1

# 转换为DataFrame格式
df_authors = pd.DataFrame(list(author_counts.items()), columns=['作者', '数量'])

# 保存为Excel文件
excel_file = '作者诗数量统计.xlsx'
df_authors.to_excel(excel_file, index=False)
print(f'作者诗数量统计已保存到 {excel_file}')

# 转换为DataFrame
df = pd.DataFrame(poems_data, columns=['诗歌类型', '题目', '作者', '详情'])

# # 中文分词
text = ''.join(jieba.cut('\n'.join(df['详情'])))

# 去掉 \n 和 }
cleaned_text = text.replace('n', '').replace('}', '').replace('\\', '').replace('详情', '').replace(':', ' ').replace("'", "")

# print(cleaned_text)

bg = plt.imread('词云背景图.jpg')
w = wc(background_color='white',
        colormap='winter',
       mask=bg,
       max_words=1500,
       repeat=True,
       font_path='方正卡通简体.ttf')

w.generate_from_text(text)
image = w.to_image().show()
w.to_file('词云图.jpg')

