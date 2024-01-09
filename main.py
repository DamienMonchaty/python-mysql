from models.cinema import Cinema
from data.database_operations import select_specific_cols, insert_cinema, update_cinema, select_by_id, delete_cinema

# Exemple d'utilisation
results = select_specific_cols()
print("Résultats de la requête SELECT :")
for res in results:
    print(res)

# Exemple d'insertion
cinema_ajout: Cinema = Cinema(None, "NouveauCinema", "Rue1")
insert_cinema(cinema_ajout)

# Exemple de mise à jour
cinema_edit: Cinema = Cinema(7, "NouveauCinema", "Rue11111")
update_cinema(cinema_edit)

# Exemple de sélection par ID
selected_cinema = select_by_id(7)
print(f"Sélection du cinéma avec ID 7 : {selected_cinema}")

# Exemple de suppression
delete_cinema(6)
print("Cinéma avec ID 6 supprimé.")