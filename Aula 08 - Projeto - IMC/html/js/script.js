function calcularIMC(){
    let form = document.querySelector('.form');
    let resultado = document.querySelector('.resultado');


    let pessoas = []; //array


function recebeEventoForm(evento){
evento.preventDefault();
   


    let nome = form.querySelector('.nome');
    let sobrenome = form.querySelector('.sobrenome');
    let peso = form.querySelector('.peso');
    let altura = form.querySelector('.altura');


    if(!nome){
        setResultado('Preencha o campo Nome!', false);
        return;
    }if(!sobrenome){
        setResultado('Preencha o campo Sobrenome!', false);
        return;
    }if(!peso){
        setResultado('Preencha o campo Peso!', false);
        return;
    }if(!altura){
        setResultado('Preencha o campo Altura!', false);
        return;
    }


    let imc = getImc(peso.value, altura.value);
    let nivelImc = getNivelIMC(imc);


    pessoas.push({
        nome: nome.value,
        sobrenome: sobrenome.value,
        peso: peso.value,
        altura: altura.value,
        imc: imc,
        nivel: nivelImc
    });


    //Incluir os objetos no array pessoas
    console.log(pessoas)
    //mostrar a mensagem na div resultado
    resultado.innerHTML += '<p>' + nome.value + ' '+ sobrenome.value + ' - Seu IMC é ' + imc + ' kg/m<sup>2</sup> - ' + nivelImc + '</p>';
}


form.addEventListener('submit', recebeEventoForm);
};


function getImc(peso, altura){
    let imc = peso / (altura ** 2);
    return imc.toFixed(2);


}
function getNivelIMC(imc){
    let nivel = ['Abaixo do peso','Peso ideal','Sobrepeso','Obesidade grau I','Obesidade grau II','Obesidade grau III'];
    if(imc < 18.5) return nivel[0];
    if(imc <= 24.9) return nivel[1];
    if(imc <= 29.9) return nivel[2];
    if(imc <= 34.9) return nivel[3];
    if(imc <= 39.9) return nivel[4];
    if(imc > 40) return nivel[5];
}

calcularIMC();

