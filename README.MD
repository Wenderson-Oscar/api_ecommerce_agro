# Introdução à API para auxiliar os comerciantes agropecuários através de um projeto feito em Flutter

O objetivo da API é fornecer um conjunto de endpoints (URLs) que permitem a comunicação entre o aplicativo móvel desenvolvido em Flutter, destinado aos comerciantes agropecuários, e o servidor backend construído em Django. Essa API permitirá que o aplicativo Flutter acesse, envie e manipule dados relevantes para o funcionamento do aplicativo.

## Tutorial de como utilizar a API no Django

Neste tutorial, vamos abordar os passos para rodar a API em um ambiente virtual no Windows e Linux. É altamente recomendado o uso de ambientes virtuais para isolar as dependências do projeto e garantir um ambiente limpo e independente para a API.


## Clonando e configurando o projeto Django

1. Baixe ou clone o projeto Django da API.

2. Navegue para o diretório do projeto no terminal e execute o seguinte comando para clonar.

```bash
git clone https://github.com/Wenderson-Oscar/api_ecommerce_agro.git
```

3. Dentro do projeto abra o terminal

## Configurando o ambiente virtual

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

No Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalando as dependências do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

##  Realizando as migrações do banco de dados

```bash
python manage.py migrate
```

## Descobrindo o IP

execute o seguinte comando no terminal para descobrir o `IP`

```bash
ifconfig
```

ou 

```bash
hostname -I
```

## Iniciando o servidor de desenvolvimento

```bash
python manage.py runserver 'ip':8000
```

# Observação

Para o Aplicativo Funcionar, Tera que deixar a Api e a aplicação flutter rodando junto.