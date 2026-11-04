from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def trova_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query= "SELECT distinct nome FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)
            bibliotche = []
            for row in cursor:
                bibliotche.append(row[0])
            cursor.close()
            cnx.close()
            return bibliotche
        else:
            return None

