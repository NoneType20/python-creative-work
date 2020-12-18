import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
# a = tf.ones([10,10]) #10행 10렬을 zeros(0) 으로 초기화 ones(1) 
# b = tf.eye(10) 
# print(a+b) # 더하는것은 shape가 같아야지만 된다 

# # reduce로 행렬 합 , 평균 , 최대갑 , 최소값 
# c = tf.constant([1,2,3,4,5,6,7,8,9,10]) 
# #print(tf.reduce_sum(c)) #행렬 합 
#     # tf.reduce_mean  평균 , tf.reduce_max 최대값 , tf.reduce_min 최소값
# d = c + 5 # c값에 각각 5 추가
# print(d)



#행 만들기 
e = tf.constant([[10],[11],[12],[13],[14]])
f = tf.constant([[1,2,3]])
#print(e)
#print(f)
g = tf.matmul(e,f)  # 곱셈  10 20 30
#                           11 22 33
#                           12 24 36

#덧셈(add) 뺄셈은(subtract) shape가 같아야 가능 ( 행 , 열 )이 같아야함
#print(g) #다음 영상은 9부터 보면 됨  https://www.youtube.com/watch?v=c36iRqaHd6Q&list=PLsGh7Wc318kjY43uABF-39GQMOJPdpyUM&index=9 

h = tf.zeros([100,100])
i = tf.constant([range(300,310)] ,shape=(10,1))
j = tf.constant([range(1,11)])

k = tf.matmul(i,j) 
test = tf.ones([10,10])
test = tf.add(test , test)



print(test)
print('='*50)
print(k)
print('='*50)
result_list = []


for n , m in zip(list(test) , list(k)) : 
    for z ,p in zip(list(n) , list(m)) :
        result_list.append(int(z) * int(p))
testsec = tf.constant([result_list] , shape=(10,10))

print(testsec)


# ac = np.array([k]) 
# ad = np.array([test]) 

# # print(np.matmul(ac,ad))
# kk = tf.constant(10)
# print(tf.matmul(test,k))

