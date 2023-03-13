import os

def trouver_chemin_cavalier(n, depart):
    plateau = [[-1] * n for _ in range(n)]
    mouvements = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    x, y = depart
    plateau[x][y] = 0
    def trouver_chemin_recursif(x, y, prochain):
        if prochain == n**2:
            return True
        for dx, dy in mouvements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and plateau[nx][ny] == -1:
                plateau[nx][ny] = prochain
                if trouver_chemin_recursif(nx, ny, prochain+1):
                    return True
                plateau[nx][ny] = -1
        return False
    if trouver_chemin_recursif(x, y, 1):
        return plateau
    else:
        return None
    
    
def afficher(solution):
    if solution is None:
        print("Aucune solution n'a été trouvée.")
        return
    n = len(solution)
    for i in range(n):
        for j in range(n):
            print(str(solution[i][j]).rjust(2), end=' ')
        print()
        
        
        
taille = input("Veuillez me donner la taille de votre plateau:")
taille = int(taille)

x = input("Donnez le point x de départ :")
x = int(x)

y = input("Donnez le point y de départ :")
y = int(y)
solution = trouver_chemin_cavalier(taille, (x, y))
# Afficher la solution
afficher(solution)