var count1 = 0;
var count2 = 0;
var count3 = 0;
var count4 = 0;
var count5 = 0;
var count6 = 0;
var count7 = 0;
var count8 = 0;

$(document).ready(function(){
   $("#sim1").click(function(){
    $("#answer1").addClass("on");
   });
   $("#sim2").click(function(){
    $("#answer2").addClass("on");
   });
   $("#nao1").click(function(){
    $("#answer1").removeClass("on");
    $('input[name="freq1"]').prop('checked', false).change();               
   });
   $("#nao2").click(function(){
    $("#answer2").removeClass("on");
    $('input[name="freq2"]').prop('checked', false).change(); 
   });
   $("#sim3").click(function(){
    $("#outer_box_doenca_cronica").addClass("on");
   });
   $("#sim4").click(function(){
    $("#outer_box_sintoma").addClass("on");
   });
   $("#sim5").click(function(){
    $("#outer_box_diagnostico").addClass("on");
   });
   $("#sim6").click(function(){
    $("#outer_box_cirurgia").addClass("on");
   });
   $("#sim7").click(function(){
    $("#outer_box_internacao").addClass("on");
   });
   $("#sim8").click(function(){
    $("#outer_condicao_familiar").addClass("on");
    $(".condicao_familiar").addClass("on");
   });
   $("#sim9").click(function(){
    $("#outer_med_cp").addClass("on");
   });
   $("#sim10").click(function(){
    $("#outer_med_sp").addClass("on");
   });
   /*$(".add_condicao_familiar").click(function(){
    $(".condicao_familiar").addClass("on");
   });*/
    $("#nao3").click(function(){
     $("#outer_box_doenca_cronica").removeClass("on");
    });
   $("#nao4").click(function(){
    $("#outer_box_sintoma").removeClass("on");
   });
   $("#nao5").click(function(){
    $("#outer_box_diagnostico").removeClass("on");
   });
   $("#nao6").click(function(){
    $("#outer_box_cirurgia").removeClass("on");
   });
   $("#nao7").click(function(){
    $("#outer_box_internacao").removeClass("on");
   });
   $("#nao8").click(function(){
    $("#outer_condicao_familiar").removeClass("on");
   });
   $("#nao9").click(function(){
    $("#outer_med_cp").removeClass("on");
    $('input[name="freq3"]').prop('checked', false).change(); 
   });
   $("#nao10").click(function(){
    $("#outer_med_sp").removeClass("on");
    $('input[name="freq4"]').prop('checked', false).change(); 
   });
  
  //Gerar novas divs com id's únicas.
  $("body").on("click", ".add_doenca_cronica", function(){
    count1++;
    var $address = $(this).parents('.inner_box_doenca_cronica');
    var nextHtml = $address.clone();
    nextHtml.prop('checked', false); 
    nextHtml.attr('id', 'doenca_cronica' + count1);

    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd1', nextHtml).append(rm);
      $('.add_doenca_cronica', nextHtml).remove(); 
    }
    else {
      $('.add_doenca_cronica', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_box_doenca_cronica').remove();
   });

   $("body").on("click", ".add_sintoma", function(){
    count2++;
    var $address = $(this).parents('.inner_box_sintoma');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'sintoma' + count2);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd2', nextHtml).append(rm);
      $('.add_sintoma', nextHtml).remove();
    }
    else {
      $('.add_sintoma', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_box_sintoma').remove();
   });

   $("body").on("click", ".add_diagnostico", function(){
    count3++;
    var $address = $(this).parents('.inner_box_diagnostico');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'diagnostico' + count3);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd3', nextHtml).append(rm);
      $('.add_diagnostico', nextHtml).remove();
    }
    else {
      $('.add_diagnostico', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_box_diagnostico').remove();
   });

   $("body").on("click", ".add_cirurgia", function(){
    count4++;
    var $address = $(this).parents('.inner_box_cirurgia');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'cirurgia' + count4);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd4', nextHtml).append(rm);
      $('.add_cirurgia', nextHtml).remove();
    }
    else {
      $('.add_cirurgia', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_box_cirurgia').remove();
   });

   $("body").on("click", ".add_internacao", function(){
    count5++;
    var $address = $(this).parents('.inner_box_internacao');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'internacao' + count5);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd5', nextHtml).append(rm);
      $('.add_internacao', nextHtml).remove();
    }
    else {
      $('.add_internacao', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_box_internacao').remove();
   });

   $("body").on("click", ".add_condicao_familiar", function(){
    count6++;
    var $address = $(this).parents('.inner_condicao_familiar');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'condicao_familiar' + count6);
    /*$('.1grau', nextHtml).attr('name', 'parentesco' + count6);
    $('.2grau', nextHtml).attr('name', 'parentesco' + count6);
    $('.3grau', nextHtml).attr('name', 'parentesco' + count6);*/
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd6', nextHtml).append(rm);
      $('.add_condicao_familiar', nextHtml).remove();
    }
    else {
      $('.add_condicao_familiar', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_condicao_familiar').remove();
   });

   $("body").on("click", ".add_med_cp", function(){
    count7++;
    var $address = $(this).parents('.inner_med_cp');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'med_cp' + count7);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd7', nextHtml).append(rm);
      $('.add_med_cp', nextHtml).remove();
    }
    else {
      $('.add_med_cp', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_med_cp').remove();
   });

   $("body").on("click", ".add_med_sp", function(){
    count8++;
    var $address = $(this).parents('.inner_med_sp');
    var nextHtml = $address.clone();
    nextHtml.attr('id', 'med_sp' + count8);
    var hasRmBtn = $('.rmbtn', nextHtml).length > 0;
    if (!hasRmBtn){
      var rm = "<button type='button' class='rmbtn'>Remover</button>";
      $('.addmoreadd8', nextHtml).append(rm);
      $('.add_med_sp', nextHtml).remove();
    }
    else {
      $('.add_med_sp', nextHtml).remove();
    }
    $address.after(nextHtml);
   });
   $("body").on("click", ".rmbtn", function(){
    $(this).parents('.inner_med_sp').remove();
   });

   $("#submit").click(function(){
    $("#submit2").show();
   });


   //Evitar que a página recarregue quando o usuário submeter o formulário;
   /*$(document).on('submit', '#form', function() {
    return false;
   });*/
});
 //Função JQuery para converter valores de inputs para objetos json.
 $.fn.serializeObject = function(){
  var o = {};
  var a = this.serializeArray();
  $.each(a, function() {
      if (o[this.name] !== undefined) {
          if (!o[this.name].push) {
              o[this.name] = [o[this.name]];
          }
          o[this.name].push(this.value || '');
      } else {
          o[this.name] = this.value || '';
      }
  });
  return o;
};

$(function() {
  $('#submit').click(function() {
    $('#result').val()
    $('#result').val(JSON.stringify($('form').serializeObject()));
    return false;
  });
});

//Adicinar imagens para comprovar doenças crônicas.
// function previewFile() {
//   var preview = document.querySelector('.show_doenca_cronica');
//   var file    = document.querySelector('input[type=file]').files[0];
//   var reader  = new FileReader();

//   reader.onloadend = function () {

//     preview.src = reader.result;
//   }

//   if (file) {
//     reader.readAsDataURL(file);
//   } else {
//     preview.src = "";
//   }  
// }