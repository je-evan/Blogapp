setTimeout(function () {
    $("#message").fadeOut();
}, 5000);

function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}

function toggleIcon(element) {
    $(element).removeClass("fa-regular fa-copy text-primary").addClass("fa-solid fa-check text-success")
}