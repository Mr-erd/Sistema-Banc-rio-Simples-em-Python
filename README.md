# 🏦 Sistema Bancário Simples em Python

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)

## 📝 Descrição

Este projeto é uma simulação de um sistema bancário simples, desenvolvido inteiramente em Python. O objetivo foi aplicar conceitos fundamentais de programação, como manipulação de dados, modularização em funções e persistência de dados com arquivos JSON.

O sistema opera através de um menu interativo na linha de comando, permitindo ao usuário realizar operações bancárias básicas e gerenciar clientes e contas.

## ✨ Funcionalidades

O sistema oferece as seguintes operações:

* **[d] Depositar:** Permite ao usuário adicionar um valor em dinheiro à sua conta.
* **[s] Sacar:** Permite retirar um valor da conta, com validações de saldo, limite por saque (R$ 500,00) e quantidade diária de saques (3).
* **[e] Extrato:** Exibe o histórico de todas as transações (depósitos e saques) e o saldo atual.
* **[nu] Novo Usuário:** Cadastra um novo cliente no sistema. Os dados são salvos em `usuarios.json` para garantir persistência.
* **[nc] Nova Conta:** Cria uma nova conta corrente, que é sempre vinculada a um usuário já existente.
* **[lc] Listar Contas:** Mostra uma lista formatada de todas as contas criadas.
* **[q] Sair:** Encerra a aplicação de forma segura.

### Recursos Adicionais
* **Persistência de Dados:** As informações dos usuários são salvas localmente em um arquivo `usuarios.json`.
* **Interface de Usuário Amigável:** Inclui barras de carregamento para uma experiência mais agradável ao iniciar e sair do sistema.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Módulos Padrão do Python:**
    * `json`: Para serialização e persistência dos dados dos usuários.
    * `textwrap`: Para a formatação limpa do menu de texto.
    * `time`: Para criar os efeitos de carregamento.

## 🚀 Como Executar o Projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos
* É necessário ter o **Python 3** instalado em seu sistema.
* É necessário ter o **Git** instalado para clonar o repositório.

### Passos
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Mr-erd/Sistema-Banc-rio-Simples-em-Python.git](https://github.com/Mr-erd/Sistema-Banc-rio-Simples-em-Python.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Sistema-Banc-rio-Simples-em-Python
    ```

3.  **Execute o script principal:**
    ```bash
    python sistema_bancario.py
    ```
    
