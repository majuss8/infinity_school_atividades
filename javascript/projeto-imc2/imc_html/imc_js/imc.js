function clicar() {
let peso = document.getElementById('peso')
let altura = document.getElementById('altura')
let res = document.getElementById('res')
let p = Number.parseFloat(peso.value)
let a = Number.parseFloat(altura.value)


let imcRes = p / (a * a)
let imc = imcRes.toFixed(2)
if(imc < 24.99 && imc > 18.50){
    res.innerHTML="Seu IMC é "+imc+"(Peso ideal)."
}else if(imc < 16){
    res.innerHTML="Seu IMC é "+imc+"(Baixo Peso Grau III)."
}else if(imc < 16.99 && imc > 16){
    res.innerHTML="Seu IMC é "+imc+"(Baixo Peso Grau II)."
}else if(imc < 18.49 && imc > 17){
    res.innerHTML="Seu IMC é "+imc+"(Baixo Peso Grau I)."
}else if(imc < 29.99 && imc > 25){
    res.innerHTML="Seu IMC é "+imc+"(Sobrepeso)."
}else if(imc < 34.99 && imc > 30){
    res.innerHTML="Seu IMC é "+imc+"(Obesidade Grau I)."
}else if(imc < 39.99 && imc > 35){
    res.innerHTML="Seu IMC é "+imc+"(Obesidade Grau II)."
}else if(imc > 40){
   res.innerHTML="Seu IMC é "+imc+"(Obesidade Grau III)."
}

}