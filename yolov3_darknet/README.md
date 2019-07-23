#### YOLOV3 darknet训练
1.下载源文件
```
git clone https://github.com/pjreddie/darknet
```

2.编译

- 修改Makefile文件
```
cd darknet
cp Makefile Makefile.org
vim Makefile
```
- 修改五处地方（GPU）
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_2.png)

- 编译源文件
```
make
# 注:可能出现“ No package‘opencv' found ”错误. 
# sudo apt install libopencv -dev 安装完成后重新编译即可
```

3.简单测试

- 下载预训练模型
```
wget https://pjreddie.com/media/files/yolov3.weights
```
- 测试
```
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_1.png)

4.生成darknet训练要求数据集

- 整理VOC格式数据集
```
mkdir cv_train
cp script/voc_label.py cv_train/.
cp -r VOCdevkit cv_train/.
```
- xml转txt
```
wget 
https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/make_main_txt.py 
修改测试集合验证集的百分比
# trainval_percent=0.9 训练集加验证集百分比
#train_percent=0.8 训练集加验证集中训练集的百分比
python3 make_main_txt.py

```
- 修改voc_label.py
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_3.png)
```
python3 voc_label.py
```
- 查看目录结构
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_4.png)

5.修改训练文件
- 修改data中的voc.names
```
cp data/voc.names cv_train/.
gedit cv_train/voc.names
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_8.png)
- 修改cfg中的voc.data
```
cp cfg/voc.data cv_train/.
gedit cv_train/ voc.data
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_6.png)
- 修改cfg中的yolov3-voc.cfg
```
cp cfg/yolov3-voc.cfg cv_train/.
gedit cv_train/ yolov3-voc.cfg
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_5.png)
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img_7.png)

6.下载draknet卷积层预训练权重
```
wget https://pjreddie.com/media/files/darknet53.conv.74
```

7.训练模型
- 单GPU训练
```
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74
#保存log
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74 | tee cv_train/train.log
```
- 多GPU训练
```
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74 -gpu 0,1,2,3
```
- CPU训练
```
./darknet -nogpu detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74
```

8.测试模型
- 单张图片测试
```
#注意将yolov3-voc.cfg里面的batch和subdivisions设为1
./darknet detector test cv_train/voc.data cv_train/yolov3-voc.cfg cv_train/backup/yolov3-voc_xxx.weights image.jpg
```
