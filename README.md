# 🤖 CHAD — Controlador Humanoide Articulado de Dança
**Equipe:**

- Cauan Lemos Souza — RA: 2402120
- Filipe Vale Moreira — RA: 2401241
- Gabriel Macedo de Araujo Vieira — RA: 2401585
- Guilherme Pinheiro dos Santos — RA: 2401832

Projeto desenvolvido para a disciplina de **Robótica**, utilizando o **LEGO Mindstorms EV3** e programação em **Python**.

O **CHAD (Coreógrafo Humanoide Articulado de Dança)** é um robô desenvolvido para executar uma coreografia automatizada, utilizando motores para movimentar suas pernas e braços, além de um sensor de toque para iniciar a apresentação.

---

## 🎯 Objetivo do Projeto

O **CHAD** foi desenvolvido para demonstrar a integração entre:

- 🤖 Robótica
- 🐍 Programação em Python
- ⚙️ Controle de motores
- 👆 Sensores
- 🔄 Estruturas de repetição
- 🧩 Organização do código em funções

Ao pressionar o sensor de toque, o robô inicia automaticamente uma sequência de movimentos, realizando uma coreografia com os braços e as pernas.

---

## 🛠️ Tecnologias e Componentes

### 💻 Software

- **Python**
- **ev3dev2**
- **LEGO Mindstorms EV3**

### 🤖 Componentes utilizados

| Componente | Porta | Função |
|---|---|---|
| Motor grande — Perna direita | B | Movimento da perna direita |
| Motor grande — Perna esquerda | C | Movimento da perna esquerda |
| Motor médio — Braços | A | Movimento dos braços |
| Sensor de toque | 1 | Iniciar a dança |

---

## ⚙️ Funcionamento

O funcionamento do CHAD pode ser resumido em quatro etapas:

```text
        ┌──────────────────────┐
        │ Inicialização do EV3 │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Aguarda o sensor     │
        │ de toque             │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Sensor pressionado   │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Executa a coreografia│
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Libera os motores    │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Aguarda novo toque   │
        └──────────────────────┘



https://github.com/user-attachments/assets/a4fb16c3-1c23-4ded-9d28-d3cd20273304


<img width="900" height="1600" alt="Imagem do prototipo construido" src="https://github.com/user-attachments/assets/cad8e4d8-c33f-455e-923e-f38c39aa637c" />


<img width="1200" height="1600" alt="Inicio da construção do prototipo" src="https://github.com/user-attachments/assets/9f938b7a-f220-4154-994d-a1131418ec07" />



