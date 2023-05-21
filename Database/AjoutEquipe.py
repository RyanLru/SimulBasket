import sqlite3
from tkinter import *

# Fonction pour ajouter une équipe
def ajouter_equipe():
    nom_equipe = entry_nom_equipe.get()
    photo_equipe = entry_photo_equipe.get()

    # Insérer les données de l'équipe dans la base de données
    cursor.execute("INSERT INTO Equipes (nom, equipe_photo_path) VALUES (?, ?)", (nom_equipe, photo_equipe))
    conn.commit()

    # Afficher un message de succès
    label_message.config(text="L'équipe a été ajoutée avec succès.")

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Ajouter une équipe")

# Connexion à la base de données
conn = sqlite3.connect("Basketball.db")
cursor = conn.cursor()

# Création des widgets
label_nom_equipe = Label(fenetre, text="Nom de l'équipe:")
label_nom_equipe.pack()

entry_nom_equipe = Entry(fenetre)
entry_nom_equipe.pack()

label_photo_equipe = Label(fenetre, text="Chemin de la photo de l'équipe:")
label_photo_equipe.pack()

entry_photo_equipe = Entry(fenetre)
entry_photo_equipe.pack()

button_ajouter = Button(fenetre, text="Ajouter l'équipe", command=ajouter_equipe)
button_ajouter.pack()

label_message = Label(fenetre, text="")
label_message.pack()

# Boucle principale Tkinter
fenetre.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
