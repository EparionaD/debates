//Cambiar de color la barra de menu
window.onscroll = function(){
    const scroll = document.documentElement.scrollTop || document.body.scrollTop
    if(scroll > 50){
        document.getElementById("menu").classList.add('menuprincipal--color')
    }else{
        document.getElementById("menu").classList.remove('menuprincipal--color')
    }
}
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
//Calcular tamaño de las ventanas en el munu inicio
if((window.innerWidth >= 300) && (window.innerWidth <= 991)){
    const alturav = document.getElementById("noticia-1").offsetWidth;
    console.log(alturav)

    let alturanoticiafirst = document.getElementById("noticia-1").style.height = alturav - 106 + 'px';
    let alturaimgfirst = document.getElementById("img-first").style.height = alturav - 106 + 'px';
    let alturanoticia = document.getElementById("noticia-2").style.height = alturav - 106 + 'px';
    console.log(alturanoticia)
    let alturanoticia1 = document.getElementById("noticia-3").style.height = alturav - 106 + 'px';
}
if(window.innerWidth >= 992){
    const noticia = document.getElementById("noticia-1").offsetHeight;
    let divisor = noticia/13;
    let altura = divisor*6.28;

    
    let alturanoticia = document.getElementById("noticia-2").style.height = altura + 'px';
    let alturanoticia1 = document.getElementById("noticia-3").style.height = altura + 'px';
}