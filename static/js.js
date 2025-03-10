let bt = document.getElementById('dashboard');
let idPersist = ''

function changeBackgroundButtonSidebar(id) {
    idPersist = id
    document.getElementById(idPersist).style.backgroundColor = '#212529'
}

function changeIcon(nameClass) {
    document.getElementsByClassName(nameClass)
}