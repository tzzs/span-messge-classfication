import tensorflow as tf
from tensorflow import keras

import numpy as np
import nltk
import nltk.stem
import re
from nltk.tokenize import word_tokenize
import pandas
import csv

label = []
message = []

with open('train.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row[:2] for row in reader]

print(rows)

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

print(label)
print(message)
