const btnCalcular = document.getElementById("btn-calcular")
const resultado = document.getElementById("resultado")

btnCalcular.addEventListener("click", () => {
    const peso = document.getElementById("peso").value
    const altura = document.getElementById("altura").value

    const calculo = peso / (altura**2)

    const mensagem = calculo <= 18.5 ? "Abaixo do peso" : "com peso Normal"

    resultado.innerText = `Seu imc é ${calculo.toFixed(2)}, e você está ${mensagem}`
})