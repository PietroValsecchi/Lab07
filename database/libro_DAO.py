from database.DB_connect import DBConnect
from model.libro_DTO import Libro
from UI.alert import AlertManager

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def trova_generi(self):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            query = "SELECT distinct genere FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            generi = []
            for row in cursor:
                generi.append(row[0])

            cursor.close()
            cnx.close()
            return generi

        else:
            return None

