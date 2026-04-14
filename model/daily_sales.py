from dataclasses import dataclass
from datetime import datetime


@dataclass
class Daily_sales:
    Retailer_code: int
    Product_number: int
    Date: datetime
    ricavo: float

    def __str__(self):
        return f"Data: {self.Date}; Ricavo: {self.ricavo}; Retailer: {self.Retailer_code}; Product: {self.Product_number}"

