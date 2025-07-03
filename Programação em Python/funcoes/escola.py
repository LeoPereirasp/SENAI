alunos = {}

def cadastrar_aluno(nome: str, matricula: str) -> str:
    """
    Cadastra um novo aluno no sistema.

    :param nome: Nome do aluno.
    :param matricula: Matrícula única do aluno.
    :return: Mensagem de sucesso ou erro.
    """
    if matricula in alunos:
        return "Aluno já cadastrado."
    alunos[matricula] = {"nome": nome, "notas": []}
    return "Aluno cadastrado com sucesso."


def registrar_nota(matricula: str, nota: float) -> str | float:
    """
    Adiciona uma nota ao aluno.

    :param matricula: Matrícula do aluno.
    :param nota: Nota a ser adicionada.
    :return: Mensagem de sucesso ou erro.
    """
    if matricula not in alunos:
        return "Aluno não encontrado."
    if nota < 0 or nota > 10:
        return "Nota inválida. Use de 0 a 10."
    alunos[matricula]["notas"].append(nota)
    return "Nota registrada com sucesso."


def calcular_media(matricula: str) -> str:
    """
    Calcula e retorna a média do aluno.

    :param matricula: Matrícula do aluno.
    :return: Média ou mensagem de erro.
    """
    if matricula not in alunos:
        return "Aluno não encontrado."
    notas = alunos[matricula]["notas"]
    if not notas:
        return "Aluno ainda não possui notas."
    media = sum(notas) / len(notas)
    return f"Média de {alunos[matricula]['nome']}: {media:.2f}"


def listar_alunos() -> str:
    """
    Lista todos os alunos cadastrados.

    :return: String formatada com a lista dos alunos.
    """
    if not alunos:
        return "Nenhum aluno cadastrado."
    resultado = "Lista de alunos:\n"
    for matricula, dados in alunos.items():
        resultado += f"- {dados['nome']} (Matrícula: {matricula})\n"
    return resultado.strip()

def boletim_aluno(matricula: str) -> str:
    """
    Gera o boletim do aluno, exibindo as notas e a média.

    :param matricula: Matrícula do aluno.
    :return: Boletim formatado ou mensagem de erro.
    """
    if matricula not in alunos:
        return "Aluno não encontrado."

    notas = alunos[matricula]["notas"]
    nome = alunos[matricula]["nome"]

    if not notas:
        return f"Boletim de {nome}:\nNenhuma nota registrada."

    lista_notas = ""
    for nota in notas:
        lista_notas += f"{nota:.1f} "

    media = sum(notas) / len(notas)
    return f"Boletim de {nome}:\nNotas: {lista_notas.strip()}\nMédia final: {media:.2f}"