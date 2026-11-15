

# CANES — Catálogo web

## Sobre o projeto

O CANES é um projeto acadêmico que estou desenvolvendo durante minhas aulas de Python e Django, com o objetivo de colocar em prática os conhecimentos adquiridos em programação e desenvolvimento web.

Durante o desenvolvimento, venho trabalhando com a criação de páginas HTML, configuração de rotas, funções em Python, templates do Django e organização dos arquivos do projeto.

O sistema apresenta um catálogo de produtos e  pedidos, utilizando dados fictícios para realizar cálculos e apresentar informações na interface.

## Funcionalidades

- **Página inicial:** apresentação do projeto CANES.
- **Catálogo de produtos:** exibição de produtos cadastrados, preços e quantidades em estoque.
- **Indicadores do catálogo:** quantidade de produtos cadastrados, produtos disponíveis e valor total em estoque.
- **Filtros de produtos:** opções para visualizar todos os produtos, disponíveis e indisponíveis.
- **Painel de pedidos:** apresentação dos pedidos, clientes, produtos, quantidades, valores e situações.
- **Indicadores de pedidos:** cálculo do total de pedidos, pedidos pendentes, concluídos e valor total.
- **Saudação personalizada:** exibição de uma mensagem utilizando o nome informado na URL.
- **Componentes reutilizáveis:** utilização de templates para organizar cabeçalho, rodapé e mensagens informativas.
- **Páginas responsivas:** adaptação de elementos visuais para diferentes tamanhos de tela.

## Tecnologias utilizadas

- **Python:** desenvolvimento das funções, condições, repetições e cálculos.
- **Django:** criação das views, rotas e renderização das páginas.
- **HTML5:** estruturação do conteúdo.
- **CSS3:** estilização e responsividade.
- **JavaScript:** funcionamento dos filtros do catálogo.
- **Git e GitHub:** versionamento e publicação do código.
- **VS Code:** ambiente utilizado para desenvolver o projeto.

## Estrutura do projeto

O projeto está organizado em pastas para separar as configurações do Django, as funções Python e os arquivos utilizados na interface.

- `config/` — configurações gerais e rotas principais.
- `core/` — aplicativo responsável pelas páginas e funcionalidades.
- `core/views.py` — funções responsáveis por processar os dados e renderizar as páginas.
- `core/urls.py` — definição das rotas do aplicativo.
- `core/templates/core/` — arquivos HTML do projeto.
- `core/templates/core/partials/` — componentes HTML reutilizáveis.
- `core/static/core/css/style.css` — estilos compartilhados.
- `manage.py` — gerenciamento do projeto Django.
- `requirements.txt` — dependências necessárias para executar o projeto.

## Instalação e execução

Para executar o projeto localmente, é necessário ter o Python instalado.

Primeiro, clone o repositório e acesse a pasta do projeto.

### Windows — PowerShell

py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver


Depois, abra o navegador e acesse:

http://127.0.0.1:8000/

## Páginas do projeto

| Rota | Descrição |
|---|---|
| `/` | Página inicial do CANES |
| `/catalogo/` | Catálogo de produtos |
| `/pedidos/` | Painel de acompanhamento de pedidos |
| `/ola/Anderson/` | Exemplo de saudação personalizada |
| `/sobre/` | Informações sobre o projeto |

## Aprendizados durante o desenvolvimento

Durante as aulas e o desenvolvimento do CANES, venho aprendendo a trabalhar com a estrutura de um projeto Django e a integrar o Python com páginas HTML.

Também pratiquei a utilização de variáveis, listas, dicionários, estruturas condicionais, laços de repetição e funções para calcular e organizar informações.

Outro aprendizado importante foi a utilização de templates reutilizáveis, evitando repetir códigos em diferentes páginas.

Além disso, estou utilizando o Git e o GitHub para acompanhar as alterações realizadas e manter o projeto atualizado.

## Observações

Este projeto possui finalidade educacional e está em desenvolvimento.

Os produtos e pedidos utilizados são fictícios e definidos diretamente no código Python, sem um sistema de cadastro ou armazenamento desses registros em banco de dados.

Novas funcionalidades e melhorias poderão ser adicionadas conforme o avanço das aulas.

## Desenvolvedor

**Anderson Santos**

Estudante de desenvolvimento web, com foco no aprimoramento dos conhecimentos em Python, Django, HTML, CSS e JavaScript.

**GitHub:** https://github.com/Anderssantos
