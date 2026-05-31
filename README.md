Aqui está o arquivo `README.md` completo e atualizado, com a seção de **Mudança de Escopo** incluída de forma clara para o professor ver. É só copiar o bloco inteiro abaixo e colar direto no seu arquivo:

```markdown
# 🚚 TechFlow Logistics

Sistema dinâmico de gerenciamento de demandas e fluxos logísticos baseado na metodologia ágil Kanban. O projeto foi desenvolvido em Python utilizando **Streamlit** para a interface gráfica, **SQLite** para persistência estável de dados e **Pytest** para automação de testes unitários integrados a uma esteira de Integração Contínua (CI) via GitHub Actions.

## 📋 Funcionalidades (CRUD Completo)

- **📊 Painel Kanban (Read):** Visualização dinâmica e em tempo real das demandas logísticas divididas em três colunas estruturadas (`A Fazer`, `Em Progresso` e `Concluído`) utilizando cards retráteis (`st.expander`).
- **➕ Nova Demanda (Create):** Formulário seguro para cadastro de rotas, cargas e motoristas responsáveis, com validação de dados em tempo de execução.
- **⚙️ Gerenciar Tarefas (Update & Delete):** Painel administrativo integrado com tabelas do Pandas para atualizar o status de movimentação dos cards ou realizar a exclusão definitiva de registros.

## 🔄 Registro de Mudança de Escopo (Histórico de Adaptação)

Durante o ciclo de desenvolvimento do projeto, foi identificada a necessidade crítica de uma alteração de escopo pelo setor de operações logísticas:

* **Demanda de Mudança:** O sistema precisava de uma forma visual e estruturada para diferenciar a urgência das entregas, pois tratar todas as demandas com o mesmo peso gerava gargalos na expedição.
* **Solução Implementada:** Foi realizada uma refatoração adaptativa no meio do projeto para incluir o conceito de **Grau de Prioridade** (`Baixa`, `Média`, `Alta`). Essa alteração exigiu a modificação dinâmica da estrutura da tabela no banco de dados SQLite, a inclusão de um campo de seleção (`st.selectbox`) no formulário de cadastro, e a renderização visual do nível de prioridade diretamente nos cards do painel Kanban e na tabela de gerenciamento.

## 📐 Estrutura do Projeto

O projeto segue as diretrizes recomendadas de Engenharia de Software, isolando o código de produção das rotinas de testes automatizados:

```text
techflow-logistics/
├── .github/
│   └── workflows/
│       └── testes.yml       # Configuração do GitHub Actions (CI)
├── src/
│   ├── app.py               # Interface Streamlit e Conexão SQLite
│   └── validacoes.py        # Regras de negócio e validações puras
├── tests/
│   └── test_validacoes.py   # Testes unitários com Pytest
├── .gitignore               # Proteção contra arquivos locais e binários
└── requirements.txt         # Dependências do projeto

```

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório

```bash
git clone [https://github.com/SEU_USUARIO/techflow-logistics.git](https://github.com/SEU_USUARIO/techflow-logistics.git)
cd techflow-logistics

```

### 2. Configurar o Ambiente Virtual (Opcional, mas recomendado)

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt

```

### 4. Executar a Aplicação Streamlit

Certifique-se de estar na **raiz do projeto** (`techflow-logistics`) e execute o comando:

```bash
streamlit run src/app.py

```

O navegador abrirá automaticamente o endereço `http://localhost:8501`.

---

## 🧪 Como Rodar os Testes Automatizados

As regras de validação lógica do sistema foram blindadas contra falhas através de testes unitários. Para executá-los localmente, configure o `PYTHONPATH` na raiz do projeto e chame o Pytest:

```bash
# No Windows (PowerShell):
$env:PYTHONPATH="."
pytest

# No Windows (CMD):
set PYTHONPATH=.
pytest

# No Linux/macOS:
export PYTHONPATH=.
pytest

```

*Nota: Toda alteração enviada para o repositório principal dispara automaticamente a pipeline do **GitHub Actions**, que valida a integridade das funções na nuvem utilizando ambientes virtuais Ubuntu.*

```

```
