<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $(document).ready(function () {
    $(".nav-link").click(function (e) {
      e.preventDefault();

      let url = $(this).attr("href");
      $("#loading-popup").fadeIn(200);

      $(".content-wrapper").fadeOut(200, function () {
        $.get(url, function (data) {
          $(".content-wrapper").html($(data).find(".content-wrapper").html()).fadeIn(200);
          $("#loading-popup").fadeOut(200);
        });
      });

      $(".nav-link").removeClass("active");
      $(this).addClass("active");
    });
  });

  window.onload = function() {
    document.getElementById("loading-popup").style.display = "none";
  };
</script>

console.log("Pop-up script loaded");
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM fully loaded");
});
