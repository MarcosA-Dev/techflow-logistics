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
            responsavel TEXT
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