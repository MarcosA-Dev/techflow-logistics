# TechFlow Logistics

Sistema de gerenciamento de demandas e fluxos logísticos baseado na metodologia Kanban. O projeto foi desenvolvido em Python utilizando Streamlit para a interface gráfica e SQLite para persistência estável de dados. O fluxo também conta com testes unitários automatizados integrados a uma esteira de Integração Contínua via GitHub Actions.

## Funcionalidades do Sistema

O sistema contempla as operações fundamentais para o controle de cargas e rotas:

* **Painel Kanban:** Visualização do fluxo de trabalho dividido em colunas para triagem de demandas em tempo real.
* **Nova Demanda:** Formulário estruturado para cadastro de serviços, registrando título, descrição e o operador responsável.
* **Gerenciar Tarefas:** Área administrativa para atualização de status dos registros cadastrados e remoção de demandas concluídas ou canceladas.

## Histórico de Alteração de Escopo

Durante o ciclo de desenvolvimento da aplicação, foi identificada a necessidade de mapear o nível de urgência dos serviços para otimizar a triagem da expedição. Como solução para essa demanda de negócios, o projeto passou por uma refatoração adaptativa para incorporar o conceito de Grau de Prioridade (dividido em Baixa, Média e Alta).

Essa modificação exigiu a reestruturação da tabela do banco de dados SQLite para suportar o novo atributo, além da atualização da interface gráfica com a inclusão de um campo de seleção no formulário de cadastro e a exibição correspondente da prioridade diretamente nos cartões informativos do painel Kanban.

## Estrutura de Diretórios

O projeto adota uma divisão clara entre os arquivos de produção e as rotinas de validação:

```text
techflow-logistics/
├── .github/
│   └── workflows/
│       └── testes.yml       # Configuração da pipeline de CI
├── src/
│   ├── app.py               # Interface gráfica e banco de dados
│   └── validacoes.py        # Funções lógicas de validação
├── tests/
│   └── test_validacoes.py   # Validações automatizadas
├── .gitignore               # Restrições de arquivos locais
└── requirements.txt         # Lista de dependências do Python

```

## Instruções de Execução Local

Para rodar a aplicação em ambiente local, realize o clone do repositório e execute a instalação das dependências listadas no arquivo de requisitos:

```bash
git clone https://github.com/SEU_USUARIO/techflow-logistics.git
cd techflow-logistics
pip install -r requirements.txt

```

Após concluir a instalação de todos os pacotes necessários, utilize o comando a seguir a partir da raiz do projeto para inicializar a interface do painel de logística no navegador:

```bash
streamlit run src/app.py

```
