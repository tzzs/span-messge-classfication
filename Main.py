import tensorflow as tf
from tensorflow import keras

import numpy as np

label = []
message = []

with open('train.csv', encoding='utf-8') as f:
    data = f.readlines()[1:]

print(data)

for d in data:
    d = d.split(',', 1)

    label.append(d[0])
    message.append(d[1])

print(label)
print(message)
