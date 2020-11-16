//Cambiar de color la barra de menu
document.getElementById("menu").classList.add('menuprincipal--color')
//Posicionar buscador
let menu = document.getElementById("menu");
let tamanomenu = menu.getBoundingClientRect();
let alturamenu = tamanomenu.height;

let topmenu = document.getElementById("buscar").style.top = alturamenu + 5 +'px';

//Botón de buscar
function aparecer(){
    let buscador = document.getElementById("buscar");
    if(buscador.style.display == "none"){
        document.getElementById("buscar").style.display = "block";
        document.getElementById("buscar").classList.add('animate__fadeIn');
    }else{
        document.getElementById("buscar").style.display = "none";
        document.getElementById("buscar").classList.remove('animate__fadeIn');
    }
}