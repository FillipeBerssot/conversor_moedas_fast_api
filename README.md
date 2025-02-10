# 🚀 Conversor de Moedas - FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)

Este projeto é um **Conversor de Moedas** desenvolvido com **FastAPI**, permitindo a conversão de valores entre diferentes moedas utilizando APIs externas.

---

## 🚀 Funcionalidades
✅ Conversão de moedas com base em valores atuais.
✅ API síncrona utilizando **FastAPI**.
✅ Cobertura de testes utilizando **pytest** e **VCR.py**.
✅ Configuração de variáveis de ambiente com **.env**.
✅ Gerenciamento de dependências com **Poetry**.
✅ Uso de **Ruff** para padronização do código.
✅ Automação de tarefas com **Taskipy**.

---

## 📌 Pré-requisitos

Antes de começar, você precisará ter os seguintes requisitos instalados:

- 📌 [Python 3.12+](https://www.python.org/downloads/)
- 📌 [Poetry](https://python-poetry.org/docs/#installation)
- 📌 [Taskipy](https://github.com/taskipy/taskipy)
- 📌 [Git](https://git-scm.com/downloads)

---

## 🔧 Instalação

1️⃣ **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/conversor-moedas-fast-api.git
   cd conversor-moedas-fast-api
   ```

2️⃣ **Instale as dependências com Poetry:**
   ```bash
   poetry install
   ```

3️⃣ **Ative o ambiente virtual do Poetry:**
   ```bash
   poetry shell
   ```

4️⃣ **Crie um arquivo `.env` na raiz do projeto e configure suas credenciais:**
   ```ini
   ALPHA_VANTAGE_API_NEW_KEY=suachaveaqui
   ```

---

## 🚀 Como Executar

Para rodar o servidor **FastAPI**, utilize o Taskipy:

```bash
task run
```

🔗 A API estará disponível em:

- 📄 **Docs interativas (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📄 **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Testes

O projeto inclui testes automatizados com `pytest`. Para executá-los, use o Taskipy:

```bash
task test
```

Se quiser gerar um relatório de cobertura de código:

```bash
task post_test
```

---

## 📂 Estrutura do Projeto

```bash
conversor_moedas_fast_api/
│── conversor_moedas_fast_api/
│   ├── app.py                # Arquivo principal da aplicação
│   ├── routers/              # Rotas da API
│   ├── schemas/              # Schemas (modelos de entrada/saída)
│   ├── services/             # Lógica de conversão de moedas
│   ├── settings/             # Configurações do projeto
│── tests/                    # Testes automatizados
│   ├── fixture/              # Fixtures para testes
│   ├── e2e/                  # Testes de integração (end-to-end)
│── pyproject.toml            # Gerenciamento de dependências (Poetry)
│── .gitignore                # Arquivos ignorados pelo Git
│── .env                      # Variáveis de ambiente (NÃO COMMITAR!)
```

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como um estudo prático sobre **FastAPI**, **testes automatizados** e **ferramentas auxiliares** como **Poetry**, **PyTest**, **Taskipy**, **Ruff** e outros.
O objetivo é aprimorar conhecimentos nessas tecnologias e aplicar boas práticas de desenvolvimento.
