#Sistema Bancário Simples em Python

Este é um projeto de terminal que simula um sistema bancário básico, com funcionalidades de **depósito**, **saque**, **extrato** e **controle de limites**.

## Funcionalidades

- 📥 **Depósito**
  - Permite ao usuário inserir um valor positivo para adicionar ao saldo.
  - Valores negativos ou inválidos são rejeitados.

- 💸 **Saque**
  - Permite realizar até **3 saques diários**, cada um com valor máximo de **R$500,00**.
  - Verificações:
    - Saldo suficiente
    - Limite de valor por saque
    - Limite de quantidade de saques

- 📄 **Extrato**
  - Exibe:
    - Lista de todos os depósitos efetuados.
    - Lista de todos os saques realizados.
    - Saldo final.

- ❌ **Sair**
  - Encerra o programa.

## 🧠 Lógica e Regras de Negócio

- `LIMITE_DIARIO`: R$500 por saque.
- `LIMITE_SAQUES`: 3 saques por sessão.
- Armazenamento de histórico de depósitos e saques em listas separadas.
- Verificações de entrada usando `try/except` e validação de valores.

## 📂 Estrutura de Código

- Uso de `while True` para exibir um menu interativo.
- Cada opção do menu (`d`, `s`, `e`, `q`) chama uma operação específica.
- Os dados do usuário são processados em tempo real e impressos no terminal.

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.6+).
2. Salve o código em um arquivo chamado `banco.py`.
3. Execute no terminal:

   ```bash
   python banco.py
