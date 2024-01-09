import mysql.connector
from models.cinema import Cinema

# Fonction pour se connecter à la base de données
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3308,
        database="cinemas"
    )

# Fonction pour effectuer une requête SELECT spécifique
def select_specific_cols():
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = "SELECT NumCinema, NomCinema, RueCinema FROM cinema;"
            cursor.execute(query)
            return cursor.fetchall()

# Fonction pour effectuer une opération d'insertion
def insert_cinema(cinema: Cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"INSERT INTO cinema (NomCinema, RueCinema) VALUES ('{cinema.nom_cinema}', '{cinema.rue_cinema}');"
            cursor.execute(query)
            mydb.commit()
            last_inserted_id = cursor.lastrowid

    return last_inserted_id

# Fonction pour effectuer une opération de mise à jour
def update_cinema(cinema: Cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"UPDATE cinema SET NomCinema = '{cinema.nom_cinema}', RueCinema = '{cinema.rue_cinema}' WHERE NumCinema = {cinema.num_cinema};"
            cursor.execute(query)
            mydb.commit()

# Fonction pour effectuer une requête SELECT par ID
def select_by_id(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"SELECT NumCinema, NomCinema, RueCinema FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            return cursor.fetchone()

# Fonction pour effectuer une opération de suppression
def delete_cinema(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"DELETE FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            mydb.commit()

