"use strict"
let btnEntrace = document.getElementsByClassName("header-buttons-signIn")[0];
let btnRegistration = document.getElementsByClassName("header-buttons-registration")[0];
let section = document.querySelector(".cover");

btnEntrace.onclick = function() {
    section.style.display = "block";
}

btnRegistration.onclick = function() {
    section.style.display = "block";
}

section.addEventListener("click", hideModal);

function hideModal() {
    section.style.display = "none";
}