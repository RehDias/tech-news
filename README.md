# Tech News <img src="https://github.com/user-attachments/assets/fb2ab78a-af42-47b8-9e6a-d7cd4ccece6f" alt="image" width="60"/>

## Sobre

O **Tech News** é um projeto que realiza **web scraping** de um blog de notícias da Trybe, extraindo informações diretamente do HTML do site e armazenando-as em um banco de dados **MongoDB**. Através de uma interface em menu, o usuário pode:

- Definir a quantidade de notícias a ser extraída.
- Filtrar notícias por título, tag, data e categoria.
- Visualizar as cinco notícias mais populares.
- Exibir as cinco categorias mais frequentes nas notícias salvas.

Este projeto combina a coleta automática de dados com consultas flexíveis, permitindo uma análise rápida e eficiente das notícias.

## Funcionalidades

- **Web Scraping**: Extração automática de notícias do blog da Trybe.
- **Armazenamento de Dados**: As notícias extraídas são armazenadas em um banco de dados MongoDB.
- **Filtros**: Filtragem das notícias por:
  - Título
  - Tag
  - Data
  - Categoria
- **Ranking**:
  - Exibe as cinco notícias mais populares.
  - Exibe as cinco categorias mais frequentes nas notícias salvas.

## Tecnologias Utilizadas

- **Python**: Linguagem principal usada para o desenvolvimento do projeto.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar as notícias extraídas.
- **Requests**: Biblioteca Python usada para fazer as requisições HTTP e obter o HTML das páginas.
- **Parsel**: Utilizada para processar e extrair dados do HTML de forma eficiente.
- **Docker**: Utilizado para garantir a consistência do ambiente e facilitar a execução da aplicação.
- **docker-compose**: Gerencia e orquestra os containers Docker, fornecidos pela Trybe.

## Como Executar

### Pré-requisitos

- **Docker** e **docker-compose**: Certifique-se de que ambos estão instalados em sua máquina.

### Passo a Passo

1. Clone o repositório:

    ```bash
    git clone https://github.com/SeuUsuario/tech-news.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd tech-news
    ```

3. Execute o Docker para iniciar a aplicação:

    ```bash
    docker-compose up
    ```

4. Use o menu interativo para definir o número de notícias a serem extraídas e para aplicar filtros ou visualizar rankings.

## Estrutura do Projeto

- **tech_news/**: Contém o código principal do projeto.
  - **scraper/**: Responsável pelo processo de raspagem de dados utilizando `requests` e `parsel`.
  - **database/**: Gerenciamento do armazenamento das notícias no MongoDB.
  - **menu/**: Interface de menu para interações com o usuário, incluindo filtragem e exibição de rankings.

<h3>Aplicação</h3>

https://user-images.githubusercontent.com/91297277/202060508-506fcb8d-bac5-42c6-83ff-1587077711f1.mp4
