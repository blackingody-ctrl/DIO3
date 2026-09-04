# Avaliação e Métricas

A avaliação do DevHelper IA será realizada utilizando perguntas previamente definidas.

## Critérios

Cada resposta será analisada considerando:

### 1. Relevância

A resposta está relacionada à pergunta?

### 2. Precisão

A informação apresentada está correta de acordo com a base de conhecimento?

### 3. Clareza

A resposta pode ser compreendida por um estudante iniciante?

### 4. Limitação

O assistente informa quando não possui informação suficiente?

## Testes

### Teste 1

Pergunta:

```text
O que é Python?
```

Resultado esperado:

Uma explicação sobre Python baseada na base de conhecimento.

### Teste 2

Pergunta:

```text
O que é Git?
```

Resultado esperado:

Uma explicação sobre Git.

### Teste 3

Pergunta:

```text
O que é um endpoint?
```

Resultado esperado:

Uma explicação sobre endpoint em APIs.

### Teste 4

Pergunta fora da base:

```text
Qual é a previsão do tempo para amanhã?
```

Resultado esperado:

O assistente deve informar que não possui informações suficientes para responder.

## Métrica

Foi utilizada uma avaliação simples baseada em três categorias:

* Resposta correta;
* Resposta parcialmente correta;
* Resposta incorreta.

O objetivo não é medir apenas a quantidade de respostas corretas, mas verificar se o comportamento do assistente está de acordo com as regras definidas.
