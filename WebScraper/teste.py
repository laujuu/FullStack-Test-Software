# importar função
from scraper import search_buscape_by_keyword
import pprint

# definir parâmetros de teste
category = 'celular'
keyword = 'Iphone'

# chamar função e imprimir resultado
results = search_buscape_by_keyword(category, keyword)

pprint.pprint(f'Foram encontrados {len(results)} resultados para a pesquisa na categoria {category}:')
for result in results:
    pprint.pprint(f'{result["title"]} - R${result["price"]} - {result["link"]}')
