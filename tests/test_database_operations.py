import pytest
import sys
import os

# Ajouter le chemin du dossier parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.database_operations import *
from models.cinema import Cinema

# Fixture pour initialiser la base de données 
# avec des données de test
@pytest.fixture
def setup_database():
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            # Vérifie si l'entrée avec NumCinema=1 existe déjà
            cursor.execute("SELECT COUNT(*) FROM cinema WHERE NumCinema = 1;")
            count = cursor.fetchone()[0]
            if count == 0:
                # Si l'entrée n'existe pas, insère des données de test
                cursor.execute("INSERT INTO cinema (NumCinema, NomCinema, RueCinema) VALUES (1, 'CinemaTest', 'RueTest');")
                mydb.commit()

# Test la fonction select_all ...
def test_select_all(setup_database):
    results = select_all()
    assert len(results) > 0
    assert isinstance(results[0], tuple)

# Test la fonction insert_cinema
def test_insert_cinema(setup_database):
    cinema_ajout: Cinema = Cinema(None, "NouveauCinema", "Rue1")
    num = insert_cinema(cinema_ajout)

    # Vérifie que le cinéma a bien été inséré
    selected_cinema = select_by_id(num)
    assert selected_cinema is not None
    assert selected_cinema[1] == "NouveauCinema"
    assert selected_cinema[2] == "Rue1"

# Test la fonction update_cinema
def test_update_cinema(setup_database):
    cinema_edit: Cinema = Cinema(1, "NouveauCinema", "Rue11111")
    update_cinema(cinema_edit)

    # Vérifie que le cinéma a bien été mis à jour
    updated_cinema = select_by_id(1)
    assert updated_cinema is not None
    assert updated_cinema[1] == "NouveauCinema"
    assert updated_cinema[2] == "Rue11111"

# Test la fonction delete_cinema
def test_delete_cinema(setup_database):
    num_cinema = 1
    delete_cinema(num_cinema)

    # Vérifie que le cinéma a bien été supprimé
    deleted_cinema = select_by_id(num_cinema)
    assert deleted_cinema is None