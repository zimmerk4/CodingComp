def transpose(mat):
    return [list(i) for i in zip(*mat)]


def parse(str):
    """Parses string and outputs list of matrices in array form"""
    mat = []
    for row in str.strip().split(";"):
        mat.append([int(i) for i in row.split(",")])
    return mat


def is_symmetric(mat):
    if mat == transpose(mat):
        print("Symmetric")
    else:
        print("Not symmetric")
    return

with open("matsub.txt") as mat:
    for line in mat:
        is_symmetric(parse(line))
    print() # Practice needed blank line??


