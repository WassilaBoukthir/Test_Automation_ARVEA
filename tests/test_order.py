

def test_order_creation(driver):
    # Données de test
    USER = "TN25000000"
    PASS = "maisonduweb123"
    PRODUCT = "20122"
    
    # Execution
    driver.get("https://recrutement.arvea-test.ovh")
    
    # Login 
    driver.find_element("id", "username").send_keys(USER)
    driver.find_element("id", "password").send_keys(PASS)
    driver.find_element("id", "login-btn").click()
    
    # Commande
    from pages.order_page import OrderPage
    order = OrderPage(driver)
    order.create_order(PRODUCT, 5)
    
    # Vérification basique
    assert "succès" in driver.page_source.lower()
    
    