from inventory_report.product import Product


def test_create_product() -> None:
    produto_teste = Product(
        "id",
        "produto",
        "empresa",
        "data_fabricacao",
        "data_vencimento",
        "numero_serie",
        "instrucao_armazenamento",
    )

    assert produto_teste.id == "id"
    assert produto_teste.product_name == "produto"
    assert produto_teste.company_name == "empresa"
    assert produto_teste.manufacturing_date == "data_fabricacao"
    assert produto_teste.expiration_date == "data_vencimento"
    assert produto_teste.serial_number == "numero_serie"
    assert produto_teste.storage_instructions == "instrucao_armazenamento"
