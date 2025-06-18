![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

# 🚀 Automação Web de Extração e Processamento de Dados - Selenium + Python + Excel

## 📌 Visão Geral

Este projeto entrega uma solução completa de **automação web** para extração, transformação e manipulação de dados de um portal online, utilizando **Selenium WebDriver**, **PyAutoGUI**, **OpenPyXL** e **Pandas**.

> **Status:** Refatorado, Modular, Pronto para CI/CD e escalável para futuras integrações.

---

## 🏗️ Estrutura de Pastas

```
Automacao-Extracao/
├── src/
│   ├── __init__.py
│   ├── main.py                # Orquestração geral
│   ├── config.py              # Variáveis de ambiente
│   ├── logger.py              # Configuração de logging
│   ├── login.py               # Processo de login no portal
│   ├── navegacao.py           # Controle de módulos e páginas
│   ├── extracao.py            # Extração de tabelas e dados
│   ├── processamento.py       # Processamento, transformação e manipulação dos Excel
│   └── utils.py               # Funções utilitárias (scroll, esperar elementos, etc)
├── logs/                      # Logs gerados automaticamente
├── data/                      # Arquivos de entrada/saída
├── tests/                     # (Opcional) Testes unitários
├── .env                       # Variáveis sensíveis
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Tecnologias Usadas

| Tecnologia | Finalidade                               |
| ---------- | ---------------------------------------- |
| Python 3.x | Linguagem principal                      |
| Selenium   | Automação de navegador                   |
| Pandas     | Manipulação de DataFrames                |
| OpenPyXL   | Leitura e escrita de arquivos Excel      |
| PyAutoGUI  | Scroll horizontal e interações com mouse |
| dotenv     | Leitura de variáveis de ambiente         |
| Logging    | Monitoramento da execução                |

---

## ✅ Principais Funcionalidades

* Login automatizado com autenticação federada
* Navegação por múltiplos módulos
* Controle de paginação automática
* Scroll horizontal em áreas com overflow
* Extração de tabelas para Excel
* Backup de arquivos antes de sobrescrita
* Controle sequencial de IDs
* Duplicação de campanhas por terminal
* Colagem de colunas entre múltiplos arquivos Excel
* Mapeamento e transformação de colunas para geração de arquivo final
* Registro de logs por etapa, incluindo taxa de sucesso

---

## ⚙️ Configuração do Ambiente

### 1. Instalação das Dependências

```bash
pip install -r requirements.txt
```
**Requisitos:**
Antes de rodar a automação, é necessário que o driver do navegador (Microsoft Edge WebDriver) esteja configurado corretamente.


---

### 2. Configuração do `.env`

Exemplo de `.env`:

```
link=https://exemplo.com/login
CAMINHO_DRIVER_NAVEGADOR=C:/WebDrivers/msedgedriver.exe
ARQUIVO_BASE=data/base.xlsx
URL=https://exemplo.com/id=
ACESSO=//*[@id='login-federado']
MODULO_WEB=//*[@id='menu-aia']
SEGUNDO_MODULO_WEB=//*[@id='menu-campanhas']
CAMINHO_ARQUIVO_LOG=logs
TABELA=//*[@id='tabela-campanhas']
LINHAS_TABELA=//table/tbody/tr
SECAO_DE_NUMEROS=//*[@id='numeros']
LINHA_SECAO_DE_NUMEROS=//section//li
CONFIRMACAO_ACESSO=//*[@id='idp-abrtelecom']
ARQUIVO_EXTRACAO_POR_ID=data/terminais.xlsx
ARQUIVO_SHOW=data/Show.xlsx
ARQUIVO_FORMATADO=data/Final_Formatado.xlsx
```

---

## ▶️ Como Executar a Automação

```bash
python src/main.py
```

---

## 🧠 Fluxo de Execução (Macro)

1. **Loop Principal:**
   Executa múltiplos ciclos de login + navegação + extração.

2. **Processamento Pós-Loop:**
   Inclui:

- Extração de IDs
- Duplicação por terminal
- Colagem de terminais
- Geração de arquivo final
- Ajuste de colunas

3. **Log Final:**
   Taxa de sucesso, número de loops válidos, quantidade de linhas extraídas, etc.

---

## 📝 Exemplo de Saída de Log

```
✅ data e hora - INFO - Loop 1 concluído
✅ data e hora - INFO - Loop 2 concluído
❌ data e hora - ERROR - Loop 3 falhou no login
✅ data e hora - INFO - Loop 4 concluído
📊 data e hora - INFO - Taxa de Sucesso: 75%
🎉 data e hora - INFO - Operação Pós-Loop Finalizada com Sucesso!
```

---

## 📈 Melhorias Futuras (Roadmap)

* Implementar testes unitários e de integração
* Modularização completa via classes (OOP)
* Adicionar CI/CD com GitHub Actions
* Criação de Dockerfile
* Exportação para Google Sheets ou banco de dados
* Implementação de retry em caso de falhas temporárias no Selenium

---
