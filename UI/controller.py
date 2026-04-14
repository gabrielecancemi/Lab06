import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def topVendite(self, e):
        self._view.txt_result.controls.clear()

        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value

        if anno is None:
            self._view.create_alert("Inserire l'anno")
            return
        if brand is None:
            self._view.create_alert("Inserire il brand")
            return
        if self._retailer is None:
            self._view.create_alert("Inserire il retailer")
            return

        vendite = self._model.topVendite(anno, brand, self._retailer)

        if len(vendite) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita", color='red'))


        for v in vendite:
            self._view.txt_result.controls.append(ft.Text(v))

        self._view.update_page()

    def analizzaVendite(self, e):
        self._view.txt_result.controls.clear()

        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value

        if anno is None:
            self._view.create_alert("Inserire l'anno")
            return
        if brand is None:
            self._view.create_alert("Inserire il brand")
            return
        if self._retailer is None:
            self._view.create_alert("Inserire il retailer")
            return

        affari, numero, v, p = self._model.analizzaVendite(anno, brand, self._retailer)

        str = f"""Statistiche vendite:\n
        Giro d'affari: {affari}\n
        Numero vendite: {numero}\n
        Numero retailers coinvolti: {v}\n
        Numero prodotti coinvolti: {p}"""


        self._view.txt_result.controls.append(ft.Text(str))

        self._view.update_page()

    def riempiAnni(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(a))

    def riempiBrands(self):
        brands = self._model.getBrands()
        for b in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(b))

    def riempiRetailers(self):
        retailers = self._model.getRetailers()
        retailers.sort(key=lambda x:x.Retailer_name)
        for r in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=r.Retailer_code, text=r.Retailer_name, data=r, on_click=self.read_retailer))

    def read_retailer(self, e):
        self._retailer = e.control.data