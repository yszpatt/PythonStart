#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import os
import random
# import math
import sys
from PIL import Image
import numpy as np

_NUM_TEST = 500
_RANDOM_SEED = 0
_NUM_SHARDS = 5
DATASET_DIR = 'captcha/images/'
TFRECORD_DIT = 'captcha/'
# LABELS_FILENAME = '/Users/shenzheng/retrain/data/labels.txt'


# def _get_dataset_filename(dataset_dir, split_name, shard_id):
#     output_filename = 'image_%s_%05d-of-%05d.tfrecord' % (
#         split_name, shard_id, _NUM_SHARDS)
#     return os.path.join(dataset_dir, output_filename)


def _dataset_exists(dataset_dir):
    for split_name in ['train', 'test']:
        output_filename = os.path.join(dataset_dir, split_name + '.tfrecords')
        if not tf.gfile.Exists(output_filename):
            return False
    return True


def _get_filename_and_classes(dataset_dir):
    photo_filenames = []
    for filename in os.listdir(dataset_dir):
        path = os.path.join(dataset_dir, filename)
        photo_filenames.append(path)
    return photo_filenames


def int64_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))


def image_to_tfexample(image_data, label0, label1, label2, label3):
    return tf.train.Example(features=tf.train.Features(feature={
        'image': bytes_feature(image_data),
        'label0': int64_feature(label0),
        'label1': int64_feature(label1),
        'label2': int64_feature(label2),
        'label3': int64_feature(label3),
    }))


# def write_label_file(labels_to_class_names, dataset_dir, filename=LABELS_FILENAME):
#     labels_name = os.path.join(dataset_dir, filename)
#     with tf.gfile.Open(labels_name, 'w') as f:
#         for label in labels_to_class_names:
#             class_name = labels_to_class_names[label]
#             # print(label)
#             f.write('%d:%s\n' % (label, class_name))


def _convert_dataset(split_name, filenames, dataset_dir):
    assert split_name in ['train', 'test']
    # num_per_shard = int(len(filenames) / _NUM_SHARDS)
    with tf.Session() as sess:
        output_filename = os.path.join(TFRECORD_DIT, split_name + '.tfrecords')
        with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
            for i, filename in enumerate(filenames):
                try:
                    sys.stdout.write('\r>>Converting image %d/%d' %
                                     (i + 1, len(filenames)))

                    sys.stdout.flush()

                    image_data = Image.open(filename)
                    image_data = image_data.resize((224, 224))
                    image_data = np.array(image_data.convert('L'))
                    image_data = image_data.tobytes()

                    labels = filename.split('/')[-1][0:4]
                    num_labels = []
                    for j in range(4):
                        num_labels.append(int(labels[j]))
                    example = image_to_tfexample(
                        image_data, num_labels[0], num_labels[1], num_labels[2], num_labels[3])
                    tfrecord_writer.write(example.SerializeToString())

                except IOError as e:
                    print("Could not read:", filenames[i])
                    print("Error:", e)
                    print("Skip it\n")
    sys.stdout.write('\n')
    sys.stdout.flush()


if _dataset_exists(TFRECORD_DIT):
    print('tfrecord文件已经存在')
else:
    photo_filenames = _get_filename_and_classes(DATASET_DIR)
    random.seed(_RANDOM_SEED)
    random.shuffle(photo_filenames)
    training_filenames = photo_filenames[_NUM_TEST:]
    testing_filenames = photo_filenames[:_NUM_TEST]

    _convert_dataset('train', training_filenames, DATASET_DIR)
    _convert_dataset('test', testing_filenames, DATASET_DIR)

    print('生成tfrecord文件')
