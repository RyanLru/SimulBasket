import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Base de données de l'équipe de basket")

# Connexion à la base de données
conn = sqlite3.connect("Basketball.db")
cursor = conn.cursor()
# Déclaration de la variable treeview en tant que variable globale
treeview = None

# Fonction pour récupérer et afficher les données des joueurs
def afficher_joueurs():
    global treeview  # Utilisation de la variable globale treeview

    # Effacer les données précédentes
    for widget in frame.winfo_children():
        widget.destroy()

    # Récupérer les données des joueurs
    cursor.execute("SELECT * FROM Joueurs")
    joueurs = cursor.fetchall()

    # Créer le tableau pour afficher les joueurs
    treeview = ttk.Treeview(frame, columns=list(range(1, 20)), show="headings")
    treeview.pack(side="left", fill="both", expand=True)

    # Configurer les options de mise en page pour le tableau
    treeview.columnconfigure(0, weight=1)
    treeview.rowconfigure(0, weight=1)

    # Ajouter les en-têtes des colonnes
    for i, col in enumerate(
        [
            "ID",
            "Équipe ID",
            "Nom",
            "Prénom",
            "Taille",
            "Poids",
            "Poste",
            "Vitesse",
            "Agilité",
            "Force",
            "Précision",
            "Endurance",
            "Moral",
            "Santé",
            "Équipe",
            "Coord X",
            "Coord Y",
            "Coord Z",
            "Photo Path",
        ],
        start=1,
    ):
        treeview.heading(i, text=col)

    # Ajouter les données dans les lignes
    for joueur in joueurs:
        treeview.insert("", "end", values=joueur)

    # Associer la fonction afficher_details_joueur à un clic sur une ligne du tableau
    treeview.bind("<ButtonRelease-1>", afficher_details_joueur)

# Fonction pour afficher les détails d'un joueur avec sa photo
def afficher_details_joueur(event):
    # Récupérer l'indice de la ligne sélectionnée
    item = treeview.focus()
    joueur = treeview.item(item)["values"]

    # Créer une fenêtre pour afficher les détails du joueur
    fenetre_joueur = Toplevel()
    fenetre_joueur.title("Détails du joueur")

    # Afficher les détails du joueur
    for i, label_text in enumerate(
        [
            "ID:",
            "Équipe ID:",
            "Nom:",
            "Prénom:",
            "Taille:",
            "Poids:",
            "Poste:",
            "Vitesse:",
            "Agilité:",
            "Force:",
            "Précision:",
            "Endurance:",
            "Moral:",
            "Santé:",
            "Équipe:",
            "Coord X:",
            "Coord Y:",
            "Coord Z:",
        ],
        start=0,
    ):
        label = Label(fenetre_joueur, text=label_text)
        label.grid(row=i, column=0, sticky="e", padx=0, pady=5)

        value_label = Label(fenetre_joueur, text=joueur[i])
        value_label.grid(row=i, column=1, sticky="w", padx=0, pady=5)

    # Afficher la photo du joueur
    photo_path = joueur[-1]
    image = Image.open(photo_path)
    image = image.resize((400, 300))
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(fenetre_joueur, image=photo)
    photo_label.grid(row=0, column=2, rowspan=18, padx=10, pady=10)
    fenetre_joueur.mainloop()

# Fonction pour afficher les équipes
def afficher_equipes():
    global treeview
    # Effacer les données précédentes
    for widget in frame.winfo_children():
        widget.destroy()

    # Récupérer les données des équipes
    cursor.execute("SELECT * FROM Equipes")
    equipes = cursor.fetchall()

    # Créer le tableau pour afficher les équipes
    treeview = ttk.Treeview(frame, columns=list(range(1, 4)), show="headings")
    treeview.pack(side="left", fill="both", expand=True)

    # Configurer les options de mise en page pour le tableau
    treeview.columnconfigure(0, weight=1)
    treeview.rowconfigure(0, weight=1)

    # Ajouter les en-têtes des colonnes
    for i, col in enumerate(["ID", "Nom de l'équipe", "Photo de l'équipe"], start=1):
        treeview.heading(i, text=col)

    # Ajouter les données dans les lignes
    for equipe in equipes:
        treeview.insert("", "end", values=equipe)

    # Associer la fonction afficher_details_equipe à un clic sur une ligne du tableau
    treeview.bind("<ButtonRelease-1>", afficher_details_equipe)

# Fonction pour afficher les détails d'une équipe avec sa photo
def afficher_details_equipe(event):
    # Récupérer l'indice de la ligne sélectionnée
    item = treeview.focus()
    equipe = treeview.item(item)["values"]

    # Créer une fenêtre pour afficher les détails de l'équipe
    fenetre_equipe = Toplevel()
    fenetre_equipe.title("Détails de l'équipe")

    # Afficher les détails de l'équipe
    for i, label_text in enumerate(["ID:", "Nom de l'équipe:"], start=0):
        label = Label(fenetre_equipe, text=label_text)
        label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

        value_label = Label(fenetre_equipe, text=equipe[i])
        value_label.grid(row=i, column=1, sticky="w", padx=5, pady=5)

    # Afficher la photo de l'équipe
    photo_path = equipe[-1]
    image = Image.open(photo_path)
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(fenetre_equipe, image=photo)
    photo_label.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
    fenetre_equipe.mainloop()

# Création des boutons
button_joueurs = Button(fenetre, text="Afficher les joueurs", command=afficher_joueurs)
button_joueurs.pack(pady=10)

button_equipes = Button(fenetre, text="Afficher les équipes", command=afficher_equipes)
button_equipes.pack(pady=10)


# Création du cadre pour le tableau
frame = Frame(fenetre)
frame.pack(padx=10, pady=10)
fenetre.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
