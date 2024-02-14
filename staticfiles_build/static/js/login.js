$(document).ready(function(){
    $(".login_box").click(function(){
        this.classList.toggle("active");
        var content_account = this.nextElementSibling;
        if (content_account.style.display === "flex") {
            content_account.style.display = "none";
            this.style.borderRadius = "20px";
        } else {
        content_account.style.display = "flex";
        this.style.borderRadius = "20px 20px 0 0";
        }
    });
});
