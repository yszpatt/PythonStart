#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import os
import numpy as np
# import re
from PIL import Image
import matplotlib.pyplot as plt


class NodeLookup(object):
    def __init__(self):
        label_lookup_path = '/Users/shenzheng/inception/inception_model/imagenet_2012_challenge_label_map_proto.pbtxt'
        uid_lookup_path = '/Users/shenzheng/inception/inception_model/imagenet_synset_to_human_label_map.txt'
        self.node_lookup = self.load(label_lookup_path, uid_lookup_path)

    def load(self, label_lookup_path, uid_lookup_path):
        proto_as_ascii_lines = tf.gfile.GFile(uid_lookup_path).readlines()
        uid_to_human = {}
        for line in proto_as_ascii_lines:
            # 去掉换行符
            line = line.strip('\n')
            # 按照\t分割
            parsed_items = line.split('\t')
            # 获取分类编号
            uid = parsed_items[0]
            # 获取分类名称
            human_string = parsed_items[1]
            # 保存编号字符串与分类名称映射关系
            uid_to_human[uid] = human_string

        proto_as_ascii = tf.gfile.GFile(label_lookup_path).readlines()
        node_id_to_uid = {}
        for line in proto_as_ascii:
            if line.startswith('  target_class:'):
                # 获取分类编号
                target_class = int(line.split(': ')[1])
            if line.startswith('  target_class_string:'):
                # 获取编号字符串n******
                target_class_string = line.split(': ')[1]
                # 保存分类编号1-1000与编号字符串n*****映射关系
                node_id_to_uid[target_class] = target_class_string[1:-2]

        # 建立分类编号1-1000对应分类名称映射关系
        node_id_to_name = {}
        for key, val in node_id_to_uid.items():
            name = uid_to_human[val]
            node_id_to_name[key] = name
        return node_id_to_name

        # 传入分类编号1-1000的返回名称
    def id_to_string(self, node_id):
        if node_id not in self.node_lookup:
            return ''
        return self.node_lookup[node_id]


with tf.gfile.FastGFile('/Users/shenzheng/inception/inception_model/classify_image_graph_def.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
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
            node_lookup = NodeLookup()
            for node_id in top_k:
                # 获取分类名称
                human_string = node_lookup.id_to_string(node_id)
                score = predictions[node_id]
                # 输出置信度
                print('%s (score = %.5f)' % (human_string, score))
            print()
