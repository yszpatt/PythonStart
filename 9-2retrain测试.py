#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import os
import numpy as np
# import re
from PIL import Image
import matplotlib.pyplot as plt

lines = tf.gfile.GFile(
    '/Users/shenzheng/retrain/output_labels.txt').readlines()
uid_to_human = {}

for uid, line in enumerate(lines):
    line = line.strip('\n')
    uid_to_human[uid] = line
print(uid_to_human)


def id_to_string(node_id):
    if node_id not in uid_to_human:
        return ''
    return uid_to_human[node_id]


with tf.gfile.FastGFile('/Users/shenzheng/retrain/output_graph.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    # 遍历图片
    for (root, dirs, files) in os.walk('/Users/shenzheng/image/'):
        for file in files:
            if not file.endswith(('.jpeg', '.gif', '.jpg', '.png')):
                continue
            # 载入图片
            image_data = tf.gfile.FastGFile(
                os.path.join(root, file), 'rb').read()
            print(file)
            predictions = sess.run(
                softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是jpg

            predictions = np.squeeze(predictions)  # 结果转为1维数据

            # 打印图片路径及名称
            image_path = os.path.join(root, file)
            print(image_path)

            img = Image.open(image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()

            # 排序
            top_k = predictions.argsort()[-5:][::-1]
            print(top_k)
            for node_id in top_k:
                # 获取分类名称
                human_string = id_to_string(node_id)
                score = predictions[node_id]
                # 输出置信度
                print('%s (score = %.5f)' % (human_string, score))
            print()
