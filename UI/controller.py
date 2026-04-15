import flet as ft

from model import retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def carica_anno(self):
        anni=self._model.get_Anni()
        self._view._dd_anno.options.append(ft.dropdown.Option("Nessun filtro"))
        for a in anni:
            self._view._dd_anno.options.append(ft.dropdown.Option(str(a)))
        self._view.update_page()

    def carica_brand(self):
        brand=self._model.get_Brand()
        self._view._dd_brand.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in brand:
            self._view._dd_brand.options.append(ft.dropdown.Option(str(b)))
        self._view.update_page()

    def carica_retail(self):
        retail=self._model.get_Retail()
        self._view._dd_retailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for r in retail:
            self._view._dd_retailer.options.append((ft.dropdown.Option(key=
                r.codice,
                text=r.nome,
                data=r, on_click=self.read_retailer)))
        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = e.control.data



    def handle_topVendite(self, e):
       pass

    def handle_analizzavendite(self,e):
        pass
