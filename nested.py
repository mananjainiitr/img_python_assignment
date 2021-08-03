import unittest
class matrices:
    mat = []
    a = []
    det =[]
    def __init__(self,x):
        self.mat = x
        print (self.mat)
    def display(self):
        for i in self.mat:
            print(i)
    # def __str__(self):
    #     string = ','.join([str(elem) for elem in self.mat])
    #     return string
    def __add__(self,other):
         a = matrices([])
         a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(other.mat)) ]
         for i in range(len(other.mat)):
            for j in range(len(other.mat[0])):
                a.mat[i][j] = self.mat[i][j]+(other.mat[i][j]) 
         return a
    def __sub__(self,other):
         a = matrices([])
         a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(other.mat)) ]
         for i in range(len(other.mat)):
            for j in range(len(other.mat[0])):
                a.mat[i][j] = self.mat[i][j]-(other.mat[i][j]) 
         return a
    def __mul__(self,other):
        a = matrices([])
        a.mat = [ [ 0 for i in range(len(other.mat[0])) ] for j in range(len(self.mat)) ]
        for i in range(len(a.mat)):
            for j in range(len(a.mat[0])):
                sum = 0
                for k in range(len(self.mat[0])):
                     sum = sum + self.mat[i][k]*other.mat[k][j]
                a.mat[i][j] = sum
        return a
    def det(self,matrix):
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
             
                        
                # sum = sum + ((-1).pow(j+1))*det()
                # print (m)
    def __pow__(self,other,modulo = None):
         obj1 = matrices([])
         obj1.mat = self.mat
         for i in range(other-1):
            obj1 = obj1 * self
         return obj1

        


class Test(unittest.TestCase):

    def setUp(self):
        self.Matrix1 = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        self.Matrix2 = matrices([[1, 5, 6], [3, 11, 2], [1, 9, 5]])
        self.expo = 2

    def tearDown(self):
        print("\n")

    def test_add(self):
        MatrixSum = self.Matrix1 + self.Matrix2
        output = matrices([[2, 7, 9], [5, 12, 5], [4, 16, 14]])
        self.assertEqual(MatrixSum.display(), output.display())
    def test_sub(self):
        MatrixDiff = self.Matrix1 - self.Matrix2
        output = matrices([[0, -3, -3], [-1, -10, 1], [2, -2, 4]])
        self.assertEqual(MatrixDiff.display(), output.display())
    def test_multiply(self):
        MatrixMul = self.Matrix1 * self.Matrix2
        output = matrices([[10, 54, 25], [8, 48, 29], [33, 173, 77]])
        self.assertEqual(MatrixMul.display(), output.display())
    def test_det(self):
        Det = matrices([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        det = Det.det([[1, 2, 3], [2, 1, 3], [3, 7, 9]])
        output = 3
        self.assertEqual(det, output)
    def test_exponent(self):
        MatrixExpo = self.Matrix1 ** self.expo
        output = matrices([[14,25,36],[13,26,36],[44,76,111]])
        self.assertEqual(MatrixExpo.display(), output.display())
    
if __name__ == "__main__":
    unittest.main()