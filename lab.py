import csv


def read_matrix(file):
    with open(file, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        return rows


def write_matrix(rows, file):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


matrix=read_matrix("matrix.csv")
def reflective(matrix_r):
    for i in range(len(matrix_r)):
        if matrix_r[i][i]!=1:
            matrix_r[i][i]=1
    write_matrix(matrix_r, 'reflective.csv')

def warshall(matrix_t):
    for k in range(1,len(matrix_t)):
        for i in range(1,len(matrix_t)):
            for j in range(1,len(matrix_t)):    
                matrix_t[i][j]=str( int(matrix_t[i][j]) | (int(matrix_t[i][k]) & int(matrix_t[k][j]) ))
    write_matrix(matrix_t, 'warshall.csv')

warshall(matrix)
def symetrical(matrix_s):
    for i in range(len(matrix_s)):
        for y in range(len(matrix_s[0])):
            if matrix_s[i][y]=='1':
                matrix_s[y][i]='1'
    write_matrix(matrix_s, 'symetrical.csv')
