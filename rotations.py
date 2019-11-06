#fichier de test pour la présentation orale

grid = [[0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],[0, 0, 0, 1, 0, 0]]
n = len(grid)
def rotation(grid, n):
    necle = []
    for i in range(n):
        necle.append([])
        for j in range(n):
            necle[i].append(0)
    for i in range (n):
        for j in range(n):
            x=n-i-1
            necle[j][x]=grid[i][j]

    return necle

def tourne(grid, n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()


print("clé par défaut :")
print()
for d in range(n):
    for e in range(n):
        print(grid[d][e], end=" ")
    print()

print()

for k in range(1,5):
    grid = rotation(grid,n)
    print()
    print("rotation ", k)
    print()
    tourne(grid,n)