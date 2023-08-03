$("#toggle_header").click(function() {
    let headderElement = $("header");
    if (headderElement.hasClass("red")) {
        headderElement.removeClass("red");
        headderElement.addClass("green");
    }
    else {
        headderElement.removeClass("green");
        headderElement.addClass("red");
    }
})