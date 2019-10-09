link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_page_should_have_add_button(browser):
    browser.get(link)
    add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_button is not None
