$(document).ready(function () {
  $(function () {
    $("#date").datepicker({
      dateFormat: "dd-mm-yyyy",
    });
  });

  $("#category").change(function () {
    let attribute = $("#other").attr("type", "hidden");
    let othercat = $(this).val() === "other";

    if (othercat) {
      $("other").attr("type", "text");
    }
  });
});
