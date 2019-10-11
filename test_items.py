import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    # ищем кнопку корзины
    assert browser.find_element_by_css_selector("button.btn-add-to-basket").text == "Añadir al carrito", "Button should be called 'Añadir al carrito' for 'es' parameter"
