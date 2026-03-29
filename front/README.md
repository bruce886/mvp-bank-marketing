# 📊 MVP - Previsão de Adesão a Depósito Bancário

Este projeto foi desenvolvido no contexto da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes**, com o objetivo de integrar um modelo de Machine Learning a uma aplicação full stack (frontend + backend).

---

## 🚀 Objetivo

O sistema tem como objetivo prever se um cliente irá aderir a um depósito a prazo, com base em dados provenientes de campanhas de marketing bancário.

O modelo de Machine Learning foi treinado utilizando o dataset **Bank Marketing** e integrado a uma API, permitindo a realização de predições em tempo real.

---

## 🧠 Tecnologias Utilizadas

### 🔹 Backend
- Python
- Flask
- Scikit-learn
- Joblib

### 🔹 Frontend
- HTML
- JavaScript

---

## 📂 Estrutura do Projeto

- notebook/ → construção do modelo de machine learning  
- backend/ → API responsável pelas predições  
- frontend/ → interface para entrada de dados  
- README.md → documentação do projeto  


---

## ▶️ Como Executar o Projeto

### 🔹 Backend

1. Acesse a pasta do backend:
cd api


2. Instale as dependências:
pip install -r requirements.txt


3. Execute a aplicação:
python app.py


A API estará disponível em:
http://localhost:5000


---

### 🔹 Frontend

1. Acesse a pasta:
cd front

2. Abra o arquivo no navegador:
index.html


---

## 🧪 Testes Automatizados

Para executar os testes:
pytest


Os testes garantem que o modelo atenda aos requisitos mínimos de desempenho definidos.

---

## 📓 Notebook de Machine Learning

O notebook contendo todo o processo de construção do modelo está disponível na pasta:
notebook/


Ele inclui:
- Análise exploratória dos dados (EDA)
- Tratamento e preparação dos dados
- Treinamento de múltiplos modelos (KNN, Árvore, Naive Bayes, SVM)
- Validação cruzada
- Otimização de hiperparâmetros
- Exportação do modelo

---

## 🎯 Funcionalidades

- Inserção de dados pelo usuário via interface web
- Envio das informações para a API
- Processamento pelo modelo de Machine Learning
- Retorno da predição em tempo real

---

## 🔐 Segurança de Dados

Embora o dataset utilizado seja público, o projeto considera boas práticas de segurança, como:

- Tratamento e validação dos dados de entrada
- Separação entre frontend e backend
- Estrutura preparada para evitar inconsistências no modelo
- Possibilidade de anonimização de dados em cenários reais

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos como parte da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes**.