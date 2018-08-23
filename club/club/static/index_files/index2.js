$(function () {

    $(window).scroll(function () {
        if ($(this).scrollTop() > 500) {
            $(".fixed_block").fadeIn(100);
        } else {
            $(".fixed_block").fadeOut(200);
        }
    })
})
;
