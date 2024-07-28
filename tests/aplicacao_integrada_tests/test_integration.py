from src.aplicacao_integracao.app import Product, Stock


def  test_add_verify_product():
    stock = Stock()
    product_chocolate = Product("chocolate", 10)
    product_milk = Product("milk", 60)
    
    stock.add_product(product_chocolate)
    stock.add_product(product_milk)
    
    assert stock.verify_quantity(product_chocolate) == 10
    assert stock.verify_quantity(product_milk) == 60
    
    


def  test_add_verify_product_product_existings():
    stock = Stock()
    product_chocolate_10 = Product("chocolate", 10)
    stock.add_product(product_chocolate_10)


    chocolate_milk_60 = Product("chocolate", 60)
    stock.add_product(chocolate_milk_60)

    assert stock.verify_quantity(chocolate_milk_60) == 70