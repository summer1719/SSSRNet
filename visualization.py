import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors    #相当于matlab imshow python版本
import torchvision

def get_n_params(model):
    pp=0
    for p in list(model.parameters()):
        nn=1
        for s in list(p.size()):
            nn = nn*s
        pp += nn
    return pp

def show_label1(gt, pred):
    import matplotlib.pyplot as plt
    from matplotlib import colors
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig, axes = plt.subplots(1, 2)
    ax1, ax2 = axes

    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax1.set_title('gt')
    ax1.imshow(gt, cmap=cmap, norm=norm)

    ax2.set_title('pred')
    ax2.imshow(pred, cmap=cmap, norm=norm)

    plt.show()

def show_seg(gt, pred, sr, label_heatmap, image_cls):

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig1, axes1 = plt.subplots(1, 3)
    ax1, ax2, ax3 = axes1

    fig2, axes2 = plt.subplots(2, 1)
    ax4, ax5 = axes2

    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax1.set_title('gt')
    axes1[0].axis('off')
    ax1.imshow(gt)

    ax2.set_title('pred')
    axes1[1].axis('off')
    ax2.imshow(pred, cmap=cmap, norm=norm)

    ax3.set_title('sr')
    axes1[2].axis('off')
    ax3.imshow(sr)

    ax4.imshow(label_heatmap)
    axes2[0].axis('off')
    ax5.imshow(image_cls)
    axes2[1].axis('off')

    plt.show()


def show_features_test(features, batch, num_chns):

    size = features.data[0].size()
    #feature_maps = features.cpu().data[batch].view(size[0]//num_chns, num_chns, size[1], size[2])
    feature_maps = features.cpu().data[batch,15*32:16*32].view(32, num_chns, size[1], size[2])
    image_features = torchvision.utils.make_grid(feature_maps)
    image_features = image_features.numpy().transpose((1,2,0))

    #fig, ax = plt.subplots(1, 1)
    #ax.imshow(image_features)
    plt.figure()
    plt.imshow(image_features)
    plt.show()


def show_ssloss_seg(gt, pred_gt, sr, pred_sr):

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig1, axes1 = plt.subplots(2, 2)
    ax1_1, ax1_2, ax2_1, ax2_2= axes1


    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax1_1.set_title('gt')
    axes1[0].axis('off')
    ax1_1.imshow(gt)

    ax1_2.set_title('pred_gt')
    axes1[1].axis('off')
    ax1_2.imshow(pred_gt, cmap=cmap, norm=norm)

    ax2_1.set_title('sr')
    axes1[2].axis('off')
    ax2_1.imshow(sr)

    ax2_2.set_title('pred_sr')
    axes1[3].axis('off')
    ax2_2.imshow(pred_sr, cmap=cmap, norm=norm)

    plt.show()

def show_ssloss_seg1(hr, gt_label, hr_label, sr_label):

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig1, axes1 = plt.subplots(2, 2)
    ax1_1, ax1_2 = axes1[0]
    ax2_1, ax2_2 = axes1[1]


    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax1_1.set_title('gt')
    axes1[0,0].axis('off')
    ax1_1.imshow(hr)

    ax1_2.set_title('gt_label')
    axes1[0,1].axis('off')
    ax1_2.imshow(gt_label, cmap=cmap, norm=norm)

    ax2_1.set_title('hr_label')
    axes1[1,0].axis('off')
    ax2_1.imshow(hr_label, cmap=cmap, norm=norm)

    ax2_2.set_title('sr_label')
    axes1[1,1].axis('off')
    ax2_2.imshow(sr_label, cmap=cmap, norm=norm)

    plt.show()

def show_image(image, is_Variable=True):
# input 4D Varialble or Tensor (N*C*H*W)
    if is_Variable:
        img = image.cpu().data[0].numpy().transpose((1,2,0))
    else:
        img = image[0].numpy().transpose((1,2,0))

    plt.imshow(img, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def show_label(label, is_label=True):
# input 3D label (N*H*W) Tensor or 4D seg Tensor (N*C*H*W)
    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    if is_label:
        label = np.asarray(label[0].numpy(), dtype=np.int)
    else:
        label = label[0].numpy()
        label = label.transpose(1, 2, 0)
        label = np.asarray(np.argmax(label, axis=2), dtype=np.int)


    plt.imshow(label, cmap=cmap, norm=norm)
    plt.axis('off')
    plt.show()


def show_features(features, batch, num_chns):
    # input 4D Varialble (N*C*H*W)
    size = features.cpu().data[0].size()
    feature_maps = features.cpu().data[batch].view(size[0]//num_chns, num_chns, size[1], size[2])
    image_features = torchvision.utils.make_grid(feature_maps, padding=3, pad_value=1)
    image_features = image_features.numpy().transpose((1,2,0))

    #fig, ax = plt.subplots(1, 1)
    #ax.imshow(image_features)
    plt.imshow(image_features, interpolation='nearest')
    plt.axis('off')
    plt.show()

def show_input(lr, lr_label, hr, hr_label):
    # input 4D Varialble images and 3D label (N*H*W) Tensor
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    fig1, axes1 = plt.subplots(2, 2)    #绘制多个子图 2行2列
    ax1_1, ax1_2 = axes1[0]
    ax2_1, ax2_2 = axes1[1]


    classes = np.array(('background',  # always index 0
               'aeroplane', 'bicycle', 'bird', 'boat',
               'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'))
    colormap = [(0,0,0),(0.5,0,0),(0,0.5,0),(0.5,0.5,0),(0,0,0.5),(0.5,0,0.5),(0,0.5,0.5),
                    (0.5,0.5,0.5),(0.25,0,0),(0.75,0,0),(0.25,0.5,0),(0.75,0.5,0),(0.25,0,0.5),
                    (0.75,0,0.5),(0.25,0.5,0.5),(0.75,0.5,0.5),(0,0.25,0),(0.5,0.25,0),(0,0.75,0),
                    (0.5,0.75,0),(0,0.25,0.5)]
    cmap = colors.ListedColormap(colormap)    #listedcolormap产生非渐变的颜色映射
    bounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    norm = colors.BoundaryNorm(bounds, cmap.N)    #参数boundaries的值为单调递增数列。ncolors为我们希望在图像中用到的colormap中的颜色个数

    lr_img = lr.cpu().data[0].numpy().transpose((1, 2, 0))    #显示 基本所有读图库都是hxwxc
    hr_img = hr.cpu().data[0].numpy().transpose((1, 2, 0))

    lr_gt = np.asarray(lr_label[0].numpy(), dtype=np.int)
    hr_gt = np.asarray(hr_label[0].numpy(), dtype=np.int)

    ax1_1.set_title('lr')
    axes1[0,0].axis('off')
    ax1_1.imshow(lr_img, interpolation='bilinear')

    ax1_2.set_title('lr_label')
    axes1[0,1].axis('off')
    ax1_2.imshow(lr_gt, cmap=cmap, norm=norm)

    ax2_1.set_title('hr')
    axes1[1,0].axis('off')
    ax2_1.imshow(hr_img, interpolation='bilinear')

    ax2_2.set_title('hr_label')
    axes1[1,1].axis('off')    #00 01 10 11 subplot 位置
    ax2_2.imshow(hr_gt, cmap=cmap, norm=norm)

    plt.show()