Projeto dos Vingadores com Flask e SQLAlchemy
Este é um projeto em Python que utiliza o framework Flask e a biblioteca SQLAlchemy para criar uma aplicação web relacionada aos heróis dos Vingadores. Nesta aplicação, os usuários podem escolher seus heróis favoritos e visualizar informações sobre eles.

Requisitos
Antes de executar o projeto, certifique-se de que o seguinte software esteja instalado em seu ambiente de desenvolvimento:

Python (versão 3.x)
Flask (versão 2.x)
SQLAlchemy (versão 1.x)
Banco de dados (SQLite)
Instalação
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1. Clone o repositório para o seu ambiente de desenvolvimento:

git clone https://github.com/Igorsaulo/Avenger.git

2. Navegue para o diretório do projeto:

cd Avenger

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

4. nstale as dependências do projeto:

pip install -r requirements.txt

5. Inicie o servidor de desenvolvimento:

flask run

O servidor de desenvolvimento do Flask será iniciado e a aplicação estará disponível em http://localhost:5000 no seu navegador.

Funcionalidades
A aplicação possui as seguintes funcionalidades:

Exibição de lista de heróis dos Marvel com informações básicas sobre cada herói.
Detalhes de herói: visualização de informações detalhadas de um herói específico.
Escolha de herói favorito: os usuários podem escolher seus heróis favoritos e salvá-los na base de dados.
Visualização de heróis favoritos: os usuários podem visualizar a lista de seus heróis favoritos.
