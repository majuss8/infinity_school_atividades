let peso = Number($("#peso")("Peso: "))
let altura = Number($("#altura")("Altura: "))
let imc = peso / (altura * altura)
if(imc < 24.99 && imc > 18.50){
    $("#enviar").document.write("Seu IMC é "+imc+"(Peso ideal).")
}else if(imc < 16){
    document.write("Seu IMC é "+imc+"(Baixo Peso Grau III).")
}else if(imc < 16.99 && imc > 16){
    document.write("Seu IMC é "+imc+"(Baixo Peso Grau II).")
}else if(imc < 18.49 && imc > 17){
    document.write("Seu IMC é "+imc+"(Baixo Peso Grau I).")
}else if(imc < 29.99 && imc > 25){
    document.write("Seu IMC é "+imc+"(Sobrepeso).")
}else if(imc < 34.99 && imc > 30){
    document.write("Seu IMC é "+imc+"(Obesidade Grau I).")
}else if(imc < 39.99 && imc > 35){
    document.write("Seu IMC é "+imc+"(Obesidade Grau II).")
}else if(imc > 40){
    document.write("Seu IMC é "+imc+"(Obesidade Grau III).")
}