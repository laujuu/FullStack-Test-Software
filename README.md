# FullStack test software

  As notícias tinham que ser obtidas através da raspagem do [_meli_](mercadolivre.com.br/). e [ busca pé ](buscape.com.br/)

  <strong>🚵 Objetivo:</strong>
  <ul>
    <li>Através de um menu suspenso, podemos escolher as categorias: Celular, Geladeira, TV.</li>
    <li>Através de um menu suspenso, podemos escolher o site: Mercado Livre / Buscapé.</li>
    <li>Criar uma entrada de texto livre para buscar produtos.</li>
    <li>Após a pesquisa, a lista de produtos aparecerá na tela com: foto, descrição, categoria, preço e site onde as informações foram obtidas.</li>
    <li>Armazenar resultados no banco de dados após a pesquisa do usuário. Se repetir a mesma pesquisa (apenas levando em conta os filtros de categoria e site para armazenar), mostrar o que deixa a base e não desfazer para os sites.</li>
    <li>Hospedar a solução on-line em um servidor gratuito como Heroku ou outra alternativa.</li>
   </ul>

</details>

## Showcase
<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2FmNDQyYzIwZTViNGFlNGM3Nzc2YWRmNjdlN2M2YjZiZTYyZjQ5NyZjdD1n/PkMxgUq9wS7twv26nk/giphy.gif" width="700" height="400" />



## Histórico de `Commits`
  * Para ver a evolução do codigo você pode checar o histórico de commits  
  ![Screenshot_9](https://user-images.githubusercontent.com/37710776/229648831-1d560b18-a34f-42bf-91b3-20a44ff2125f.png)
  
  
  
## Como clonar e testar o projeto em sua `maquina`

* Use o comando: `git clone git@github.com:laujuu/FullStack-Test-Software.git`

  1. Entre na pasta do repositório que você acabou de clonar:

* `cd FullStack-Test-Software`

  2. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`


## Como testar a aplicação

Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  Para testar o scraper.py:

  ```bash
  cd api_scraper/
  pytest tests/test_scraper.py
  ```
  
   Para testar o app.py:

  ```bash
  cd api_scraper/
  pytest test_app.py
  ```

## Rodando a API

  1. Certifique-se de estar na pasta da api:

* `cd api_scraper/`

  2. Executando a api

* `python app.py`
  
Pronto, agora a API ja esta rodando


## Rotas da API

### Em seu navegador coloque os seguintes links

  1. rota para pegar resultados mercado-livre por categoria:

* `127.0.0.1:5000/search_meli_by_category?category=celulares-telefones`

  2. rota para pegar resultados mercado-livre por categoria e keyword (pesquisa):

* `127.0.0.1:5000/search_meli_by_keyword?category=celulares-telefones&keyword=iphone`

  3. rota para pegar resultados buscapé por categoria:

* `127.0.0.1:5000/search_buscape_by_category?category=celular`

  4. rota para pegar resultados buscapé por categoria e keyword (pesquisa):

* `/search_buscape_by_keyword?category=celular&keyword=iphone`

  5. rota para pegar meli e buscapé ao mesmo tempo por categoria e keyword (pesquisa):

* `/search_all_by_category?category=celular&keyword=iphone`


## Rodando o Front End

  1. Em um terminal deixe a API rodando como explicado no passo anterior:

  2. Entre na pasta do front

* `cd client/`

  2. instale as dependencias

* `npm install`

 3. Rode o Front End

* `npm run dev`

Pronto agora o front e o back estão funcionando e comunicando entre sí, fique a vontade para explorar ;)







