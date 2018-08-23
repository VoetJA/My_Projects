function headClick() {
    $(".nav-action-box .dropdown ").hover(
        function () {
            $(".nav-action .user-dropdown-list").show();
        }, function () {
            $(".nav-action .user-dropdown-list").hide();
        }
    );
}

headClick();

$(function () {
    var e = $(".footer"), t = e.find(".go-mobile");
    t.on("click", function () {
        var e = window.location.host.split(".").reverse(),
            t = "." + e[1] + "." + e[0];
        NSB.api.cookie("mobile_request", '1', {expires: 7, domain: t}),
            window.location = window.location.href;
    });

    var isMobile = {
        Android: function () {
            return navigator.userAgent.match(/Android/i) ? true : false;
        },
        BlackBerry: function () {
            return navigator.userAgent.match(/BlackBerry/i) ? true : false;
        },
        iOS: function () {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i) ? true : false;
        },
        Windows: function () {
            return navigator.userAgent.match(/IEMobile/i) ? true : false;
        },
        any: function () {
            return (isMobile.Android() || isMobile.BlackBerry()
            || isMobile.iOS() || isMobile.Windows());
        }
    };
    if (!isMobile.any()) {
        $('.go-mobile').hide();
    }
});