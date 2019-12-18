#### 工程中使用darknet的方法
1.darknet 读取numpy格式图片,如opencv-python读取的视频流
- 修改image.c以及image.h
```shell script
// 1.添加至image.c
#ifdef NUMPY
image ndarray_to_image(unsigned char* src, long* shape, long* strides)
{
    int h = shape[0]; 
    int w = shape[1]; 
    int c = shape[2]; 
    int step_h = strides[0]; 
    int step_w = strides[1]; 
    int step_c = strides[2]; 
    image im = make_image(w, h, c); 
    int i, j, k; 
    int index1, index2 = 0;

    for(i = 0; i < h; ++i){
        for(k= 0; k < c; ++k){
            for(j = 0; j < w; ++j){
                index1 = k*w*h + i*w + j;
                index2 = step_h*i + step_w*j + step_c*k;
                // fprintf(stderr, "w=%d h=%d c=%d step_w=%d step_h=%d step_c=%d \n", w, h, c, step_w, step_h, step_c); 
                // fprintf(stderr, "im.data[%d]=%u data[%d]=%f \n", index1, src[index2], index2, src[index2]/255.); 
                im.data[index1] = src[index2]/255.;
            }
        }
    }
    rgbgr_image(im);

    return im;        
}
#endif
```
```shell script
//2.添加至image.h
#ifdef NUMPY
image ndarray_to_image(unsigned char* src, long* shape, long* strides);
#endif
```
>目录下有修改好的文件,clone替换即可
---
- 修改Makefile文件
>最前面添加NUMPY=1
```shell script
GPU=0
CUDNN=0
OPENCV=0
OPENMP=0
NUMPY=1
DEBUG=0
```
>在大概50行找个地方添加
```shell script
ifeq ($(NUMPY), 1) 
COMMON+= -DNUMPY -I/usr/include/python3.6/ -I/usr/lib/python3.6/dist-packages/numpy/core/include/numpy/ 
CFLAGS+= -DNUMPY 
endif
```
---
- 重新编译