import sqlite3
from tkinter import *

# Fonction pour ajouter un joueur
def ajouter_joueur():
    id_equipe = entry_id_equipe.get()
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    taille = entry_taille.get()
    poids = entry_poids.get()
    poste = entry_poste.get()
    vitesse = entry_vitesse.get()
    agilite = entry_agilite.get()
    force = entry_force.get()
    precision = entry_precision.get()
    endurance = entry_endurance.get()
    moral = entry_moral.get()
    sante = entry_sante.get()
    equipe = entry_equipe.get()
    coord_x = 0
    coord_y = 0
    coord_z = 0
    repertoire_photo = entry_repertoire_photo.get()

    # Insérer les données du joueur dans la base de données
    cursor.execute("INSERT INTO Joueurs (equipe_id, nom, prenom, taille, poids, poste, vitesse, agilite, force, precision, "
                   "endurance, moral, sante, equipe, coord_x, coord_y, coord_z, photo_path) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id_equipe, nom, prenom, taille, poids, poste, vitesse, agilite, force, precision, endurance,
                    moral, sante, equipe, coord_x, coord_y, coord_z, repertoire_photo))
    conn.commit()

    # Afficher un message de succès
    label_message.config(text="Le joueur a été ajouté avec succès.")

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Ajouter un joueur")

# Connexion à la base de données
conn = sqlite3.connect("Basketball.db")
cursor = conn.cursor()

# Récupérer les équipes existantes depuis la base de données
cursor.execute("SELECT ID, nom FROM Equipes")
equipes = cursor.fetchall()

# Création des widgets pour le formulaire d'ajout de joueur
label_nom = Label(fenetre, text="Nom:")
label_nom.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry_nom = Entry(fenetre)
entry_nom.grid(row=0, column=1, padx=5, pady=5)

entry_prenom = Entry(fenetre)
entry_prenom.grid(row=1, column=1, padx=5, pady=5)

label_prenom = Label(fenetre, text="Prénom:")
label_prenom.grid(row=1, column=0, sticky="e", padx=5, pady=5)

label_id_equipe = Label(fenetre, text="ID de l'équipe:")
label_id_equipe.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_id_equipe = Entry(fenetre)
entry_id_equipe.grid(row=2, column=1, padx=5, pady=5)

label_taille = Label(fenetre, text="Taille:")
label_taille.grid(row=3, column=0, sticky="e", padx=5, pady=5)

entry_taille = Entry(fenetre)
entry_taille.grid(row=3, column=1, padx=5, pady=5)

label_poids = Label(fenetre, text="Poids:")
label_poids.grid(row=4, column=0, sticky="e", padx=5, pady=5)

entry_poids = Entry(fenetre)
entry_poids.grid(row=4, column=1, padx=5, pady=5)

label_poste = Label(fenetre, text="Poste:")
label_poste.grid(row=5, column=0, sticky="e", padx=5, pady=5)

entry_poste = Entry(fenetre)
entry_poste.grid(row=5, column=1, padx=5, pady=5)

label_vitesse = Label(fenetre, text="Vitesse:")
label_vitesse.grid(row=6, column=0, sticky="e", padx=5, pady=5)

entry_vitesse = Entry(fenetre)
entry_vitesse.grid(row=6, column=1, padx=5, pady=5)

label_agilite = Label(fenetre, text="Agilité:")
label_agilite.grid(row=7, column=0, sticky="e", padx=5, pady=5)

entry_agilite = Entry(fenetre)
entry_agilite.grid(row=7, column=1, padx=5, pady=5)

label_force = Label(fenetre, text="Force:")
label_force.grid(row=8, column=0, sticky="e", padx=5, pady=5)

entry_force = Entry(fenetre)
entry_force.grid(row=8, column=1, padx=5, pady=5)

label_precision = Label(fenetre, text="Précision:")
label_precision.grid(row=9, column=0, sticky="e", padx=5, pady=5)

entry_precision = Entry(fenetre)
entry_precision.grid(row=9, column=1, padx=5, pady=5)

label_endurance = Label(fenetre, text="Endurance:")
label_endurance.grid(row=10, column=0, sticky="e", padx=5, pady=5)

entry_endurance = Entry(fenetre)
entry_endurance.grid(row=10, column=1, padx=5, pady=5)

label_moral = Label(fenetre, text="Moral:")
label_moral.grid(row=11, column=0, sticky="e", padx=5, pady=5)

entry_moral = Entry(fenetre)
entry_moral.grid(row=11, column=1, padx=5, pady=5)

label_sante = Label(fenetre, text="Santé:")
label_sante.grid(row=12, column=0, sticky="e", padx=5, pady=5)

entry_sante = Entry(fenetre)
entry_sante.grid(row=12, column=1, padx=5, pady=5)

label_equipe = Label(fenetre, text="Équipe:")
label_equipe.grid(row=13, column=0, sticky="e", padx=5, pady=5)

entry_equipe = Entry(fenetre)
entry_equipe.grid(row=13, column=1, padx=5, pady=5)

button_ajouter = Button(fenetre, text="Ajouter le joueur", command=ajouter_joueur)
button_ajouter.grid(row=17, columnspan=2, padx=5, pady=10)

label_message = Label(fenetre, text="")
label_message.grid(row=18, columnspan=2, padx=5, pady=5)

label_repertoire_photo = Label(fenetre, text="Répertoire de la photo:")
label_repertoire_photo.grid(row=14, column=0, sticky="e", padx=5, pady=5)

entry_repertoire_photo = Entry(fenetre)
entry_repertoire_photo.grid(row=14, column=1, padx=5, pady=5)

# Boucle principale Tkinter
fenetre.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
