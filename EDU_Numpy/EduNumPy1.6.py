from math import radians
import numpy as np                


import numpy as np
tensor = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],

                   [[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]],

                   [[19, 20, 21],
                    [22, 23, 24],
                    [25, 26, 27]]])

result =  tensor[:,1:2,1:2]# массив 2x2 в верхнем левом углу для каждой матрицы

print(f'Подматрица 2x2 в верхнем левом углу для каждой матрицы:\n{result}')