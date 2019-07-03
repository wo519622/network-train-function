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
