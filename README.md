# **ChatBot Gemini Pro**

![chatbot-gif ‐ Clipchamp ile yapıldı](https://github.com/ahmetdzdrr/gemini-pro-chatbot/assets/117534684/41018d7b-5253-4273-bddd-83277afe95fe)

## **Índice**

- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [O que é Flask?](#o-que-é-flask)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Como Criar a API do Google?](#como-criar-a-api-do-google)
- [Instalação](#instalação)
- [Código de Uso](#código-de-uso)
- [Contribuição](#contribuição)

## **Introdução**

Esta aplicação de chat baseada em Flask está sendo desenvolvida utilizando HTML, CSS e JS. Este projeto engloba o Gemini, um chatbot conversacional com tecnologia de IA.

## **Tecnologias Utilizadas**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## **O que é Flask?**

Flask é um framework de desenvolvimento de aplicativos web baseado em Python. Conhecido por sua natureza minimalista e flexível, é usado para criar aplicativos web e APIs. Embora forneça funcionalidade central, ele acomoda várias necessidades por meio de um sistema de extensões extensivo. Ele oferece recursos básicos como roteamento, manipulação de solicitações HTTP, suporte a templates e é frequentemente preferido para prototipagem rápida ou desenvolvimento de projetos de médio porte.

## **Visão Geral do Projeto**

As pastas no projeto são as seguintes:

- **.env**: Este arquivo contém a CHAVE DA API do Gemini e a CHAVE SECRETA. Você deve configurar essas chaves.
- **static**: Contém códigos CSS e JavaScript, juntamente com vários ícones e imagens.
- **templates**: Armazena o código HTML necessário para a implantação da aplicação Flask.
- **requirements.txt**: Contém bibliotecas de dependências para instalação.

> ### **app.py**

O arquivo contém códigos de rotas fornecidos pelo framework Flask. Quando o site é implantado, as direções das rotas dentro do arquivo app.py operam com base nas ações no site, direcionando o fluxo do site de acordo.

> ### **config.py**

O arquivo contém códigos de rotas de envio de e-mail. Ele fornece o envio de e-mail com servidor SMTP e funciona na página de contato com configurações básicas.

## **Como Criar a API do Google?**

Para utilizar o Google Gemini Pro, [clique aqui](https://makersuite.google.com/app/apikey) para obter sua Chave de API do Google e prossiga com as etapas.

## **Instalação**

1.  Python 3.8+ é necessário para executar este projeto.
2.  Crie um ambiente virtual: `python -m venv venv`
3.  Ative o ambiente virtual:
    - Windows: `venv\Scripts\activate`
    - Unix ou MacOS: `source venv/bin/activate`
4.  Crie um arquivo `.env` e adicione as variáveis ambientais necessárias:

           GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GOOGLE"
           SECRET_KEY="SUA_CHAVE_SECRETA"

5.  Clone este repositório para sua máquina local usando Git:

         git clone https://github.com/ahmetdzdrr/gemini-pro-chatbot.git

6.  Instale as bibliotecas Python necessárias executando:

          pip install -r requirements.txt

## **Código de Uso**

- `/home` - Carrega a página inicial.
- `/about` - Carrega a página sobre.
- `/contact` - Carrega a página de contato.
- `/gemini` - Carrega uma página para usar o modelo Gemini Pro.
- `/send-mail` - Envia automaticamente um e-mail da página de contato.

Para executar o projeto, siga estas etapas:

Abra seu terminal ou prompt de comando.

Navegue até o diretório onde os arquivos do projeto estão localizados.

Digite o seguinte comando:

```bash
python app.py
```

## **Contribuição**

Suas contribuições são bem-vindas! Se você deseja contribuir, sinta-se à vontade para abrir uma solicitação de pull. Por favor, explique suas alterações.
