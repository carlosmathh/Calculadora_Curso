#  Calculadora Desktop em Python (PySide6)

Aplicação desktop desenvolvida em **Python** utilizando **PySide6 (Qt for Python)**, com foco em **arquitetura limpa**, **organização modular**, **boas práticas de Programação Orientada a Objetos** e **experiência do usuário**.

O projeto simula uma calculadora real, oferecendo interface moderna em **Dark Mode**, suporte a **teclado e mouse**, tratamento robusto de erros e separação clara entre **interface**, **lógica**, **estilos** e **utilidades**.

---

##  Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

- Consolidar conhecimentos em **Python Desktop**
- Praticar **Programação Orientada a Objetos**
- Trabalhar com **Signals & Slots (Qt)**
- Criar uma aplicação real, funcional e organizada
- Demonstrar boas práticas de estruturação de código

---

##  Funcionalidades

- Interface gráfica moderna (Dark Theme)
- Operações matemáticas:
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
  - Exponenciação (`^`)
- Entrada por teclado e botões
- Exibição da equação em tempo real
- Botões especiais:
  - Limpar (`C`)
  - Backspace (`◀`)
  - Inverter sinal (`NE`)
- Tratamento de erros:
  - Divisão por zero
  - Overflow numérico
  - Operações incompletas
- Janela com tamanho fixo
- Ícone personalizado

---

##  Tecnologias Utilizadas

- Python 3
- PySide6 (Qt for Python)
- QDarkStyle
- Qt Signals & Slots
- QSS (Qt Style Sheets)

---

```text
calculadora/
│
├── main.py
├── main_window.py
├── display.py
├── styles.py
├── utils.py
├── variables.py
│
├── files/
│   └── img_cal_v2.ico
│
└── README.md 
```


Como Executar o Projeto

1️⃣ Clonar o repositório

git clone https://github.com/carlosmathh/Calculadora_Curso.git

cd Calculadora_Curso

2️⃣ Criar ambiente virtual (opcional, recomendado)
python -m venv venv


Windows

venv\Scripts\activate

3️⃣ Instalar dependências
pip install pyside6 qdarkstyle

4️⃣ Executar a aplicação
python main.py

| Tecla     | Função                  |
| --------- | ----------------------- |
| Enter     | Executar cálculo        |
| Backspace | Apagar último caractere |
| Esc       | Limpar tudo             |
| + - * /   | Operadores              |
| P         | Exponenciação (`^`)     |

##  Estrutura do Projeto


Autor

Carlos Matheus

Estudante de Análise e Desenvolvimento de Sistemas

Foco em Python, Banco de Dados e Desenvolvimento Desktop




Link para Download: https://drive.google.com/drive/folders/1QiNKL31K1aoB3Cqv7iPur9c0l7Te0EJH?usp=sharing