from inventory_report.product import Product


def test_product_report() -> None:
    prod_teste = Product(
        "001",
        "produto",
        "empresa",
        "fabricacao",
        "validade",
        "num_serie",
        "armazenar",
    )

    assert prod_teste.__str__() == (
        f"The product {prod_teste.id} - {prod_teste.product_name} "
        f"with serial number {prod_teste.serial_number} "
        f"manufactured on {prod_teste.manufacturing_date} "
        f"by the company {prod_teste.company_name} "
        f"valid until {prod_teste.expiration_date} "
        "must be stored according to the following instructions: "
        f"{prod_teste.storage_instructions}."
    )
