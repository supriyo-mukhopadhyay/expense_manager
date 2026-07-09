$(document).ready(function () {
  // alert("hello");
  // $(function () {
  //   $("#date").datepicker();
  // });

  $("#category").change(function () {
    $("#other").attr("type", "hidden");
    let othercat = $($("#category")).val();
    if (othercat === "other") {
      $("#other").attr("type", "text");
    }
  });
});
