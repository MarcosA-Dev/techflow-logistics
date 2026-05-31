from src.validacoes import validar_titulo_tarefa, validar_status_kanban

def test_titulo_com_texto_valido():
    assert validar_titulo_tarefa("Entrega de Carga Pesada #4002") is True

def test_titulo_invalido_vazio():
    assert validar_titulo_tarefa("") is False
    assert validar_titulo_tarefa("      ") is False

def test_status_kanban_corretos():
    assert validar_status_kanban("A Fazer") is True
    assert validar_status_kanban("Em Progresso") is True
    assert validar_status_kanban("Concluído") is True

def test_status_kanban_incorreto():
    assert validar_status_kanban("Cancelado") is False
    assert validar_status_kanban("Em Espera") is False