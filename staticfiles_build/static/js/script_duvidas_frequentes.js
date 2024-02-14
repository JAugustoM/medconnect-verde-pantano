//É preciso resumir.
$(document).ready(function(){
  $("#btnPesquisar").click(function(){
   $("#top-bar1").toggle("fast");
   $("#top-bar2").hide("fast");
   $("#top-bar3").hide("fast");
   $("#fechar_aba").show("fast");
  //  $("#numbers_aside").toggleClass("top-bar_on", flip++ % 2 === 0);
  //  $("#navigation_aside").toggleClass("top-bar_on");
  // if ($("#top-bar1").css('display') == 'none'){
  //   $("#numbers_aside").addClass('top_bar_off');
  //   $("#navigation_aside").addClass("top_bar_off"); 
  // }
 });
 if ($("#top-bar1").css('display') == 'none') {
  $("#numbers_aside").css({
    "position": "fixed",
    "top": "100px"
  });
  $("#navigation_aside").css({
    "position": "fixed",
    "top": "100px"
  });
}
 $("#locais_de_atendimento").click(function(){
   $("#top-bar2").toggle("fast");
   $("#top-bar1").hide();
   $("#top-bar3").hide();
   $("#fechar_aba").show("fast");
 });
 $("#outras_duvidas").click(function(){
   $("#top-bar3").toggle("fast");
   $("#top-bar1").hide();
   $("#top-bar2").hide();
   $("#fechar_aba").show("fast");
 });
 $("#fechar_aba").click(function(){
   $("#top-bar1").hide();
   $("#top-bar2").hide();
   $("#top-bar3").hide();
 });
 $(".voltar").click(function(){
   $("#top-bar1").show();
   $("#top-bar2").hide();
   $("#top-bar3").hide();
 });
 $(".login_box").click(function(){
   $("#top-bar1").hide();
   $("#top-bar2").hide();
   $("#top-bar3").hide();
 });  
 $("#topic1").click(function(){
   $("#c1 .question1").toggle();
   $("#c1 .question2").toggle();
   $("#c1 .answer1").hide();
   $("#c1 .answer2").hide();
 });
 $("#c1 .question1").click(function(){
   $("#c1 .question1").addClass("on");
   $("#c1 .answer1").toggle();
 });
 $("#c1 .question2").click(function(){
   $("#c1 .question2").addClass("on");
   $("#c1 .answer2").toggle();
 });
 $("#topic2").click(function(){
   $("#c2 .question1").toggle();
   $("#c2 .question2").toggle();
   $("#c2 .answer1").hide();
   $("#c2 .answer2").hide();
 });
 $("#c2 .question1").click(function(){
   $("#c2 .question1").addClass("on");
   $("#c2 .answer1").toggle();
 });
 $("#c2 .question2").click(function(){
   $("#c2 .question2").addClass("on");
   $("#c2 .answer2").toggle();
 });
 $("#topic3").click(function(){
   $("#c3 .question1").toggle();
   $("#c3 .question2").toggle();
   $("#c3 .answer1").hide();
   $("#c3 .answer2").hide();
 });
 $("#c3 .question1").click(function(){
   $("#c3 .question1").addClass("on");
   $("#c3 .answer1").toggle();
 });
 $("#c3 .question2").click(function(){
   $("#c3 .question2").addClass("on");
   $("#c3 .answer2").toggle();
 });
 $("#topic4").click(function(){
   $("#c4 .question1").toggle();
   $("#c4 .question2").toggle();
   $("#c4 .answer1").hide();
   $("#c4 .answer2").hide();
 });
 $("#c4 .question1").click(function(){
   $("#c4 .question1").addClass("on");
   $("#c4 .answer1").toggle();
 });
 $("#c4 .question2").click(function(){
   $("#c4 .question2").addClass("on");
   $("#c4 .answer2").toggle();
 });
 $("#topic5").click(function(){
  $("#c5 .question1").toggle();
  $("#c5 .question2").toggle();
  $("#c5 .answer1").hide();
  $("#c5 .answer2").hide();
 });
 $("#c5 .question1").click(function(){
   $("#c5 .question1").addClass("on");
   $("#c5 .answer1").toggle();
 });
 $("#c5 .question2").click(function(){
  $("#c5 .question2").addClass("on");
  $("#c5 .answer2").toggle();
 });
});
if ($("#top-bar3").css('visibility') == 'hidden') {
  $("#numbers_aside").css({
    position: "fixed",
    top: "100px"
  });
  $("#navigation_aside").css({
    position: "fixed",
    top: "100px"
  });
}
else{
  $("#numbers_aside").css({
    "position": "fixed",
    "top": "130px"
  });
  $("#navigation_aside").css({
    "position": "fixed",
    "top": "130px"
  });
}
$(window).scroll(function() {
    if($(this).scrollTop() > 1){
      $("#top-bar1").addClass("fixed");
      $("#top-bar2").addClass("fixed");
      $("#top-bar3").addClass("fixed");   
    }
    else{
      $("#top-bar1").removeClass("fixed");
      $("#top-bar2").removeClass("fixed");
      $("#top-bar3").removeClass("fixed");      
    }
});