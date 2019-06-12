##### Tensorflow--slim训练说明

> slim是基于tensorflow的快速训练模型的API，集成了常见的CNN模型训练.

1.下载github上tensorflow的官方最新的slim代码。

> git clone [github](https://github.com/tensorflow/models)

> slim 文件在research下面

2.数据处理部分，将数据集分成训练集和测试集。

```
pic
--train
  --class 0
  --class 1
--validation
  --class 0
  --class 1
```

3.数据处理部分，将数据集转成TFRecord格式。

```
python3 data_convert.py -t pic/ \
  --train-shards 2\
  --validation-shards 2\
  --num-threads 2 \
  --dataset-name satellite
```

- 会得到4个tfrecor文件和一个label文件。

4.修改slimd中dataset的部分源码。

- 在slim/datasets下复制flower.py,生成satellite.py
- 修改satellite.py中

```
__FILE_PATHTERN='satellite_%s_*.tfrecord'
SPLITS_TO_SIZES={'train':num_train(?),'validation':num_test(?)}
_NUM_CLASSES=num_label(?)
```

- 修改dataset_factory.py

```
#新增
from datasets import satellite
datasets_map={
    "satellite":satellite
}
```

5.下载预训练模型

> 这里以MoblienetV2为例子，按照自己的硬件条件选择合适的CNN网络.
>
> ![1557670143988](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1557670143988.png)

> 下载tar包即可。

6.建立训练目录结构

> 在slim下新建satellite文件夹，并建立三个子文件夹，分别是：data,train_dir,pretrained,同时将3步骤生成的五个文件放入data中，将5步骤中下载的tar包解压到pretraine.

```python
#目录结构
#slim
#--***
#--satellite
#  --data
#    --train***1.tfrecord
#	 --validation***1.tfrecord
#    --train***2.tfrecord
#	 --validation***2.tfrecord
#	 --label.txt
#  --train_dir
#  --pretrained

```

7.训练参数

```python

```

8.测试参数

```python

```

9.生成pb模型

```python

```

10.测试单张图片

```python	

```





