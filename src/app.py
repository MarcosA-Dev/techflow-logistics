import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

# Configuração da página do Streamlit
st.set_page_config(page_title="TechFlow Logistics", layout="wide", page_icon="🚚")
st.title("🚚 TechFlow Solutions - Sistema de Logística")

def conectar_banco():
    """Conecta ao banco de dados em uma pasta segura na home do usuário para evitar bloqueios."""
    pasta_usuario = Path.home()
    pasta_segura = pasta_usuario / ".techflow_banco"
    pasta_segura.mkdir(exist_ok=True)
    caminho_banco = pasta_segura / "logistica.db"
    
    conn = sqlite3.connect(str(caminho_banco))
    conn.row_factory = sqlite3.Row
    return conn

# Inicialização e criação da tabela (roda automaticamente ao abrir o app)
try:
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL,
            responsavel TEXT,
            prioridade TEXT DEFAULT 'Média'
        )
    """)
    conn.commit()
    conn.close()
except Exception as e:
    st.error(f"Erro ao inicializar o banco de dados: {e}")

# Criando as abas de navegação no painel do Streamlit
aba_painel, aba_criar, aba_gerenciar = st.tabs([
    "📊 Painel Kanban", 
    "➕ Nova Demanda", 
    "⚙️ Gerenciar Tarefas"
])

# Mensagem informativa de rodapé
st.caption("TechFlow Logistics v1.0 - Sistema desenvolvido para controle de fluxo de transporte.")


# ABA 2: NOVA DEMANDA (O "C" do CRUD - Create)

with aba_criar:
    st.markdown("### Cadastrar Nova Demanda de Logística")
    
    with st.form("form_cadastro_tarefa"):
        titulo = st.text_input("Título da Entrega/Serviço * (Ex: Entrega Zona Sul)")
        descricao = st.text_area("Descrição detalhada da rota ou carga")
        responsavel = st.text_input("Motorista / Operador Responsável")
        prioridade = st.selectbox("Grau de Prioridade *", ["Baixa", "Média", "Alta"]) # CAMPO NOVO
        status_inicial = "A Fazer"
        
        botao_enviar = st.form_submit_button("Salvar Demanda")
        
        if botao_enviar:
            from src.validacoes import validar_titulo_tarefa
            if not validar_titulo_tarefa(titulo):
                st.error("Erro: O título da tarefa não pode estar vazio!")
            else:
                try:
                    conn = conectar_banco()
                    cursor = conn.cursor()
                    # Query atualizada com a prioridade
                    cursor.execute(
                        "INSERT INTO tarefas (titulo, descricao, status, responsavel, prioridade) VALUES (?, ?, ?, ?, ?)",
                        (titulo, descricao, status_inicial, responsavel, prioridade)
                    )
                    conn.commit()
                    conn.close()
                    st.success(f"Sucesso: '{titulo}' ({prioridade}) adicionado! Atualize a página.")
                except Exception as e:
                    st.error(f"Erro ao salvar no banco de dados: {e}")


# ABA 1: PAINEL KANBAN (Acompanhamento em Tempo Real)

with aba_painel:
    st.markdown("### Fluxo de Trabalho Atualizado")
    
    try:
        # Buscar dados atualizados do banco de dados
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        todas_tarefas = cursor.fetchall()
        conn.close()
        
        # Criar as 3 colunas visuais simulando o quadro Kanban
        col_fazer, col_progresso, col_concluido = st.columns(3)
        
        with col_fazer:
            st.error("📌 A FAZER")
            st.write("---")
            for t in todas_tarefas:
                if t['status'] == 'A Fazer':
                    # Usa o expander do Streamlit para criar um card retrátil
                    with st.expander(f"📦 ID {t['id']}: {t['titulo']}"):
                        st.write(f"**Responsável:** {t['responsavel']}")
                        st.write(f"**Descrição:** {t['descricao']}")
                        st.write(f"**Prioridade:** {t['prioridade']}")
                        
        with col_progresso:
            st.warning("🚚 EM PROGRESSO")
            st.write("---")
            for t in todas_tarefas:
                if t['status'] == 'Em Progresso':
                    with st.expander(f"⚡ ID {t['id']}: {t['titulo']}"):
                        st.write(f"**Responsável:** {t['responsavel']}")
                        st.write(f"**Descrição:** {t['descricao']}")
                        st.write(f"**Prioridade:** {t['prioridade']}")
                        
        with col_concluido:
            st.success("✅ CONCLUÍDO")
            st.write("---")
            for t in todas_tarefas:
                if t['status'] == 'Concluído':
                    with st.expander(f"🏁 ID {t['id']}: {t['titulo']}"):
                        st.write(f"**Responsável:** {t['responsavel']}")
                        st.write(f"**Descrição:** {t['descricao']}")
                        st.write(f"**Prioridade:** {t['prioridade']}")
                        
    except Exception as e:
        st.error(f"Erro ao carregar o painel Kanban: {e}")


# ABA 3: GERENCIAR TAREFAS (O "U" e "D" do CRUD - Update/Delete)

with aba_gerenciar:
    st.markdown("### Gerenciamento de Demandas Ativas")
    
    try:
        conn = conectar_banco()
        # Carrega os dados em um DataFrame do Pandas para exibição em tabela limpa
        df = pd.read_sql_query("SELECT id, titulo, prioridade, status, responsavel FROM tarefas", conn)
        conn.close()
        
        if df.empty:
            st.info("Nenhuma demanda cadastrada para gerenciamento no momento.")
        else:
            # Exibe a tabela com os dados atuais do banco
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.write("---")
            
            # Criando duas colunas na interface: uma para atualizar e outra para deletar
            col_atualizar, col_deletar = st.columns(2)
            
            with col_atualizar:
                st.markdown("#### 🔄 Atualizar Status da Demanda")
                id_atualizar = st.number_input("Digite o ID da demanda para alterar:", min_value=1, step=1, key="id_up")
                novo_status = st.selectbox("Selecione o novo status:", ["A Fazer", "Em Progresso", "Concluído"])
                
                if st.button("Atualizar Status", type="primary"):
                    conn = conectar_banco()
                    cursor = conn.cursor()
                    # Verifica se o ID realmente existe antes de atualizar
                    cursor.execute("SELECT id FROM tarefas WHERE id = ?", (id_atualizar,))
                    if cursor.fetchone() is None:
                        st.error(f"Erro: O ID {id_atualizar} não foi encontrado no sistema.")
                    else:
                        cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (novo_status, id_atualizar))
                        conn.commit()
                        st.success(f"Sucesso: Demanda ID {id_atualizar} movida para '{novo_status}'. Atualize a página.")
                    conn.close()
                    
            with col_deletar:
                st.markdown("#### ❌ Excluir Demanda do Sistema")
                id_excluir = st.number_input("Digite o ID da demanda para deletar:", min_value=1, step=1, key="id_del")
                
                if st.button("Remover Registro", type="secondary"):
                    conn = conectar_banco()
                    cursor = conn.cursor()
                    cursor.execute("SELECT id FROM tarefas WHERE id = ?", (id_excluir,))
                    if cursor.fetchone() is None:
                        st.error(f"Erro: O ID {id_excluir} não foi encontrado no sistema.")
                    else:
                        cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_excluir,))
                        conn.commit()
                        st.warning(f"Aviso: Demanda ID {id_excluir} foi removida com sucesso do sistema.")
                    conn.close()
                    
    except Exception as e:
        st.error(f"Erro ao carregar a área de gerenciamento: {e}")