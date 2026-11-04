import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def generi(self):
        model = Model()
        return model.get_generi()

    def biblioteca(self):
        model = Model()
        return model.get_biblioteche()

    # CALLBACKS DROPDOWN
    #TODO


    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblioteca=self._view.biblioteca.value
        genere = self._view.genere.value
        if biblioteca == "Nessun filtro":
            biblioteca = None
        if genere == "Nessun filtro":
            genere = None
        libri = self._model.get_libri_filtrati(biblioteca, genere)
        self.aggiungi_libri(libri)

    def aggiungi_libri(self, libri):
        self._view.lista.controls.clear()
        for libro in libri:
            self._view.lista.controls.append(ft.Row(
                controls=[ft.Text(f"ID : {libro[0]}", size=15),
                          ft.Text(f"TITOLO : {libro[1]}", size=15),
                        ft.Text(f"AUTORE : {libro[2]}", size=15),
                        ft.Text(f"ANNO : {libro[3]}", size=15)],
                        spacing=25)),
        self._view.update()
        return self._view.lista


