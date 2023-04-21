############################################################################################################################################################
####################################################### CREATION D'UN MINI JEU : LE MORPION ################################################################
############################################################################################################################################################

# Importation de mes bibliothèques
from tkinter import *
from tkinter import messagebox
import tkmacosx as tkm

# Créer une fenêtre
fenetre = Tk()
fenetre.title("Tic Tac Toe")

# Créer un canvas pour la grille
canvas = Canvas(fenetre, width=300, height=300, bg="black")
canvas.pack()

# Dessiner les lignes dorées pour faire un grillage
canvas.create_line(100, 0, 100, 300, fill="saddlebrown", width=2)
canvas.create_line(200, 0, 200, 300, fill="saddlebrown", width=2)
canvas.create_line(0, 100, 300, 100, fill="saddlebrown", width=2)
canvas.create_line(0, 200, 300, 200, fill="saddlebrown", width=2)

# Variable qui definit le joueur actif (X commence ensuite c'est 0)
current_player = "X"

# Liste pour stocker l'état de la grille
grille = [["", "", ""],
          ["", "", ""],
          ["", "", ""]]

# Fonction pour detecter le clic de souris
def on_canvas_click(event):
    row = event.y // 100
    col = event.x // 100
    add_symbol(row, col)
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"    
canvas.bind("<Button-1>",on_canvas_click)

# Fonction pour ajouter un symbole X ou O à une case de la grille
def add_symbol(row, col):
    x = col * 100 + 50
    y = row * 100 + 50
    if current_player == "X" and grille[row][col] == "":
        canvas.create_text(x, y, text="X", font=("Bodoni 72", 50, "bold"), fill="darkgoldenrod")
    elif current_player == "O" and grille[row][col] == "":
        canvas.create_text(x, y, text="O", font=("Bodoni 72", 50, "bold"), fill="darkgoldenrod")
    grille[row][col] = current_player
    
    check_winner()    

# Fonction pour reinitialiser
def restart_game():
    global grille
    global current_player
    grille = [["", "", ""],
              ["", "", ""],
              ["", "", ""]]
    canvas.delete("all") # Effacer la grille
    
    canvas.create_line(100, 0, 100, 300, fill="saddlebrown", width=2)
    canvas.create_line(200, 0, 200, 300, fill="saddlebrown", width=2)
    canvas.create_line(0, 100, 300, 100, fill="saddlebrown", width=2)
    canvas.create_line(0, 200, 300, 200, fill="saddlebrown", width=2)

# Fonction pour fermer la fenetre
def close_window():                                                           
    fenetre.destroy()    
    
# Création d'un bouton d'échappatoire
quick_button = tkm.Button(fenetre, text="Se nachave", font=("Bodoni 72", 15, "bold"), bg="darkgoldenrod", command=close_window)
quick_button.pack(side="left")

# Création d'un bouton pour rejouer une nouvelle partie
reset_button = tkm.Button(fenetre, text="Try again", font=("Bodoni 72", 15, "bold"), bg="darkgoldenrod", command=restart_game)
reset_button.pack(side="right")

# Fonction pour vérifier s'il y a un gagnant
def check_winner():
       
    # Vérifier les combinaisons gagnantes horizontales
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "" and current_player == "X":
            show_winner_after_time()
            return True

    # Vérifier les combinaisons gagnantes verticales
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] != "" and current_player == "X":
            show_winner_after_time()
            return True

    # Vérifier la combinaison gagnante diagonale haut gauche - bas droite
    if grille[0][0] == grille[1][1] == grille[2][2] != "" and current_player == "X":
        show_winner_after_time()
        return True

    # Vérifier la combinaison gagnante diagonale bas gauche - haut droite
    if grille[2][0] == grille[1][1] == grille[0][2] != "" and current_player == "X":
        show_winner_after_time()
        return True
    
       # Vérifier les combinaisons gagnantes horizontales
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "" and current_player == "O":
            show_winner_after_time()
            return True

    # Vérifier les combinaisons gagnantes verticales
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] != "" and current_player == "O":
            show_winner_after_time()
            return True

    # Vérifier la combinaison gagnante diagonale haut gauche - bas droite
    if grille[0][0] == grille[1][1] == grille[2][2] != "" and current_player == "O":
        show_winner_after_time()
        return True

    # Vérifier la combinaison gagnante diagonale bas gauche - haut droite
    if grille[2][0] == grille[1][1] == grille[0][2] != "" and current_player == "O":
        show_winner_after_time()
        return True

    # Vérifier s'il y a égalité (match nul)
    if is_game_draw():
        show_draw()
        return False
    
# Fonction pour vérifier s'il y a égalité
def is_game_draw():
    global grille
    for row in grille:
        for symbol in row:
            if symbol == "":
                return False
    return True     

# Fonction pour afficher le message de match nul
def show_draw():
    messagebox.showinfo(fenetre, (current_player) + " Personne " + " n'a gagné : C'est un match nul")

# Fonction qui permet d'ajouter un délai de 100ms avant de verifier la victoire 
def show_winner_after_time():
    canvas.after(100,show_winner)

# Fonction qui affiche un message personnalisé au joueur qui gagne
def show_winner():
    messagebox.showinfo(fenetre, "Le joueur " + (current_player) + " n'a pas gagné : C'est l'autre tocardo !!!!!")

fenetre.mainloop()