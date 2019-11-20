$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('.dropdown-trigger').dropdown();
    $('.modal').modal();
})

var typed = new Typed('.typing', {
    strings: ["Get your best entertaining songs here ...", "Download your favourite songs from all catergories"],
    typeSpeed: 70,
    loop: false,
    backSpeed: 30,
    backDelay: 500,
    startDelay: 1000,
    loop: true,
});