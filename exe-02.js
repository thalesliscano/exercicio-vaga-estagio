//2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


let primeiroValor = 0;
let segundoValor = 1;
let input = 233;

console.log(0)
for (let i = 0; i >= 0; i++) {

    // Atualiza os valores para a próxima iteração
    let temp = segundoValor;
    segundoValor += primeiroValor;
    primeiroValor = temp;
    console.log(primeiroValor);  // Exibe o valor atual da sequência

    // Verifica se o próximo valor seria o input (233) antes de somá-lo à sequência
    if (segundoValor === input) {
        console.log("Está na sequência, próximo valor seria:", segundoValor);
        break;
    }
}


