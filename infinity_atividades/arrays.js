let numInt = [2, 6, 8, 45, 100, 67, 84, 38, 29, 78]

function lista(){
    function arrayNax(numInt){
        return Math.max.apply(null, numInt)
    }
    function arrayMin(numInt){
        return Math.min.apply(null, numInt)
    }

    return console.log(`Maior número: ${arrayNax(numInt)} \nMenor número: ${arrayMin(numInt)}`);
}

lista()
