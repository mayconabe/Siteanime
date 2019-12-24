jQuery(document).ready(function($) {

    $("#setaEsquerda").click(function(){
        $('#scroller').animate( { scrollLeft: '-=1000' }, 500);
    });

    $("#setaDireita").click(function(){
        $('#scroller').animate( { scrollLeft: '+=1000' }, 500);
    });

    $("#setaEsquerda2").click(function(){
        $('#scroller2').animate( { scrollLeft: '-=1000' }, 500);
    });

    $("#setaDireita2").click(function(){
        $('#scroller2').animate( { scrollLeft: '+=1000' }, 500);
    });

    $("#setaEsquerda3").click(function(){
        $('#scroller3').animate( { scrollLeft: '-=1000' }, 500);
    });

    $("#setaDireita3").click(function(){
        $('#scroller3').animate( { scrollLeft: '+=1000' }, 500);
    });

});