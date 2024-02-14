$(document).ready(function(){
    var interval = window.setInterval(rotateSlides, 6000)

    function rotateSlides() {
        var $firstSlide1 = $('#lista_hospitais').find('.slide:first');
        var width1 = $firstSlide1.width();

        $firstSlide1.animate({marginLeft: -width1}, 1000, function(){
            var $lastSlide1 = $("#lista_hospitais").find(".slide:last");
            $lastSlide1.after($firstSlide1);
            $firstSlide1.css({marginLeft: 20})
        })

        var $firstSlide2 = $('#lista_news').find('.slide_news:first');
        var width2 = $firstSlide2.width();

        $firstSlide2.animate({marginLeft: -width2}, 1000, function(){
            var $lastSlide2 = $("#lista_news").find(".slide_news:last");
            $lastSlide2.after($firstSlide2);
            $firstSlide2.css({marginLeft: 20})
        }) 
    }
    $('#arrow_left1').click(previousSlide1);
    $('#arrow_right1').click(nextSlide1);
    // $('.slide').click(nextSlide1);
    

    function nextSlide1(){
        window.clearInterval(interval);
        var $currentSlide1 = $('#lista_hospitais').find('.slide:first');
        var width1 = $currentSlide1.width();
        $currentSlide1.animate({marginLeft: -width1}, 1000, function(){
            var $lastSlide1 = $('#lista_hospitais').find('.slide:last')
            $lastSlide1.after($currentSlide1);
            $currentSlide1.css({marginLeft: 20})
            interval = window.setInterval(rotateSlides, 6000);
        });
    }

    function previousSlide1(){
        window.clearInterval(interval);
        var $currentSlide1 = $("#lista_hospitais").find('.slide:first');
        var width1 = $currentSlide1.width();
        var $previousSlide1 = $('#lista_hospitais').find('.slide:last')
        $previousSlide1.css({marginLeft: -width1})
        $currentSlide1.before($previousSlide1);
        $previousSlide1.animate({marginLeft: 20}, 1000, function(){
            interval = window.setInterval(rotateSlides, 3000);
        });
    }

    $('#arrow_left2').click(previousSlide2);
    $('#arrow_right2').click(nextSlide2);
    // $('.slide_news').click(nextSlide2);

    function nextSlide2(){
        window.clearInterval(interval);
        var $currentSlide2 = $('#lista_news').find('.slide_news:first');
        var width2 = $currentSlide2.width();
        $currentSlide2.animate({marginLeft: -width2}, 1000, function(){
            var $lastSlide2 = $('#lista_news').find('.slide_news:last')
            $lastSlide2.after($currentSlide2);
            $currentSlide2.css({marginLeft: 20})
            interval = window.setInterval(rotateSlides, 3000);
        });
    }

    function previousSlide2(){
        window.clearInterval(interval);
        var $currentSlide2 = $("#lista_news").find('.slide_news:first');
        var width2 = $currentSlide2.width();
        var $previousSlide2 = $('#lista_news').find('.slide_news:last')
        $previousSlide2.css({marginLeft: -width2})
        $currentSlide2.before($previousSlide2);
        $previousSlide2.animate({marginLeft: 20}, 1000, function(){
            interval = window.setInterval(rotateSlides, 3000);
        });
    }

    $(".btn-info-class").click(function(){
        $("#info-class-urg").addClass("on");
    })
    $("#close").click(function(){
        $("#info-class-urg").removeClass("on");
    }) 
});
$(window).scroll(function() {
    if ($(this).scrollTop() > 1){  
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