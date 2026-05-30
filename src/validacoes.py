def validar_titulo_tarefa(titulo: str) -> bool:
    if not titulo or titulo.strip() == "":
        return False
    return True

def validar_status_kanban(status: str) -> bool:
    status_permitidos = ["A Fazer", "Em Progresso", "Concluído"]
    return status in status_permitidos