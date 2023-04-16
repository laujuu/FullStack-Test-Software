from api_scraper.scraper import (
    search_mercadolivre_by_category,
    search_buscape_by_category,
    search_mercadolivre_by_keyword,
    search_buscape_by_keyword,
    search_all,
    )

import re


def test_search_mercadolivre_by_category():
    results = search_mercadolivre_by_category("computadores")
    assert len(results) > 0
    for result in results:
        assert result["category"] == "computadores"
        assert result["website"] == "Mercado Livre"


def test_search_buscape_by_category():
    results = search_buscape_by_category("celular")
    assert results
    for result in results:
        assert result["category"] == "celular"
        assert result["website"] == "Buscapé"


def test_search_mercadolivre_by_keyword():
    results = search_mercadolivre_by_keyword("celulares-telefones", "iphone")
    assert len(results) > 0
    for result in results:
        assert result["category"] == "celulares-telefones"
        assert result["website"] == "Mercado Livre"
        assert re.search(r"iphone", result["title"], re.IGNORECASE)


def test_search_buscape_by_keyword():
    results = search_buscape_by_keyword("celular", "iphone")
    assert results
    for result in results:
        assert result["category"] == "celular"
        assert result["website"] == "Buscapé"
        assert re.search(r"iphone", result["title"], re.IGNORECASE)


def test_search_all():
    category = 'celular'
    keyword = 'smartphone'

    results = search_all(category, keyword)

    assert len(results) > 0

    for result in results:
        assert result['category'] == category
        assert result["title"] is not None
        assert result['price'] is not None
        assert result['link'] is not None
