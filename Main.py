import csv
import re
from itertools import chain

label = []
message = []

with open('train.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row[:2] for row in reader]

# print(rows)

for row in rows[1:]:
    if row[0] == 'ham':  # 非垃圾短信
        label.append(0)
    elif row[0] == 'spam':  # 垃圾短信
        label.append(1)
    else:
        label.append(-1)
        print(row)
    text = re.sub(r'[^a-z ]', '', row[1].lower())
    message.append(text)

# print('label\n', label)
# print('message\n', message)

docs = [m.split() for m in message]

# 生成词表
words = list(set(chain(*docs)))  # 加*是将列表拆分为两个参数
print(words)
