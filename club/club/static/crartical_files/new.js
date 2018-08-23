$(document).ready(function () {

    var simplemde = new SimpleMDE({
        element: $("#editor_id")[0],
        spellChecker: false,
        autosave: {
            enabled: true,
            unique_id: "editor_id"
        },
        hideIcons: ["guide", "heading"],
        showIcons: ["code"],
        renderingConfig: {
            singleLineBreaks: false,
            codeSyntaxHighlighting: true
        }
    });

    if ($("#editor_id").val() != "") {
        simplemde.value($("#editor_id").val());
    }

    $("#topic_title").keyup(function (e) {
        var s = $("#topic_title");
        var text = s.val();
        var max = 120;
        var remaining = max - text.length;
        var r = $("#title_remaining");
        r.html(remaining);
    });

    $("#publish_topic").on("click", function () {
        publishTopic();
    });

    function publishTopic() {
        var errors = 0;
        var content_error = $("#content_error");
        content_error.html("");
        var title_error = $("#title_error");
        title_error.html("");
        var em = $("#error_message");
        em.html("");

        // 同步数据后可以直接取得textarea的value
        var content = simplemde.value(); // jQuery

        var title = $("#topic_title").val();

        if (title.length == 0) {
            errors++;
            title_error.html("主题标题不能为空");
            em.html("主题标题不能为空");
        } else if (title.length > 120) {
            errors++;
            title_error.html("主题标题不能超过 120 个字符");
            em.html("主题标题不能超过 120 个字符");
        }

        var POST_MAX_BYTE = 30000;
        if (content.length > POST_MAX_BYTE) {
            errors++;
            content_error.html("主题内容不能超过 " + POST_MAX_BYTE + " 个字符");
            em.html("主题内容不能超过 " + POST_MAX_BYTE + " 个字符");
        }

        if (errors == 0) {
            var input_content = $("#topic_content");
            input_content.val(content);
            var form = $("#compose");
            simplemde.clearAutosavedValue(); // no returned value
            return form.submit();
        }
    }
});


