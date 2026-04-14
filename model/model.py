from collections import Counter

from database.DAO import DAO
from model.retailer import Retailer


class Model:
    def __init__(self):
        pass

    def getAnni(self):
        return DAO.getAnni()

    def getBrands(self):
        return DAO.getBrands()

    def getRetailers(self):
        return DAO.getRetailers()

    def topVendite(self, anno, brand, retailer):
        if anno == "Nessun filtro":
            anno = None
        if brand == "Nessun filtro":
            brand = None
        if not isinstance(retailer, Retailer) and retailer == "Nessun filtro":
            retailer = None
        else:
            retailer = retailer.Retailer_code

        vendite = DAO.getVendite(anno, brand, retailer)

        vendite.sort(key=lambda x: x.ricavo, reverse=True)

        if len(vendite) > 5:
            res = vendite[0:5]
        else:
            res = vendite

        return res

    def analizzaVendite(self, anno, brand, retailer):
        if anno == "Nessun filtro":
            anno = None
        if brand == "Nessun filtro":
            brand = None
        if not isinstance(retailer, Retailer) and retailer == "Nessun filtro":
            retailer = None
        else:
            retailer = retailer.Retailer_code

        vendite = DAO.getVendite(anno, brand, retailer)



        affari = sum(v.ricavo for v in vendite)
        venditori = [v.Retailer_code for v in vendite]
        prodotti = [v.Product_number for v in vendite]
        numero = len(vendite)

        v = len(Counter(venditori))
        p = len(Counter(prodotti))



        return affari, numero, v, p