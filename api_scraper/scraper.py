import requests
from bs4 import BeautifulSoup


def search_mercadolivre_by_category(category):
    url = f"https://lista.mercadolivre.com.br/{category}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all("li", {"class": "ui-search-layout__item"})
    results = []
    for product in products:
        title = product.find("h2", {"class": "ui-search-item__title"}).text.strip()
        price = product.find("span", {"class": "price-tag-fraction"}).text.strip()
        link = product.find("a", {"class": "ui-search-link"})['href']
        image = product.find("img")['src']
        results.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image,
            "category": category,
            "website": "Mercado Livre",
            "keyword": ""
        })
    return results


def search_mercadolivre_by_keyword(category, keyword):
    url = f"https://lista.mercadolivre.com.br/{category}/{keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all("li", {"class": "ui-search-layout__item"})
    results = []
    for product in products:
        title = product.find("h2", {"class": "ui-search-item__title"}).text.strip()
        price = product.find("span", {"class": "price-tag-fraction"}).text.strip()
        link = product.find("a", {"class": "ui-search-link"})['href']
        image = product.find("img")['src']
        results.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image,
            "category": category,
            "website": "Mercado Livre",
            "keyword": keyword
        })
    return results


def search_buscape_by_category(category):
    url = f"https://www.buscape.com.br/{category}"
    # fazer request e parsear html
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # obter produtos
    products = soup.find_all("div", {"class": "SearchCard_ProductCard__1D3ve"})

    results = []

    for product in products:
        # obter informações do produto
        title = product.find("h2", {"class": "Text_Text__h_AF6"}).text.strip()
        price = product.find("p", {"class": "Text_Text__h_AF6"}).text.strip()
        link = product.find("a", {"class": "SearchCard_ProductCard_Inner__7JhKb"})['href']
        image = product.find("img")['src']

        results.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image,
            "category": category,
            "website": "Buscapé",
            "keyword": ""
        })

    return results


def search_buscape_by_keyword(category, keyword):
    url = f"https://www.buscape.com.br/{category}/{keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # obter produtos
    products = soup.find_all("div", {"class": "SearchCard_ProductCard__1D3ve"})

    results = []

    for product in products:
        # obter informações do produto
        title = product.find("h2", {"class": "Text_Text__h_AF6"}).text.strip()
        price = product.find("p", {"class": "Text_Text__h_AF6"}).text.strip()
        link = product.find("a", {"class": "SearchCard_ProductCard_Inner__7JhKb"})['href']
        image = product.find("img")['src']

        results.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image,
            "category": category,
            "website": "Buscapé",
            "keyword": ""
        })

    return results


def search_all(category, keyword=None):
    # Busca no Mercado Livre por categoria
    mercadolivre_category_results = search_mercadolivre_by_category(category)

    # Busca no Mercado Livre por palavra-chave, se especificada
    if keyword:
        mercadolivre_keyword_results = search_mercadolivre_by_keyword(category, keyword)
        mercadolivre_results = mercadolivre_category_results + mercadolivre_keyword_results
    else:
        mercadolivre_results = mercadolivre_category_results

    # Busca no Buscapé por categoria
    buscape_category_results = search_buscape_by_category(category)

    # Busca no Buscapé por palavra-chave, se especificada
    if keyword:
        buscape_keyword_results = search_buscape_by_keyword(category, keyword)
        buscape_results = buscape_category_results + buscape_keyword_results
    else:
        buscape_results = buscape_category_results

    # Combina os resultados das buscas no Mercado Livre e no Buscapé
    results = mercadolivre_results + buscape_results

    return results
