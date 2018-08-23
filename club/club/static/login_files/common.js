function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

window.NSB = window.NSB || {};
NSB.api = NSB.api || {};

NSB.api.cookie = function (e, t, i) {
    if ("undefined" == typeof t) {
        var n = null;
        if (document.cookie && "" !== document.cookie) {
            for (var a = document.cookie.split(";"), s = 0; s < a.length; s++) {
                var o = $.trim(a[s]);
                if (o.substring(0, e.length + 1) == e + "=") {
                    n = decodeURIComponent(o.substring(e.length + 1));
                    break
                }
            }
            return n
        }
    }
    i = i || {},
    null === t && (t = "", i.expires = -1);
    var r = "";
    if (i.expires && ("number" == typeof i.expires || i.expires.toUTCString)) {
        var l;
        "number" == typeof i.expires ?
            (l = new Date, l.setTime(l.getTime() + 24 * i.expires * 60 * 60 * 1e3)) :
            l = i.expires, r = "; expires=" + l.toUTCString()
    }
    var d = i.path ? "; path=" + i.path : "", c = i.domain ? "; domain=" + i.domain : "", p = i.secure ? "; secure" : "";
    document.cookie = [e, "=", encodeURIComponent(t), r, d, c, p].join("")
};

NSB.api.getUrlQuery = function (e) {
    var t = new RegExp("(^|&)" + e + "=([^&]*)(&|$)", "i"), i = window.location.search.substr(1).match(t);
    return null !== i ? i[2] : null
};

NSB.api.htmlEncode = function (e) {
    return e ? $("<div />").text(e).html() : e
};

NSB.api.htmlDecode = function (e) {
    return e ? $("<div/>").html(option).text() : e
};

NSB.api.nl2br = function (e) {
    return e ? e.replace(/(\r\n|\n\r|\r|\n)/g, "<br>") : e
};

NSB.api.uriEncode = function (e) {
    return e ? uriEncode(e) : e
};

NSB.api.uriDecode = function (e) {
    return e ? uriEncode(e) : e
};

NSB.api.href = function (e) {
    window.location.href = NSB.api.htmlEncode(e)
};

NSB.api.get = function (e, t, i, n) {
    "undefined" == typeof n && (n = "json"),
        t = t || {},
        t.time = (new Date).getTime(),
        $.get(e, t, function (e) {
                if ("json" === n) {
                    "success" === e.status ?
                    $.isFunction(i.success) &&
                    i.success(e.data, e.redirect_url) :
                    $.isFunction(i.error) && i.error(e.data, e.redirect_url)
                } else
                    $.isFunction(i.success) &&
                    i.success(e.data, e.redirect_url)
            }, n
        )
};

$.ajaxSetup({
    beforeSend: function (e, t) {
        var i = t.type;
        if ("GET" != i && "HEAD" != i && "OPTIONS" != i) {
            var n = /(.+; *)?_xsrf *= *([^;" ]+)/, a = n.exec(document.cookie);
            a && e.setRequestHeader("X-Xsrftoken", a[2])
        }
    }
});

NSB.api.post = function (e, t, i, n) {
    if (i) {
        var a = window.NSB.user, s = parseInt(a.isLogin, 10);
        if (0 === s)return !1
    }
    e += /\?/.test(e) ? "&_t=" + (new Date).getTime() : "?_t=" + (new Date).getTime(),
        $.post(e, t, function (e) {
            "success" === e.status ? $.isFunction(n.success) && n.success(e.data, e.redirect_url) :
            $.isFunction(n.error) && n.error(e.data, e.redirect_url)
        }, "json")
};

NSB.api.jsonp = function (e, t, i, n) {
    $.ajax(
        {
            url: e,
            dataType: "jsonp",
            jsonp: !1,
            jsonpCallback: t,
            data: i,
            success: function (e) {
                "success" === e.status ? $.isFunction(n.success) &&
                n.success(e.data, e.redirect_url) : $.isFunction(n.error) &&
                n.error(e.data, e.redirect_url)
            },
            error: function () {
            }
        }
    )
};

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};
