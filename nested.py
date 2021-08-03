import unittest
class matrices:
    mat = []
    a = []
    det =[]
    def __init__(self,x):
        i = 1
        f = 0
        while(i < len(x) and f == 0):
            if(len(x[i])==len(x[i-1])):
                i = i + 1
            else:
                f =1
        if(f == 0):
            self.mat = x
            print (self.mat)
        else:
            print("invalid matrix")
    def display(self):
        if(self.mat):
            for i in self.mat:
                print(i)
                return self.mat
        else:
            return(False)
    # def __str__(self):
    #     string = ','.join([str(elem) for elem in self.mat])
    #     return string
    def __add__(self,other):
         if len(self.mat )== len(other.mat)and len(self.mat[0])==len(other.mat[0]):
            a = matrices([])
            a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(other.mat)) ]
            for i in range(len(other.mat)):
                for j in range(len(other.mat[0])):
                    a.mat[i][j] = self.mat[i][j]+(other.mat[i][j]) 
            return a
         else:
             matr = matrices([])
             return matr
    def __sub__(self,other):
         if len(self.mat )== len(other.mat)and len(self.mat[0])==len(other.mat[0]):
            a = matrices([])
            a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(other.mat)) ]
            for i in range(len(other.mat)):
                for j in range(len(other.mat[0])):
                    a.mat[i][j] = self.mat[i][j]-(other.mat[i][j]) 
            return a
         else:
              matr = matrices([])
              return matr
    def __mul__(self,other):
         if len(self.mat[0]) == len(other.mat):
            a = matrices([])
            a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(self.mat)) ]
            for i in range(len(a.mat)):
                for j in range(len(a.mat[0])):
                    sum = 0
                    for k in range(len(self.mat[0])):
                        sum = sum + self.mat[i][k]*other.mat[k][j]
                    a.mat[i][j] = sum
            return a
         else:
             matr = matrices([])
             return matr
    def det(self,matrix):
        if len(self.mat) == len(self.mat[0]):
            sum = 0
            n = len(self.mat)
            
            if n == 2 :
                return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
            else:
                for j in range(len(matrix[0])):
                    a1 = 0 
                    a2 = 0
                    m = [ [ 0 for i in range(len(self.mat[0])-1) ] for j in range(len(self.mat)-1) ]
                    for i in range(1,len(matrix[0])):
                        for k in range(len(matrix[0])):
                            if k != j:
                                m[a1][a2] = matrix[i][k]
                                a2 = ((a2+1)%(n-1))
                        a1 = (a1+1)%(n-1)
                        obj = matrices(m)
                    sum = sum + pow(-1,j)*matrix[0][j]*obj.det(m)
            return sum
        else:
            return False

             
                        
                # sum = sum + ((-1).pow(j+1))*det()
                # print (m)
    def __pow__(self,other,modulo = None):
         if len(self.mat) == len(self.mat[0]):
            obj1 = matrices([])
            obj1.mat = self.mat
            for i in range(other-1):
                obj1 = obj1 * self
            return obj1
         else:
            return False

        


class Test(unittest.TestCase):

    def setUp(self):
        self.matrix1 = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        self.matrix2 = matrices([[1, 5, 6], [3, 11, 2], [1, 9, 5]])
        self.expo = 2

    def tearDown(self):
        print("\n")

    def test_add(self):
        MatrixSum = self.matrix1 + self.matrix2
        output = matrices([[2, 7, 9], [5, 12, 5], [4, 16, 14]])
        self.assertEqual(MatrixSum.display(), output.display())
    def test_sub(self):
        matrixDiff = self.matrix1 - self.matrix2
        output = matrices([[0, -3, -3], [-1, -10, 1], [2, -2, 4]])
        self.assertEqual(matrixDiff.display(), output.display())
    def test_multiply(self):
        matrixMul = self.matrix1 * self.matrix2
        output = matrices([[10, 54, 25], [8, 48, 29], [33, 173, 77]])
        self.assertEqual(matrixMul.display(), output.display())
    def test_det(self):
        Det = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        det = Det.det([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        output = 3
        self.assertEqual(det, output)
    def test_exponent(self):
        MatrixExpo = self.matrix1 ** self.expo
        output = matrices([[14,25,36],[13,26,36],[44,76,111]])
        self.assertEqual(MatrixExpo.display(), output.display())
    def test_valid(self):
        matrix = matrices([[1,2,3],[3,4,5],[2,3,1]])
        output = [[1,2,3],[3,4,5],[2,3,1]]
        self.assertEqual(matrix.display(),output)
    def test_valid2(self):
        matrix = matrices([[1,2],[3,4,5],[2,3,1]])
        output = False
        self.assertEqual(matrix.display(),output)
    def test_add2(self):
        mat1 = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        mat2 = matrices([[1, 5, 6], [3, 11, 2]])
        mat3 = mat1+mat2
        output = False
        self.assertEqual(mat3.display(),output)
    def test_sub2(self):
        mat1 = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        mat2 = matrices([[1, 5, 6], [3, 11, 2]])
        mat3 = mat1-mat2
        output = False
        self.assertEqual(mat3.display(),output)
    def test_sub2(self):
        mat1 = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        mat2 = matrices([[1, 5, 6], [3, 11, 2]])
        mat3 = mat1*mat2
        output = False
        self.assertEqual(mat3.display(),output)
    

    
    
if __name__ == "__main__":
    unittest.main()
