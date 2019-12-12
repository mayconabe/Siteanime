jQuery(document).ready(function($) {

  $("#setaEsquerda").click(function(){
      $('#scroller').animate( { scrollLeft: '-=1000' }, 500);
  });

  $("#setaDireita").click(function(){
      $('#scroller').animate( { scrollLeft: '+=1000' }, 500);
  });

});