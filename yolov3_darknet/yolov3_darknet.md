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
```
python3 voc_label.py
```
