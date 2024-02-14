$(document).ready(function(){
    $.fn.select2.defaults.set("allowClear", "true");

    /*$(".select-uf").select2({
        placeholder: 'UF',
    });

    $(".select-municipio").select2({
        placeholder: 'Cidade/Município',
    });

    $(".select-especialidade").select2({
        placeholder: 'Especialidade',
    });*/

    $(".select-categoria").select2({
        placeholder: 'Categoria',
    });
});