import random

class Matrix:
    def __init__(self, nrows, ncols):   # 初始建立 n*m 矩陣，各value為亂數值
        self.matr=[]                    # 建立list matr
        self.row=nrows
        self.col=ncols

        for i in range(self.row):
            new_row=[]                  # 建立new_row list
            for j in range(self.col):
                value=random.randint(1,9)   
                new_row.append(value)   # 將亂數插入new_row list，重複col次
            self.matr.append(new_row)   # 將new_row list 插入 matr list並重複row次，成為二為陣列matr

    def add(self,B):                           # 求A + B
        print("==========A + B==========")     # 建立一個Matrix C物件 (其matrix row=i,col=j)
        C=Matrix(self.row,self.col) 
        if(self.col==B.col and self.row==B.row):
            for i in range(self.row):
                for j in range(self.col):
                    C.matr[i][j]=A.matr[i][j]+B.matr[i][j]      # 同位相加   
            C.display()                                         # 印出C矩陣
        else:
            print("matrix's size should be in the same size \n")
        
    def sub(self,B):
        print("==========A - B==========")     # 求A - B   
        C=Matrix(self.row,self.col)            # 建立一個Matrix C物件 (其matrix row=A.row,col=B.col)
        if(self.col==B.col and self.row==B.row):
            for i in range(self.row):
                for j in range(self.col):
                    C.matr[i][j]=A.matr[i][j]-B.matr[i][j]      # 同位相減
            C.display()                                         # 印出C矩陣
        else:
            print("matrix's size should be in the same size \n")

    def mul(self,B):                                        # 求A * B
        print("==========A * B==========")
        C=Matrix(self.row,B.col)                            # 建立一個Matrix C物件(其matrix row=i,col=k)
        if(self.col==B.row):                                # EX: for j=3的矩陣
            for i in range(self.row):                       # 重副 A.row 次
                for k in range(B.col):                      # 重複 B.col 次以下動作   
                    value=0
                    for j in range(self.col):
                        value+=self.matr[i][j]*B.matr[j][k]     # 算A[i][j]*B[j][k] (i=A.row, j=A.col =B.row, k=B.col)
                                                                # EX:第一個value值為 ex:A[1][1]*B[1][1]+A[1][2]*B[2][1]+A[1][3]*B[3][1]
                    C.matr[i][k]=value                          # EX:第一個value值存進 C[1][1],k=k+1
            C.display()
        else:       
            print("none \n")       # matrix A,B 無法相乘時，印出none
            C.matr=[]              # 讓 C matrix變成空矩陣(為了讓trans判斷其沒有mul) 
        return C

    def transpose(self):           # 求transpose of A * B
        print("=====the transpose of A * B=====")
        if self.matr!=[]:          # 當該矩陣不等於空矩陣時(matrix A,B 可相乘時)，執行transpose
            C=Matrix(self.col,self.row)
            for i in range(self.col):
                for j in range(self.row):
                    C.matr[i][j]=self.matr[j][i]
            C.display()
        else:             
            print("none \n")       # 當該矩陣等於空矩陣時(matrix A,B 無法相乘時)，印出none

    def display(self):             # 印出陣列
        for i in range(self.row):
            for j in range(self.col):
                print(self.matr[i][j],end=" ") 
            print('')
        print('\n')
        
# 執行主程式
#create A
a=input("Please enter A matrix's rows: ")   # 輸入 matrix A 的 row 和 col
b=input("Please enter A matrix's cols: ")
a=int(a)                                    # 將string 轉成 integer
b=int(b)
A=Matrix(a,b)                               # 定義 Matrix A 這個物件
print("Matrix A(",a,",",b,"):")             
A.display()                                 # 印出 matrix A

#create B
c=input("Please enter B matrix's rows: ")
d=input("Please enter B matrix's cols: ")
c=int(c)
d=int(d)
B=Matrix(c,d)
print("Matrix B(",c,",",d,"):")
B.display()

A.add(B)                    # A+B
A.sub(B)                    # A-B
C=A.mul(B)                  # A*B
C.transpose()               # the transpose of A*B

