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
if((window.innerWidth >= 400) && (window.innerWidth <= 991)){
    const alturav = document.getElementById("noticia-1").offsetWidth;
    const alturagaleria = document.getElementById("galeria").offsetHeight;

    let alturanoticia = document.getElementById("noticia-2").style.height = alturav - 96 + 'px';
    let alturanoticia1 = document.getElementById("noticia-3").style.height = alturav - 96 + 'px';
    let alturatexto = document.getElementById("galeriatexto").style.height = alturagaleria - 30 + 'px';
}
if(window.innerWidth >= 992){
    const noticia = document.getElementById("noticia-1").offsetHeight;
    let divisor = noticia/13;
    let altura = divisor*6.28;
    const alturagaleria = document.getElementById("galeria").offsetHeight;
    const alturaagenda = document.getElementById("agenda").offsetHeight;
    const anchoopinion = document.getElementById("opinion").clientWidth;
    
    let alturanoticia = document.getElementById("noticia-2").style.height = altura + 'px';
    let alturanoticia1 = document.getElementById("noticia-3").style.height = altura + 'px';
    let alturatexto = document.getElementById("galeriatexto").style.height = alturagaleria - 30 + 'px';
    let alturaobservatorio = document.getElementById("observatorio").style.height = alturaagenda + 16 + 'px';
    let alturaobservatorioimagen = document.getElementsByClassName("articulos__img")[1].style.height = alturaagenda + 16 + 'px';

    let alturaimgopinion = document.getElementsByClassName("altura")
    for(i=0;i<alturaimgopinion.length; i++){
        alturaimgopinion[i].style.height = anchoopinion + 'px';
    }

    let alturaopinionimagen = document.getElementsByClassName("agenda__img--altura")
    for(i=0;i< alturaopinionimagen.length; i++){
        alturaopinionimagen[i].style.height = anchoopinion  +'px';
    }
}