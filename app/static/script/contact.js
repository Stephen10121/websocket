$(document).ready(function(){
    $("#contact-search-input").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $(".contact-list center button").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
});
