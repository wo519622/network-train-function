from voc_eval import voc_eval

darknet_path = "/opt/jeff_train/darknet/"
sub_files = os.listdir("%s/results" % (darknet_path))
mAP = []
for i in range(len(sub_files)):
    class_name = sub_files[i].split(".txt")[0]
    print(class_name)
    rec, prec, ap = voc_eval('%s/results/{}.txt' % (darknet_path),
                             '%s/cv_train/VOCdevkit/VOC2007/Annotations/{}.xml' % (darknet_path),
                             '%s/cv_train/VOCdevkit/VOC2007/ImageSets/Main/test.txt' % (darknet_path), class_name,
                             '.')
    print(rec, prec, ap)
    print("{} :\t {} ".format(class_name, ap))
    mAP.append(ap)
mAP = tuple(mAP)
print("***************************")
print("mAP :\t {}".format(float(sum(mAP) / len(mAP))))
