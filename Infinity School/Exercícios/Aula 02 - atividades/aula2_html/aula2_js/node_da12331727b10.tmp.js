// Q, 07
// let nome = String(prompt('Informe seu nome: '))
// let idade = Number(prompt('Informe sua idade: '))
// if (idade <= 10) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$30,00`)
// }else if (idade > 10 && idade <=29) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$60,00`)
// }else if (idade > 29 && idade <=45) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$120,00`)
// }else if (idade > 45 && idade <=59) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$150,00`)
// }else if (idade > 59 && idade <=65) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$250,00`)
// }else if (65 < idade) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$400,00`)
// }else{
//     alert('Coloque os dados corretamente')
// }

// Q. 08
// let saldoMedio = Number(prompt('Informe seu saldo médio: '))
// if (saldoMedio > 0 && saldoMedio <= 500){
//     alert(`Você não possui crédito`)
// }else if (saldoMedio >= 501 && saldoMedio <= 1000){
//     let credito1 = (saldoMedio * 30) / 100
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito1.toFixed(2)}`)
// }else if (saldoMedio >= 1001 && saldoMedio <= 3000){
//     let credito2 = (saldoMedio * 40) / 100
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito2.toFixed(2)}`)
// }else if (saldoMedio >= 3001){
//     let credito3 = (saldoMedio * 50) / 100
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito3.toFixed(2)}`)
// }else{
//     alert('Coloque os dados corretamente')
// }

// Q. 09
// let j1 = Number(prompt('Número de pontos do Jogador 1: '))
// let j2 = Number(prompt('Número de pontos do Jogador 2: '))
// let j3 = Number(prompt('Número de pontos do Jogador 3: '))
// let soma = j1 + j2 + j3
// if (soma > 100){
//     let media = soma / 3
//     if (j1 > j2 && j2 > j3){
//         alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }else if (j1 > j3 && j3 > j2){
//         alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 3: ${j3} pontos\n3° - Jogador 2: ${j2} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }else if (j2 > j1 && j1 > j3){
//         alert(`1° - Jogador 2: ${j2} pontos\n2° - Jogador 1: ${j1} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }else if (j2 > j3 && j3 > j1){
//         alert(`1° - Jogador 2: ${j2} pontos\n2° - Jogador 3: ${j3} pontos\n3° - Jogador 1: ${j1} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }else if (j3 > j1 && j1 > j2){
//         alert(`1° - Jogador 3: ${j3} pontos\n2° - Jogador 1: ${j1} pontos\n3° - Jogador 2: ${j2} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }else if (j3 > j2 && j2 > j1){
//         alert(`1° - Jogador 3: ${j3} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 1: ${j1} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
//     }
// }else{
//     if (j1 > j2 && j2 > j3){
//         alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }else if (j1 > j3 && j3 > j2){
//         alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 3: ${j3} pontos\n3° - Jogador 2: ${j2} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }else if (j2 > j1 && j1 > j3){
//         alert(`1° - Jogador 2: ${j2} pontos\n2° - Jogador 1: ${j1} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }else if (j2 > j3 && j3 > j1){
//         alert(`1° - Jogador 2: ${j2} pontos\n2° - Jogador 3: ${j3} pontos\n3° - Jogador 1: ${j1} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }else if (j3 > j1 && j1 > j2){
//         alert(`1° - Jogador 3: ${j3} pontos\n2° - Jogador 1: ${j1} pontos\n3° - Jogador 2: ${j2} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }else if (j3 > j2 && j2 > j1){
//         alert(`1° - Jogador 3: ${j3} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 1: ${j1} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
//     }
// }
// BÔNUS
var agora = new Date()
var diaSem = agora.getDay()
/*
 Domingo
 Segunda
 Terça
 Quarta
 Quinta
 Sexta
 Sábado
*/
console.log(diaSem)




