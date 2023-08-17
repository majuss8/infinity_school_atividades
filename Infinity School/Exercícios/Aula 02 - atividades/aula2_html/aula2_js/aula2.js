// Q. 07
// let nome = String(prompt('Informe seu nome: '))
// let idade = Number(prompt('Informe sua idade: '))
// if (idade <= 10) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$30,00`)
// }else if (idade <=29) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$60,00`)
// }else if (idade <=45) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$120,00`)
// }else if (idade <=59) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$150,00`)
// }else if (idade <=65) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$250,00`)
// }else if (idade > 65) {
//     alert(`Nome: ${nome}\nIdade: ${idade}\nValor do plano de saúde: R$400,00`)
// }else{
//     alert('Coloque os dados corretamente')
// }

// Q. 08
// let saldoMedio = Number(prompt('Informe seu saldo médio: ')) 
// let credito3 = (saldoMedio * 50) / 100
// if (saldoMedio > 0 && saldoMedio <= 500){
//     alert(`Você não possui crédito`)
// }else if (saldoMedio <= 1000){
//     let credito1 = (saldoMedio * 30) / 100
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito1.toFixed(2)}`)
// }else if (saldoMedio <= 3000){
//     let credito2 = (saldoMedio * 40) / 100
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito2.toFixed(2)}`)
// }else if (saldoMedio > 3000){
   
//     alert(`Saldo Médio: R$${saldoMedio}\nValor do Crédito: R$${credito3.toFixed(2)}`)
// }else{
//     alert('Coloque os dados corretamente')
// }

// Q. 09
// let j1 = Number(prompt('Número de pontos do Jogador 1: '))
// let j2 = Number(prompt('Número de pontos do Jogador 2: '))
// let j3 = Number(prompt('Número de pontos do Jogador 3: '))
// let soma = j1 + j2 + j3
// let media = soma / 3
// let aux = j1
// if (j2 > j1){
//     aux = j2;
//     j2 = j1;
//     j1 = aux;
// }
// if (j3 > j1){
//     aux = j3;
//     j3 = j1;
//     j1 = aux;
// }
// if (j3 > j2){
//     aux = j3;
//     j3 = j2;
//     j2 = aux;
// }
// if (soma > 100){
//     alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nMédia de pontos da equipe: ${media.toFixed()}`)
// }else{
//     alert(`1° - Jogador 1: ${j1} pontos\n2° - Jogador 2: ${j2} pontos\n3° - Jogador 3: ${j3} pontos\nTotal de pontos: ${soma}\nEquipe Desclassificada!`)
// }

// BÔNUS
// let prato = Number(prompt('Informe seus pedidos: \n*** PRATOS ***\n1 - Vegetariano (180cal)\n2 - Peixe (230cal)\n3 - Frango (250cal)\n4 - Carne (350cal)'))
// let sobremesa = Number(prompt('*** SOBREMESAS ***\n1 - Abacaxi (75 cal)\n2 - Sorvete diet (110cal)\n3 - Mousse diet (170cal)\n4 - Mousse de chocolate (200cal)'))
// let bebida = Number(prompt('*** BEBIDAS ***\n1 - Chá (20cal)\n2 - Suco de laranja (70cal)\n3 - Suco de melão (100cal)\n4 - Refrigerante diet (65cal)'))
// if (prato == 1){
//     prato = 180
// }else if (prato == 2){
//     prato = 230
// }else if (prato == 3){
//     prato = 250
// }else if (prato == 4){
//     prato = 350
// }else{
//     alert('Número inválido')
// }
// if (sobremesa == 1){
//     sobremesa = 75
// }else if (sobremesa == 2){
//     sobremesa = 110
// }else if (sobremesa == 3){
//     sobremesa = 170
// }else if (sobremesa == 4){
//     sobremesa = 200
// }else{
//     alert('Número inválido')
// }
// if (bebida == 1){
//     bebida = 20
// }else if (bebida == 2){
//     bebida = 70
// }else if (bebida == 3){
//     bebida = 100
// }else if (bebida == 4){
//     bebida = 65
// }else{
//     alert('Número inválido')
// }
// let totalCal = prato + sobremesa + bebida
// alert(`O total de calorias da sua refeição foi ${totalCal}`)




