import numpy as np
import copy


def read_matrix(file):
    """
    str -> list
    Reads the given file with matrix and return every row in a list
    """
    with open(file, 'r', encoding='utf-8') as f:
        rows = []
        line = f.readline()
        if line[len(line)-1]=='\n': # removes last \n character
            line=line[:-1]
        for i in range(len(line)): # adds every line as a list to a list
            row = []
            for el in line:
                row.append(el)
            rows.append(row)
            line = f.readline()
            if line=="":
                break
            if line[len(line)-1]=='\n':
                line=line[:-1]
        return rows


def write_matrix(rows, file):
    """
    Takes a list of lists, that show every row of a matrix.
    Writes it in the file.
    """
    with open(file, 'w', newline='', encoding='utf-8') as f:
        for row in rows: # writes every element of a given list to new line
            f.writelines(row)
            f.write('\n')



def reflective(matrix_r):
    """
    str -> str
    Makes reflexive closure from given matrix.
    Writes it in reflective.txt and returns reflective matrix.
    """
    for i in range(len(matrix_r)): # changes every diagonal value of matrix to 1
        if matrix_r[i][i]!='1':
            matrix_r[i][i]='1'
    write_matrix(matrix_r, 'reflective.txt')
    return matrix_r


def warshall(matrix_t):
    """
    str -> str
    Makes transitive closure from given matrix.
    Writes it in warshall.txt and returns transitive matrix.
    """
    for k in range(len(matrix_t)): # algorithm of warshall
        for i in range(len(matrix_t)):
            for j in range(len(matrix_t)):  
                matrix_t[i][j]=str(int(matrix_t[i][j]) | (int(matrix_t[i][k])& int(matrix_t[k][j])))
    write_matrix(matrix_t, 'warshall.txt')
    return matrix_t


def symetrical(matrix_s):
    """
    str -> str
    Makes symetrical closure from given matrix.
    Writes it in symetrical.txt and returns symetrical matrix.
    """
    for i in range(len(matrix_s)): # changes matrix element (y,i) value to value that (i,y) has
        for y in range(len(matrix_s[0])):
            if matrix_s[i][y]=='1':
                matrix_s[y][i]='1'
    write_matrix(matrix_s, 'symetrical.txt')
    return matrix_s


def is_transitive(file):
    """
    str -> bool
    Chechk if matrix is transitive.
    """
    given_matrix = copy.deepcopy(read_matrix(file))
    matrix_t = warshall(read_matrix(file))
    if given_matrix == matrix_t: # compares given matrix to given matrix after warshall algorithm.
        return True              # True means matrix is transitive, False - isn't
    return False

def equvivalent_classes(file):
    """
    str -> list
    Returns all equvivalent_classes of a matrix
    """
    matrix = read_matrix(file)
    classes=[]
    for i in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[i][y]=='1':
                classes_append(i,y,classes)
    classes_list=[]
    for i in range(len(classes)):
        for y in range(len(classes[i])):
            classes[i][y]=classes[i][y]+1
        classes_list.append(set(classes[i]))
    return classes_list


def classes_append(i,y,classes):
    if len(classes)!=0:
        added=0
        for k in range(len(classes)):
            if y in classes[k] or i in classes[k]:
                classes[k].append(y)
                classes[k].append(i)
                added=1
                break
        if added==0:
            classes.append([y])
    else:
        classes.append([i,y])


def matrix_multiplication(matrix):
    """
    list -> list
    Multiplies the matrix by itself
    """
    matrix1=copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for y in range(len(matrix)):
            for k in range(len(matrix)):
                matrix1[i][y]+=matrix[i][k]*matrix[k][y]
    for i in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix1[i][y]>1:
                matrix1[i][y]=1
    return matrix1


def number_of_transitive(n):   
    """
    int -> int
    calculates number of transitive relations on 
    n*n matrix
    results:
    1 - 2
    2 - 13
    3 - 171
    4 - 3994
    5 - 154303
    """
    count=0
    for i in range(2**(n**2)):
        a=2**(n**2)+i
        a=str(bin(a))
        a=a[3:]
        matrix=[]
        for i in range(n):
            helper=list(a[(i*n):((i+1)*(n))])
            helper_1=[]
            for i in range(n):
                helper_1.append(int(helper[i]))
            matrix.append(helper_1)
        matrix1=copy.deepcopy(matrix)
        matrix2=matrix_multiplication(matrix)
        k=0
        for i in range(n):
            for y in range(n):
                if matrix2[i][y]==1 and matrix1[i][y]==0:
                    k=1
                    break
        if k==0:
            count=count+1
    return count
