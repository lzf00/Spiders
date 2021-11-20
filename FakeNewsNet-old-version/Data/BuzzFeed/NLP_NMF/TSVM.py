# -*- codeing = utf-8 -*-
# @Time : 2021/2/6 17:10
# @Author : lzf
# @File : TSVM.py
# @Software :PyCharm
#链接：https://blog.csdn.net/FelixWang0515/article/details/94629025?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control
import numpy as np
import sklearn.svm as svm
import joblib
import pickle
from sklearn.model_selection import train_test_split,cross_val_score

class TSVM(object):
    def __init__(self):
        pass

    def initial(self, kernel='rbf'):
        #Initial TSVM，kernel: kernel of svm

        self.Cl, self.Cu = 1, 0.001  #Cl为有标签数据的权重，Cu为无标签数据的权重
        self.kernel = kernel
        self.clf = svm.SVC(C=1, kernel=self.kernel,gamma=3,decision_function_shape='ovo') #惩罚因子C，越大分类效果越好，但有可能会过拟合
        #C是调节间隔与准确率的因子，C值越大，越不愿放弃那些离群点；c值越小，越不重视那些离群点。
        #
    def load(self, model_path='./TSVM.model'):
        '''
        Load TSVM from model_path
        Parameters
        ----------
        model_path: model path of TSVM
        model should be svm in sklearn and saved by sklearn.externals.joblib
        '''
        self.clf = joblib.load(model_path)

    def train(self, X1, Y1, X2):
        '''
        Train TSVM by X1, Y1, X2
        Parameters参数
        ----------
        X1: Input data with labels
                np.array, shape:[n1, m], n1: numbers of samples with labels, m: numbers of features
        Y1: labels of X1
                np.array, shape:[n1, ], n1: numbers of samples with labels
        X2: Input data without labels
                np.array, shape:[n2, m], n2: numbers of samples without labels, m: numbers of features
        '''
        N = len(X1) + len(X2)
        sample_weight = np.ones(N)
        sample_weight[len(X1):] = self.Cu

        self.clf.fit(X1, Y1)
        Y2 = self.clf.predict(X2)
        Y2 = np.expand_dims(Y2, 1)
        X2_id = np.arange(len(X2))
        X3 = np.vstack([X1, X2])
        Y3 = np.vstack([Y1, Y2])

        while self.Cu < self.Cl:
            self.clf.fit(X3, Y3, sample_weight=sample_weight)
            while True:
                Y2_d = self.clf.decision_function(X2)    # linear: w^Tx + b
                Y2 = Y2.reshape(-1)
                epsilon = 1 - Y2 * Y2_d   # calculate function margin
                positive_set, positive_id = epsilon[Y2 > 0], X2_id[Y2 > 0]
                negative_set, negative_id = epsilon[Y2 < 0], X2_id[Y2 < 0]
                positive_max_id = positive_id[np.argmax(positive_set)]
                negative_max_id = negative_id[np.argmax(negative_set)]
                a, b = epsilon[positive_max_id], epsilon[negative_max_id]
                if a > 0 and b > 0 and a + b > 2.0:
                    Y2[positive_max_id] = Y2[positive_max_id] * -1
                    Y2[negative_max_id] = Y2[negative_max_id] * -1
                    Y2 = np.expand_dims(Y2, 1)
                    Y3 = np.vstack([Y1, Y2])
                    self.clf.fit(X3, Y3, sample_weight=sample_weight)##########33
                else:
                    break
            self.Cu = min(2*self.Cu, self.Cl)
            sample_weight[len(X1):] = self.Cu

    def score(self, X, Y):

        #Calculate accuracy of TSVM by X, Y
        return self.clf.score(X, Y)

    def predict(self, X):

        #Feed X and predict Y by TSVM
        return self.clf.predict(X)

    def save(self, path='./TSVM.model'):
        '''
        Save TSVM to model_path
        Parameters
        ----------
        model_path: model path of TSVM
                        model should be svm in sklearn
        '''
        joblib.dump(self.clf, path)
def show_accuracy(a, b, tip):
  acc = (a.ravel () == b.ravel ())  #ravel扁平化数据
  print ( "%s Accuracy:%.6f" % (tip, np.mean ( acc )) )

if __name__ == '__main__':
    path = 'True_mat_W.csv'
    data = np.loadtxt ( path, dtype=float, delimiter=' ' )
    print ( '矩阵1维度:::', data.shape )

    path1 = 'T_mat_W.csv'
    x2 = np.loadtxt ( path1, dtype=float, delimiter=' ' )
    print ( '矩阵2维度:::', x2.shape )
    # print(data)
    y = np.ones ( (90,1 ) )  # 74行1列的‘1’矩阵
    # print(y)
    for i in range ( 81 ):
        y = np.append ( y, [[-1]], axis=0 )  # 直接在np数据后面添加元素，加入列表元素【0】，axis=0，1表示垂直，水平方向
    # print(y)
    # 实验链接https://www.cnblogs.com/luyaoblog/p/6775342.html
    x_train, x_test, y_train, y_test = train_test_split ( data[:, 0:10], y,random_state=0, train_size=0.8 )#不设置random_state，则每次随机数据不一样，random_state=100

    model = TSVM()
    model.initial()
    model.train(x_train, y_train,x2[:,0:10])  #x2为无标签的数据,x2[:,0:10]取x2多少行，10列的数据，x2为无标签数据
    #y_hat=np.ones((71,1))
    y_hat = model.predict (x_train )
    print('训练:',y_hat)
    show_accuracy ( y_hat, y_train, '训练集' )
    y_hat1 = model.predict(x_test  )
    print('测试:',y_hat1)
    show_accuracy ( y_hat1, y_test, '测试集' )
    #y_test=y_test.values.ravel ()
    accuracy = model.score(x_test, y_test)  #测试
    #print('Accuracy:',accuracy)


