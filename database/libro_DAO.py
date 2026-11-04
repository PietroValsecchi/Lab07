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
        cnx = DBConnect.get_connection()
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


    def trova_libro(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = """SELECT l.id, l.titolo, l.autore, l.anno_pubblicazione 
                        FROM biblioteca b, libro l
                        WHERE l.id_biblioteca = b.id AND l.genere = COALESCE(%s, l.genere) AND b.nome = COALESCE(%s, b.nome)"""
            cursor = cnx.cursor()
            cursor.execute(query, (genere, biblioteca))
            risultato = []
            for row in cursor:
                risultato.append(row)
            cursor.close()
            cnx.close()
            return risultato

        else:
            return None



