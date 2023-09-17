// fetch("https://jsonplaceholder.typicode.com/posts").then(response => {
//     return response.json()
// }).then(json => {
//     console.log(json);
// })

// funcao assincrona

const ulElement = document.querySelector("ul")
async function getPosts() {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts")
    const json = await response.json()

    let lista = ""

    json.forEach(element => {
        lista += `<li>${element.title}</li>`
    });

    ulElement.innerHTML = lista
    
}

getPosts()