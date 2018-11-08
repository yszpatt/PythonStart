python3 /Users/shenzheng/models/research/slim/train_image_classifier.py  \
--train_dir=/Users/shenzheng/retrain \
--dataset_name=myimages \
--dataset_split_name=train \
--dataset_dir=/Users/shenzheng/retrain/data/train \
--batch_size=10 \
--max_number_of_steps=150 \
--model_name=inception_v3