$("#myVideo").ready(function () {
    let height = $("#myVideo").height();
    console.log(height);
    $(".background-transparent").css("height", height + "px");
})

$(document).ready(function () {
// set height of bg block
    $(".close, .nope").on('click', function () {
        $('.modal').addClass('hidden');
        $('.modal-bg').addClass('hidden');
        $('body').addClass('hidden');
    })
    $(".open").on('click', function () {
        $('body').removeClass('hidden');
        $('.modal-bg').removeClass('hidden');
        $('.modal').removeClass('hidden');
    })

});
