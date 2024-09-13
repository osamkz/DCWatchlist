//Introducing the constants necessary for the buttons

//Button for the username

const myName = document.getElementById("myName");
const username = document.getElementById("username");
const saveName = document.getElementById("saveName");
const mySelf = document.getElementById("mySelf");
const myPresent = document.getElementById("myPresent");
const presentForm = document.getElementById("presentForm");

// button for the watchlist
const addMovie = document.getElementById("addMovie");
const SaveWatch = document.getElementById("SaveWatch");
const addedmovies = document.getElementById("addedmovies");
const watchBox = document.getElementById("watchBox");
const watchForm = document.getElementById("watchForm");
const listofwatch=document.getElementById("listofwatch");


// introducing the methods to register the username in local storage

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

// introducing the methods to register the added Movie in local storage

function displayList(){
    let element = "";
    for (let i = 1; i <= localStorage.length; i++) {
        const key = "Movie " + i.toString();
        stored_elem = localStorage.getItem(key);
        if (stored_elem !== null && stored_elem !== "") {
            element += stored_elem + "\n";
        }

    }
    if (element !== "" ){
        const newDisplaylist = document.createElement("ul");
        newDisplaylist.className = "displayedList";
        const searchexp=/_/gi;
        const replacexp=" ";
        element = element.replace(searchexp,replacexp);
        newDisplaylist.innerText =  element;
        listofwatch.appendChild(newDisplaylist);
        listofwatch.removeChild(addedmovies)
        }
}

//Introducing the eventlistener
//Introducing the case where the display function only works when we are in Index page. 
//Source: https://stackoverflow.com/questions/50692992/how-to-run-a-javascript-function-only-on-a-certain-page-or-pages

if ( window.location.pathname === "/") {
    displayList();
    saveName.addEventListener("click", saveUsername);
    document.addEventListener("DOMContentLoaded",function(){
loadname()
});

    }




