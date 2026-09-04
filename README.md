# DevHelper IA

Assistente virtual desenvolvido para auxiliar estudantes e desenvolvedores iniciantes com dúvidas relacionadas à programação.

## Sobre o projeto

O DevHelper IA utiliza Inteligência Artificial e uma base de conhecimento organizada para responder dúvidas sobre desenvolvimento de software.

A proposta é fornecer respostas simples e objetivas, evitando informações que não estejam presentes na base de conhecimento.

## Objetivo

Criar um assistente capaz de:

* Responder dúvidas de programação;
* Explicar conceitos técnicos de forma simples;
* Auxiliar na identificação de erros;
* Sugerir próximos passos para resolver um problema;
* Informar quando não possui conhecimento suficiente para responder.

## Público-alvo

Estudantes de programação e desenvolvedores iniciantes que precisam de auxílio durante seus estudos.

## Tecnologias

* Python
* Inteligência Artificial
* JSON
* Google Colab
* GitHub

## Estrutura

```text
devhelper-ia/
│
├── README.md
├── data/
│   └── conhecimento.json
├── docs/
│   ├── documentacao.md
│   ├── prompts.md
│   ├── avaliacao.md
│   └── pitch.md
└── src/
    └── app.py
```

## Funcionamento

O usuário envia uma pergunta para o assistente.

O sistema analisa a pergunta, consulta a base de conhecimento e gera uma resposta relacionada ao conteúdo disponível.

Fluxo:

```text
Usuário
   ↓
Pergunta
   ↓
Assistente
   ↓
Base de conhecimento
   ↓
Processamento
   ↓
Resposta
```

## Critério de segurança

Quando uma informação não estiver disponível na base de conhecimento, o assistente deve informar que não possui dados suficientes em vez de inventar uma resposta.

## Exemplo

**Usuário:**

```text
O que é uma API REST?
```

**Assistente:**

```text
Uma API REST é uma interface que permite a comunicação entre sistemas
utilizando princípios do estilo arquitetural REST e normalmente o
protocolo HTTP.
```

## Possíveis melhorias

* Integração com uma API de IA;
* Interface Web;
* Histórico das conversas;
* Banco de dados;
* Sistema de avaliação das respostas;
* Autenticação de usuários.

## Autor

Ruan

Projeto desenvolvido como parte de um Lab da DIO sobre construção de assistentes virtuais com Inteligência Artificial.
