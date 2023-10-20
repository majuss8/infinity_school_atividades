const root = document.getElementById("root")

const objetos = [
    {"id": 1, "email": "email@email.com", "senha": "senha123"},
    {"id": 2, "email": "email2@gmail.com", "senha": "123senha"},
    {"id": 3, "email": "email33@gmail.com", "senha": "321senha"}
]

const tableBody = objetos.map((objetos) => {
    return `<tr>
    <td>${objetos.id}</td>
    <td>${objetos.email}</td>
    <td>${objetos.senha}</td>
    </tr>`
}).join('')

const table = `<table>
    <tr>
    <td>ID</td>
    <td>EMAIL</td>
    <td>SENHA</td>
    </tr>
    ${tableBody}
    </table>`;

root.insertAdjacentHTML('beforeend', table)


