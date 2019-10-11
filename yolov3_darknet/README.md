### YOLOV3 darknet训练
---
##### 1. 下载源文件
```bash
git clone https://github.com/pjreddie/darknet
```
---
##### 2. 编译
- 修改Makefile文件
```bash
cd darknet
cp Makefile Makefile.org
vim Makefile
```
- 修改五处地方（GPU）
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_2.png)
- 编译源文件
```bash
make
# 注:可能出现“ No package‘opencv' found ”错误. 
# sudo apt install libopencv -dev 安装完成后重新编译即可
```
---
##### 3. 简单测试
- 下载预训练模型
```bash
wget https://pjreddie.com/media/files/yolov3.weights
```
- 测试
```bash
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_1.png)
---
##### 4. 生成darknet训练要求数据集
- 整理VOC格式数据集
```bash
mkdir cv_train
cp script/voc_label.py cv_train/.
cp -r VOCdevkit cv_train/.
```
- xml转txt
```bash
wget 
https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/make_main_txt.py 
修改测试集合验证集的百分比
# trainval_percent=0.9 训练集加验证集百分比
#train_percent=0.8 训练集加验证集中训练集的百分比
python3 make_main_txt.py
```
- 修改voc_label.py
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_3.png)
```bash
python3 voc_label.py
```
- 查看目录结构
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_4.png)
---
##### 5. 修改训练文件
- 修改data中的voc.names
```bash
cp data/voc.names cv_train/.
gedit cv_train/voc.names
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_8.png)
- 修改cfg中的voc.data
```bash
cp cfg/voc.data cv_train/.
gedit cv_train/ voc.data
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_6.png)
- 修改cfg中的yolov3-voc.cfg
```bash
cp cfg/yolov3-voc.cfg cv_train/.
gedit cv_train/ yolov3-voc.cfg
```
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_5.png)
![image](https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/img/img_7.png)
---
##### 6. 下载draknet卷积层预训练权重
```bash
wget https://pjreddie.com/media/files/darknet53.conv.74
```
---
##### 7. 训练模型
- 单GPU训练
```bash
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74
#保存log
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74 | tee cv_train/train.log
```
- 多GPU训练
```bash
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74 -gpu 0,1,2,3
```
- checkpoint继续训练
```bash
./darknet detector train cv_train/voc.data cv_train/yolov3-voc.cfg cv_train/backup/yolov3-voc.backup
```
- CPU训练
```bash
./darknet -nogpu detector train cv_train/voc.data cv_train/yolov3-voc.cfg darknet53.conv.74
```
---
##### 8. 测试模型
- 单张图片测试
```bash
#注意将yolov3-voc.cfg里面的batch和subdivisions设为1 (只显示框好后的图片和类别、置信率)
./darknet detector test cv_train/voc.data cv_train/yolov3-voc.cfg cv_train/backup/yolov3-voc_xxx.weights image.jpg
```
- 多张图片测试
```bash
# 修改./examples/detector.c
cp ./examples/detector.c ./example/detector.c.org
wget https://github.com/Jeffer-hua/network-train-function/blob/master/yolov3_darknet/detector.c
vim ./examples/detector.c
# 根据文中注释将三处改为自己的路劲
# 重新编译
make clean
make
./darknet detector test cv_train/voc.data cv_train/yolov3-voc.cfg cv_train/backup/yolov3-voc_xxx.weights
# Enter Image Path : 输入测试txt，eg: ./cv_train/2007_test.txt
# 结果会保存在 ./data/test_out
```
---
##### 9. 计算mAP，Recall
- 生成预测结果
```bash
./darknet detector valid cv_train/voc.data cv_train/yolov3-voc.cfg cv_train/backup/yolov3-voc_xxxx.weights -thresh .5
# 结果会以comp4_det_test_[类名].txt保存在./result中
mv comp4_det_test_[类名].txt [类名].txt
# 将生成的预测结果文件名重命名
```
- 计算mAP
```bash
# 目前是采用py-faster-rcnn下的voc_eval.py计算mAP,
# 下载compute_map_py2
cd compute_map_py2
vim compute_mAP.py
# 将darknet_path修改为自己的路劲
python compute_mAP.py
```
---
