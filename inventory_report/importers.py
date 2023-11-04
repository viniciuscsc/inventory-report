from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        try:
            with open(self.path, "r") as inventario_json:
                dados_json = json.load(inventario_json)
                produtos = []

                for produto_dict in dados_json:
                    produto = Product(
                        produto_dict["id"],
                        produto_dict["product_name"],
                        produto_dict["company_name"],
                        produto_dict["manufacturing_date"],
                        produto_dict["expiration_date"],
                        produto_dict["serial_number"],
                        produto_dict["storage_instructions"],
                    )

                    produtos.append(produto)

                return produtos

        except FileNotFoundError:
            raise FileNotFoundError("Arquivo não encontrado")


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
