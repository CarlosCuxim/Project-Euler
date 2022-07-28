# ========== Project Euler. Problem #16 =========

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the
# maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
# be solved by brute force, and requires a clever method! ;o)

# -----------------------------------------------

Moves = ["L", "R"]

def ListPermutations(L, k):
    if k ==1:
        return L
    else:
        oldP = ListPermutations(L, k-1)
        newP = []
        for p in oldP:
            for i in L:
                newP.append(p+i)
        return newP

# Función que suma un camino actual
def SumPath(M, Path):
    # Posición inicial
    (i,j) = (0,0)
    S = M[i][j]
    for move in Path:
        if move=="L":
            (i,j) = (i+1, j)
        elif move=="R":
            (i,j) = (i+1, j+1)
        S += M[i][j]
    return S

def GetMaxSumPath(M):
    Paths = ListPermutations(Moves, len(M)-1)
    Max = 0
    for path in Paths:
        S = SumPath(M, path)
        if S>Max:
            Max = S
    return Max

# Preparación
T = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

T = [ line.split(" ") for line in T.splitlines()]
for i in range(len(T)):
    for j in range(len(T[i])):
        T[i][j] = int(T[i][j])

print(f"El la suma máxima de todos los caminos es {GetMaxSumPath(T)}")