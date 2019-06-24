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
    if row[0] == 'ham':
        label.append(0)
    elif row[0] == 'spam':
        label.append(1)
    else:
        label.append(-1)
        print(row)
    message.append(row[1].lower())

print(label)
print(message)
