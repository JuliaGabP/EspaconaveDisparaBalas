# Espaconave Dispara Balas 

## Descrição

Este projeto foi desenvolvido como prática de programação em Python e desenvolvimento de jogos utilizando a biblioteca Pygame.   
No jogo, o jogador controla uma nave que pode se mover horizontalmente e disparar projéteis para destruir uma frota de alienígenas.   

## Funcionalidades

- Movimentação da nave
- Nível de dificuldade
- Disparo de projéteis
- Geração de frota de alienígenas
- Sistema de pontuação
- Controle de vidas da nave

## Tecnologias utilizadas

- Python 3
- Pygame

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/JuliaGabP/EspaconaveDisparaBalas.git
```

2. Entre na pasta do projeto:

```bash
cd EspaconaveDisparaBalas
```

3. Instale as dependências:

```bash
pip install pygame
```

## Como executar o jogo

Execute o arquivo principal:

```bash
python alien_invasion.py
```

## Controles

| Tecla | Ação |
|------|------|
| ← | mover nave para esquerda |
| → | mover nave para direita |
| Espaço | disparar |
| Q | sair do jogo |

## Estrutura do projeto

```
EspaconaveDisparaBalas
│
├── alien_invasion
    |
    ├── alien.py
    ├── alien_invasion.py
    ├── bullet.py
    ├── button.py
    ├── game_stats.py
    ├── scoreboard.py
    ├── settings.py
    └── ship.py
└── README.md
```

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Programação orientada a objetos
- Estrutura de jogos
- Manipulação de eventos
- Controle de sprites
- Organização de código em múltiplos arquivos
