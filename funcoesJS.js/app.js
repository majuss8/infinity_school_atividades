function somar(n1, n2) {
    return n1 + n2
}

const total = somar(2, 4)

console.log(total);


// Funções Anônimas 
const somar = function(n1, n2) {
    return n1 + n2
}

console.log(somar(1, 2));

// arrow function
const somar = (n1, n2) => {
    return n1 + n2
}

console.log(somar(1, 2));

const pessoa1 = {
    nome: 'Edson',
    anoNasc: 2001
}

const pessoa2 = {
    nome: 'Pedro',
    anoNasc: 2000
}

const calcularIdade = (ano) => {
    return new Date().getFullYear() - ano
}

const exibirPessoa = (pessoa) => {
    const total = calcularIdade(pessoa.anoNasc)
    console.log(`Meu nome é ${pessoa.nome} e tenho ${total} anos.`); 
}

exibirPessoa(pessoa1)
exibirPessoa(pessoa2)