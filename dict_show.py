classes = {'background': [26.520524878026631, 1449], 'aeroplane': [22.755793952309791, 90], 'bicycle': [18.81372769902962, 79], 'bird': [24.600439461563909, 103], 'boat': [21.234290924615102, 72], 'bottle': [22.983264973480232, 96], 'bus': [21.993208600359111, 74], 'car': [22.036677125185189, 127], 'cat': [27.676353510054156, 119], 'chair': [27.446874212999749, 123], 'cow': [26.811450789081846, 71], 'diningtable': [26.102268549772383, 75], 'dog': [27.868479654115809, 128], 'horse': [26.466056067182233, 79], 'motorbike': [20.615119930850437, 76], 'person': [25.634813033392618, 446], 'pottedplant': [23.041459298970313, 85], 'sheep': [25.616622002522877, 57], 'sofa': [29.118444071957359, 90], 'train': [21.757411810357805, 84], 'tvmonitor': [26.631676893425187, 74], 'all': [25.739090161917876, 1449]}
for key in classes.keys():
    print('%s' % key)
    print('{:.4f} dB   {}'.format(classes[key][0], classes[key][1]))