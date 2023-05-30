window.addEventListener("load", function () {
    (function ($) {
        $(document).ready(function () {
          $(".cantidad-input").on("input", function () {
            var row = $(this).closest("tr");
            var cantidad = parseInt($(this).val());
            console.log(cantidad);
            var precio = parseInt(row.find(".materiales-input select option:selected").data("precio"));
            // var precio = 500;
            console.log(precio);
      
            if (!isNaN(cantidad) && !isNaN(precio)) {
              var total = cantidad * precio;
              row.find(".field-get_total .readonly").val(total);
            } else {
              row.find(".field-get_total .readonly").text("Error de cálculo");
            }
          });
        });
      })(django.jQuery);
         
});
