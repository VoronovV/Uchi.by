//"use strict"
console.log("asdasd");
const btnEnt = document.getElementById("ent");
let btnRegistration = document.getElementById("reg");
let section = document.querySelector("cover").addEventListener("click", hideModal);





//btnRegistration.onclick = function() {
//    section.style.display = "block";
//}
//btnEnt.onclick = function() {
//    section.style.display = "block";
//}
if(btnRegistration){
    btnRegistration.addEventListener("click", function(){section.style.display = "block";})
}

if(btnEnt){
console.log("qwe");
btnEnt.addEventListener("click", function(){section.style.display = "block";})
}
if(section){
console.log("qwe");
section.addEventListener("click", hideModal);
}
function hideModal() {
    section.style.display = "none";
}