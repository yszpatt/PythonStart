# coding:utf-8
import tensorflow as tf
import numpy as np


with tf.Session():
    input1 = tf.constant([[12, 7, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

    input2 = tf.constant([[5, 8, 1],
                          [6, 7, 3],
                          [4, 5, 9]])
    output = tf.add(input1, input2)
    result = output.eval()
    print(result)

# Z = np.zeros(shape=(len(X), len(X[0])))

# for i in range(0, len(X)):
#     for j in range(0, len(X[0])):
#         Z[i][j] = X[i][j] + Y[i][j]


# print()
