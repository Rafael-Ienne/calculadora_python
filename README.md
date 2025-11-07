# 🐍 Calculadora Python com Tkinter

Este é um projeto de uma calculadora de desktop simples, mas funcional, desenvolvida em Python utilizando a biblioteca gráfica nativa **Tkinter**.

O projeto combina a lógica de "backend" (as funções de cálculo) e o "frontend" (a interface gráfica) em um único script, demonstrando o uso de widgets do Tkinter, gerenciamento de layout com `.grid()` e a vinculação de funções a eventos de clique de botão.

## 🕹️ Recursos

A calculadora suporta as seguintes operações:

* **Operações Básicas:** Adição (`+`), Subtração (`-`), Multiplicação (`*`), Divisão (`/`)
* **Funções Matemáticas:**
    * Porcentagem (`%`)
    * Raiz Quadrada (`√`)
    * Seno (`sin`)
    * Cosseno (`cos`)
    * Tangente (`tan`)
* **Controle:**
    * Botão **'C'** para limpar o visor.
    * Botão **'='** para avaliar a expressão completa no visor (utilizando `eval()`).
* **Interface:**
    * Visor digital para entrada e saída de valores.
    * Layout de botões intuitivo.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Tkinter**: A biblioteca gráfica padrão do Python.
* **Math**: Biblioteca padrão do Python para as operações matemáticas avançadas (raiz, seno, etc.).

## 🚀 Como Executar

Como o `Tkinter` e o `math` fazem parte da biblioteca padrão do Python, não há necessidade de instalar dependências externas.

1.  Salve o código fornecido em um arquivo com o nome `calculadora.py`.
2.  Abra seu terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o script com o seguinte comando:

    ```bash
    python calculadora.py
    ```

5.  A janela da calculadora será aberta e estará pronta para uso.
