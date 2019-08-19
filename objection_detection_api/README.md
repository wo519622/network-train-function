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

