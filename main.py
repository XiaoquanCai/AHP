import numpy as np
from AHP import AHP
# 准则重要性矩阵
'''
   因素i比因素j         量化值
    同等重要             1
    稍微重要             3
    较强重要             5
    强烈重要             7
    极端重要             9
两相邻判断的中间值     2，4，6，8

A为准则层按两两比较的矩阵

a_ij=1/a_ji
'''
criteria = np.array([[1, 2, 7, 5, 5],
                     [1 / 2, 1, 4, 3, 3],
                     [1 / 7, 1 / 4, 1, 1 / 2, 1 / 3],
                     [1 / 5, 1 / 3, 2, 1, 1],
                     [1 / 5, 1 / 3, 3, 1, 1]])

# 构造所有相对于不同准则的方案层判断矩阵
'''
   因素i比因素j         量化值
    同等重要             1
    稍微重要             3
    较强重要             5
    强烈重要             7
    极端重要             9
两相邻判断的中间值     2，4，6，8

b_ij=1/b_ji
'''
b1 = np.array([[1, 1 / 3, 1 / 8],
               [3, 1, 1 / 3],
               [8, 3, 1]])
b2 = np.array([[1, 2, 5],
               [1 / 2, 1, 2],
               [1 / 5, 1 / 2, 1]])
b3 = np.array([[1, 1, 3],
               [1, 1, 3],
               [1 / 3, 1 / 3, 1]])
b4 = np.array([[1, 3, 4],
               [1 / 3, 1, 1],
               [1 / 4, 1, 1]])
b5 = np.array([[1, 4, 1 / 2],
               [1 / 4, 1, 1 / 4],
               [2, 4, 1]])

b = [b1, b2, b3, b4, b5]
a = AHP(criteria, b).run()
