import json
import difflib

with open("../data/conhecimento.json", "r", encoding="utf-8") as arquivo:
    conhecimento = json.load(arquivo)

def carregar_conhecimento():
    itens = {}

    for categoria, dados in conhecimento.items():
        for chave, valor in dados.items():
            itens[chave.lower()] = valor

    return itens

base = carregar_conhecimento()

def buscar_resposta(pergunta):
    pergunta = pergunta.lower().strip()

    melhor_chave = None
    melhor_nivel = 0

    for chave in base:
        palavras = pergunta.split()

        nivel = 0

        for palavra in palavras:
            if len(palavra) > 2 and palavra in chave:
                nivel += 1

        similaridade = difflib.SequenceMatcher(
            None,
            pergunta,
            chave
        ).ratio()

        nivel += similaridade

        if nivel > melhor_nivel:
            melhor_nivel = nivel
            melhor_chave = chave

    if melhor_chave is None or melhor_nivel < 0.7:
        return "Não encontrei informações suficientes na minha base de conhecimento para responder essa pergunta."

    return base[melhor_chave]


def iniciar_assistente():
    print("=" * 50)
    print("DEVHELPER IA")
    print("=" * 50)
    print("Digite uma dúvida sobre programação.")
    print("Digite 'sair' para encerrar.")
    print()

    while True:
        pergunta = input("Você: ")

        if pergunta.lower().strip() == "sair":
            print("Assistente: Até mais.")
            break

        resposta = buscar_resposta(pergunta)

        print("Assistente:", resposta)
        print()


iniciar_assistente()
