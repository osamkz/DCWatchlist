//Introducing the constants necessary for the buttons
// button for the watchlist
const addMovie = document.getElementById("addMovie");
const SaveWatch = document.getElementById("SaveWatch");
const addedmovies = document.getElementById("addedmovies");
const watchBox = document.getElementById("watchBox");
const watchForm = document.getElementById("watchForm");
const listofwatch=document.getElementById("listofwatch");

// introducing the methods to register the added Movie in local storage
function saveMovie(){
    const newParaforList = document.createElement("h6");
    newParaforList.className = "paraforList";
     // Introducing the local storage
    let itemCount = Object.keys(localStorage).length;
    let movieAdded = false;
         // break when we find an already existing movie added. This will enable the "Already Added message"
    for (let j =1; j<=itemCount; j++){
        const itemnum = "Movie "+j.toString();
        if (localStorage.getItem(itemnum) == addMovie.value){
            movieAdded = true;
            break; 
        }
    }
    if (movieAdded){
        newParaforList.innerText =  "Already Added !";
    }
    else {
        const itemnum = "Movie " + (itemCount + 1).toString();
        localStorage.setItem(itemnum, addMovie.value);
        newParaforList.innerText =  "Added with success !";
    }

    watchBox.appendChild(newParaforList);
    watchBox.removeChild(watchForm);

}

// eventListener for adding the movie in the watchList
//separating the functions for adding the movie and adding the username in different file was a suggestion of AI tool as a way to solve the perturbation of both event listeners
SaveWatch.addEventListener("click", saveMovie);