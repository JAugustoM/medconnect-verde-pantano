$(document).ready(function(){
    $(".login_box2").click(function(event){
        $(".modal_box_login").removeClass("hidden");
        event.stopPropagation();
    });

    $(".voltar2").click(function(event){
        $(".modal_box_login").addClass("hidden");
        event.stopPropagation();
    });

    $(".link_esqueciSenha").click(function(event){
        $(".modal_login").addClass("hidden");
        $(".modal_esqueciSenha").removeClass("hidden");
        event.stopPropagation();
    });

    $(".voltar3").click(function(event){
        $(".modal_esqueciSenha").addClass("hidden");
        $(".modal_login").removeClass("hidden");
        event.stopPropagation();
    });
    
    $(".message").click(function(event){
        $(".message").hide();
        event.stopPropagation();
    });

    $(".modal_login").click(function(event){
        event.stopPropagation();
    });

    $(".modal_esqueciSenha").click(function(event){
        event.stopPropagation();
    });

    $(".modal_box_login").click(function(){
        $(".modal_box_login").addClass("hidden")
        $(".modal_esqueciSenha").addClass("hidden");
        $(".modal_login").removeClass("hidden");
    });

    if ($(".login").length >= 1) {
        $(".modal_box_login").removeClass("hidden");
    }

});