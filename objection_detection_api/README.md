#### 使用谷歌目标检测API快速训练目标检测模型
- environment : Tensorflow 1.9,ubuntu18.04

1.安装
>官方有给出安装help:https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

- clone项目
```
git clone https://github.com/tensorflow/models.git
```
- 替换obejction_detection(18年版本的运行起来没有遇到问题)
```
mv models/research/object_detection models/research/object_detection.org
# 在复制本项目的object_detection到models/research/下
```

2.编译，测试
- 安装protoc>3.0
```
wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
unzip protobuf.zip
```
- protoc编译
```
protoc object_detection/protos/*.proto --python_out=.
```
- 设置环境变量
```
 sudo vim ~/.bashrc
 # 在最后添加,pwd为API安装目录
 export PYTHONPATH=$PYTHONPATH:/pwd/models/research:/pwd/models/research/slim
 source ~/.bashrc
```
- 测试安装
```
python3 object_detection/builders/model_builder_test.py
# 返回ok则success
```
3.tfrecord数据生成
- VOC格式数据生成
- tfrecord数据生成
```
# 训练集
python3 object_detection/dataset_tools/create_pascal_tf_record.py --data_dir=data/ --year=VOC2007 --set=train --output_path=data/pascal_train.record
# 验证集
python3 object_detection/dataset_tools/create_pascal_tf_record.py --data_dir=data/ --year=VOC2007 --set=val --output_path=data/pascal_val.record
# 测试集
python3 object_detection/dataset_tools/create_pascal_tf_record.py --data_dir=data/ --year=VOC2007 --set=test --output_path=data/pascal_test.record
```

4.修改训练配置
- 以faster_rcnn_resnnet50为例子
```
# 下载预训练模型以及配置文件

```


5.训练
```
python3 object_detection/model_main.py --model_dir=data/checkpoints --pipeline_config_path=data/pretrained/faster_rcnn_resnet50_coco.config
```
6.模型转换
```
python3 object_detection/export_inference_graph.py  --input_type image_tensor --pipeline_config_path=data/pretrained/faster_rcnn_resnet50_coco.config --trained_checkpoint_prefix=data/checkpoints/model.ckpt-x --output_directory=data/out_pb
```
7.测试
- 生成计算mAPtfrecord
```
python3 object_detection/inference/infer_detections.py --input_tfrecord_paths=data/test_pascal.record --output_tfrecord_path=data/test_detections.tfrecord  --inference_graph=data/out_pb/frozen_inference_graph.pb --discard_image_pixels
```
- 生成指标相关的配置文件
```
mkdir -p data/test_eval_metrics
vim test_eval_config.pbtxt
# 写入 
# metrics_set: 'coco_detection_metrics'
vim test_input_config.pbtxt
# 写入 
# label_map_path: 'data/pascal_label_map.pbtxt'
# tf_record_input_reader: { input_path: 'data/test_detections.tfrecord@1' }
```
- 计算mAP
```
python3 object_detection/metrics/offline_eval_map_corloc.py --eval_dir=data/test_eval_metrics --eval_config_path=data/test_eval_metrics/test_eval_config.pbtxt --input_config_path=data/test_eval_metrics/test_input_config.pbtxt
```
