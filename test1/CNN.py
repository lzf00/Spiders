# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 21:59
# @Author : lzf
# @File : CNN.py
# @Software :PyCharm
import mnist
import numpy as np
import matplotlib.pyplot as plt

#查看数据
im = mnist.test_images()[0]
print(im.shape)
plt.imshow(im, cmap='Greys')
plt.show()

#卷积层
class Conv3x3:
    # 使用3x3滤波器的卷积层
    def __init__(self, num_filters):
        self.num_filters = num_filters

        # filters是一个具有维度的3d数组
        # 除以9以减少初始值的方差
        self.filters = np.random.randn ( num_filters, 3, 3 ) / 9

    def iterate_regions(self, image):
        #图像矩阵
        h, w = image.shape

        for i in range ( h - 2 ):
            for j in range ( w - 2 ):
                im_region = image[i:(i + 3), j:(j + 3)]
                yield im_region, i, j

    def forward(self, input):
        # 28x28
        self.last_input = input

        #输入：图像矩阵
        h, w = input.shape
        output = np.zeros ( (h - 2, w - 2, self.num_filters) )

        for im_region, i, j in self.iterate_regions ( input ):
            output[i, j] = np.sum ( im_region * self.filters, axis=(1, 2) )

        return output

    def backprop(self, d_L_d_out, learn_rate):
        #d_L_d_out: 该层输出的损耗梯度
        #learn_rate
        d_L_d_filters = np.zeros ( self.filters.shape )

        for im_region, i, j in self.iterate_regions ( self.last_input ):
            for f in range ( self.num_filters ):
                #d_L_d_filters[f]:3x3矩阵
                #d_L_d_out[i, j, f]:num
                #im_region:图像区域，3x3矩阵图像
                d_L_d_filters[f] += d_L_d_out[i, j, f] * im_region

        #更新滤波器
        self.filters -= learn_rate * d_L_d_filters

        return None

#池化层
class MaxPool2:
    #池大小为2的最大池化层
    def iterate_regions(self, image):

        #生成非重叠的2x2图像区域以聚集在一起
        #image是一个2d numpy数组
        #image：conv层的3d矩阵

        h, w, _ = image.shape
        new_h = h // 2
        new_w = w // 2

        for i in range ( new_h ):
            for j in range ( new_w ):
                im_region = image[(i * 2):(i * 2 + 2), (j * 2):(j * 2 + 2)]
                yield im_region, i, j

    def forward(self, input):
        '''
        使用给定的输入执行maxpool层的前向传递
        返回具有维度(h/2,w/2,num_filters)的3d numpy数组
        输入是一个具有维度(h, w, num_filters)的3d numpy数组
        '''
        # 26x26x8
        self.last_input = input

        #输入：conv层的3d矩阵
        h, w, num_filters = input.shape
        output = np.zeros ( (h // 2, w // 2, num_filters) )

        for im_region, i, j in self.iterate_regions ( input ):
            output[i, j] = np.amax ( im_region, axis=(0, 1) )

        return output

    def backprop(self, d_L_d_out):
        # d_L_d_out:层输出的损耗梯度

        d_L_d_input = np.zeros ( self.last_input.shape )

        for im_region, i, j in self.iterate_regions ( self.last_input ):
            h, w, f = im_region.shape
            amax = np.amax ( im_region, axis=(0, 1) )

            for i2 in range ( h ):
                for j2 in range ( w ):
                    for f2 in range ( f ):
                        #如果这个像素是最大值,将梯度复制给它
                        if im_region[i2, j2, f2] == amax[f2]:
                            d_L_d_input[i + i2, j + j2, f2] = d_L_d_out[i, j, f2]

        return d_L_d_input

#全连接层
class Softmax:
    #一个标准的全连接层与softmax激活

    def __init__(self, input_len, nodes):
        #除以input_len以减少初始值的方差。input_len：输入节点的长度，nodes：输出节点的长度
        self.weights = np.random.randn ( input_len, nodes ) / input_len
        self.biases = np.zeros ( nodes )

    def forward(self, input):
        '''
        使用给定的输入执行softmax层的前向传递。
        返回包含相应概率值的1d numpy数组。
        -input可以是任何维度的任何数组。
        '''
        # 3d
        self.last_input_shape = input.shape

        # 3d to 1d
        input = input.flatten ()

        self.last_input = input

        input_len, nodes = self.weights.shape

        totals = np.dot ( input, self.weights ) + self.biases

        # softmax之前的输出
        # 一维矢量
        self.last_totals = totals

        exp = np.exp ( totals )
        return exp / np.sum ( exp, axis=0 )

    def backprop(self, d_L_d_out, learn_rate):
        for i, gradient in enumerate ( d_L_d_out ):
            #k != c, gradient = 0
            #k == c, gradient = 1
            #当k等于c时，找出i的值
            if gradient == 0:
                continue

            t_exp = np.exp ( self.last_totals )
            S = np.sum ( t_exp )

            d_out_d_t = -t_exp[i] * t_exp / (S ** 2)
            d_out_d_t[i] = t_exp[i] * (S - t_exp[i]) / (S ** 2)

            #每个节点的权重渐变
            d_t_d_w = self.last_input  #矢量
            d_t_d_b = 1
            #1000 x 10
            d_t_d_inputs = self.weights

            #总损失梯度
            #d_L_d_t, d_out_d_t, vector, 10 elements
            d_L_d_t = gradient * d_out_d_t

            #weights/biases/input的损失梯度
            #(1000, 1) @ (1, 10) to (1000, 10)
            d_L_d_w = d_t_d_w[np.newaxis].T @ d_L_d_t[np.newaxis]
            d_L_d_b = d_L_d_t * d_t_d_b
            #(1000, 10) @ (10, 1)
            d_L_d_inputs = d_t_d_inputs @ d_L_d_t

            #更新 weights/biases
            self.weights -= learn_rate * d_L_d_w
            self.biases -= learn_rate * d_L_d_b

            #它将在上一个池层中使用
            #重塑这个矩阵
            return d_L_d_inputs.reshape ( self.last_input_shape )


# 测试：只使用前1000测试示例（总共10000个）
test_images = mnist.test_images ()[:1000]
test_labels = mnist.test_labels ()[:1000]

#训练：使用每组的前1000个例子。
train_images = mnist.train_images ()[:1000]
train_labels = mnist.train_labels ()[:1000]

conv = Conv3x3 ( 8 )  # 28x28x1 -> 26x26x8
pool = MaxPool2 ()  # 26x26x8 -> 13x13x8
softmax = Softmax ( 13 * 13 * 8, 10 )  # 13x13x8 -> 10

def forward(image, label):
    '''
    完成CNN的向前传递，并计算精度和交叉熵损失。
    - image是一个2d numpy数组
    - label是一个数字
    '''
    #标准做法：将图像从[0，255]转换为[-0.5，0.5]
    out = conv.forward ( (image / 255) - 0.5 )
    out = pool.forward ( out )
    out = softmax.forward ( out )

    #计算交叉熵损失和精度
    loss = -np.log ( out[label] )
    acc = 1 if np.argmax ( out ) == label else 0

    return out, loss, acc #概率向量，数字，1or0

def train(im, label, lr=0.003  ):   #first：0.003，second：0.01，third：0.005, 0.007,0.006,0.004,0.009

    out, loss, acc = forward ( im, label )#forward

    #计算初始梯度
    gradient = np.zeros ( 10 )
    gradient[label] = -1 / out[label]

    gradient = softmax.backprop ( gradient, lr )#Backprop
    gradient = pool.backprop ( gradient )
    gradient = conv.backprop ( gradient, lr )

    return loss, acc

print ( 'MNIST CNN initialized!' )

#训练迭代次数epoch
for epoch in range ( 3 ):
    print ( '--- Epoch %d ---' % (epoch + 1) )

    #洗牌训练数据
    permutation = np.random.permutation ( len ( train_images ) )
    train_images = train_images[permutation]
    train_labels = train_labels[permutation]
    #训练
    loss = 0
    num_correct = 0
    # i: index，im: image，label: label
    for i, (im, label) in enumerate ( zip ( train_images, train_labels ) ):
        if i > 0 and i % 100 == 99:
            print (
                '[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%' %(i + 1, loss / 100, num_correct)
            )
            loss = 0
            num_correct = 0

        l, acc = train ( im, label )
        loss += l
        num_correct += acc

#测试
print ( '\n--- Testing the CNN ---' )
loss = 0
num_correct = 0
for im, label in zip ( test_images, test_labels ):
    _, l, acc = forward ( im, label )
    loss += l
    num_correct += acc

num_tests = len ( test_images )
print ( 'Test Loss:', loss / num_tests )
print ( 'Test Accuracy:', num_correct / num_tests )
