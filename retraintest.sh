#!/bin/bash
python3 /Users/shenzheng/PythonStart/mineretrain.py \
--bottleneck_dir /Users/shenzheng/retrain/bottleneck \
--how_many_training_steps 2000 \
--model_dir /Users/shenzheng/inception/inception_model \
--output_graph /Users/shenzheng/retrain/output_graph.pb \
--output_labels /Users/shenzheng/retrain/output_labels.txt \
--image_dir /Users/shenzheng/retrain/data/train/ 

