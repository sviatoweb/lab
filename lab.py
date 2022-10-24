import csv


def read_matrix(file):
    """
    str -> list
    Reads the given file with matrix and return every row in a list
    """
    with open(file, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        return rows


def write_matrix(rows, file):
    """
    Takes a list of lists, that show every row of a matrix.
    Writes it in the file.
    """
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def reflective(matrix_r):
    """
    str -> str
    Makes reflexive closure from given matrix.
    Writes it in reflective.csv and returns reflective matrix.
    """
    for i in range(len(matrix_r)):
        if matrix_r[i][i]!=1:
            matrix_r[i][i]=1
    write_matrix(matrix_r, 'reflective.csv')
    return matrix_r


def warshall(matrix_t):
    """
    str -> str
    Makes transitive closure from given matrix.
    Writes it in warshall.cvs and returns transitive matrix.
    """
    for k in range(1,len(matrix_t)):
        for i in range(1,len(matrix_t)):
            for j in range(1,len(matrix_t)):    
                matrix_t[i][j]=str(int(matrix_t[i][j]) | (int(matrix_t[i][k])& int(matrix_t[k][j])))
    write_matrix(matrix_t, 'warshall.csv')
    return matrix_t


def symetrical(matrix_s):
    """
    str -> str
    Makes symetrical closure from given matrix.
    Writes it in symetrical.cvs and returns symetrical matrix.
    """
    for i in range(len(matrix_s)):
        for y in range(len(matrix_s[0])):
            if matrix_s[i][y]=='1':
                matrix_s[y][i]='1'
    write_matrix(matrix_s, 'symetrical.csv')
    return matrix_s


def is_transitive(file):
    """
    str -> bool
    Chechk if matrix is transitive.
    """
    given_matrix = read_matrix(file)
    matrix_t = warshall(read_matrix(file))
    if given_matrix == matrix_t:
        return True
    return False
