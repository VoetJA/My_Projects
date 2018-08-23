var submitcount = 0;
$('#info_submit').html("注册中，请稍后......<img src='/static/img/site/loading3.gif'  />");
$('#info_submit').hide();
function submitOnce(obj) {
    if (submitcount == 0) {
        submitcount++;
        $('#info_submit').show();
        $('#info_submit').html("注册中，请稍后......<img src='/static/img/site/loading3.gif'  />");
        return true;
    } else {
        return false;
    }
}

function chgUrl(url) {
    var timestamp = (new Date()).valueOf();
    index = url.indexOf("?");
    urlurl = url;
    if (index > 0) {
        urlurl = url.substring(0, index);
    }
    urlurl = urlurl + "?t=" + timestamp;
    return urlurl;
}

//
//
//
$(".verify_code_change").on("click", function () {
    var imgSrc = $("#verify_code");
    var src = imgSrc.attr("src");
    imgSrc.attr("src", chgUrl(src));
});


$("#verify_code_btn").on("click", function () {
    var verifycode = $("#verifycode").val();

    var i = "/account/signup/resend",
        s = {verify_code: verifycode};

    if (!verifycode) {
        $("#verifycode_error").html("请输入验证码");
        return;
    }

    var p = (new Date).getTime();
    $("#verifycode_error").html("正在发送....");
    NSB.api.post(i, s, !1, {
        success: function (t) {
            if (t.verify_code_error) {
                $("#verifycode_error").html(t.verify_code_error);
            } else {
                $("#verifycode_error").html("发送成功");
                window.open('/account/signup/resend', '_blank');
            }
        },
        error: function (e) {
            $("#verifycode_error").html("发送失败,请稍后重试");
        }
    });

    var imgSrc = $("#verify_code");
    var src = imgSrc.attr("src");
    imgSrc.attr("src", chgUrl(src));
});