//Introducing the constants necessary for the buttons

const myName = document.getElementById("myName");
const username = document.getElementById("username");
const saveName = document.getElementById("saveName");
const mySelf = document.getElementById("mySelf");
const myPresent = document.getElementById("myPresent");
const presentForm = document.getElementById("presentForm");


// introducing the methods

function saveUsername(){
    const newParagraph = document.createElement("h3");
    newParagraph.className = "paragraphStyle";
    newParagraph.innerText = "Welcome to your DC List " + myName.value + " !";
    username.appendChild(newParagraph);
    username.removeChild(presentForm);
    // Introducing the local storage
    const itempara = document.getElementsByClassName("paragraphStyle");
     
    if (itempara.length > 0){
        localStorage.setItem("username", myName.value);

    }
}

function loadname(){
    const storedName = localStorage.getItem("username");
    const newParagraph = document.createElement("h3");
    newParagraph.className = "paragraphStyle";
    if (storedName != null){
        newParagraph.innerText = "Welcome back "+ storedName + " !";
        username.appendChild(newParagraph);
        username.removeChild(presentForm);

    }
}

//Introducing the eventlistener

saveName.addEventListener("click", saveUsername);
document.addEventListener("DOMContentLoaded",function(){
    loadname()
});