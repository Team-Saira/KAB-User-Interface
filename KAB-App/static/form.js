window.onload = function(){
    var hideLocation = document.getElementsByClassName("input-group");
    var i;
    for (i = 0; i < hideLocation.length; i++) {
        hideLocation[i].style.display = 'none';
    }

};


document.addEventListener("click",onClick)
function onClick(){
    var clickCity = document.getElementById('enter-city');
    var clickAddr = document.getElementById('enter-addr');
    var clickCoord = document.getElementById('enter-coord');

    clickCity.onclick = getCity;
    clickAddr.onclick = getAddr;
    clickCoord.onclick = getCoord;

}


function getCity(){
    document.getElementById("btn1").innerHTML = "Submit City";
    
    if (cities.style.display = 'none'){
    cities.style.display = 'block';
    //states.style.display = 'block';
    //if they change the option
    //zips.style.display = 'none';
    //addrCities.style.display = 'none';
    addresses.style.display = 'none';
    latitudes.style.display = 'none';
    longitudes.style.display = 'none';
    ranges.style.display = 'none'
    }
    else {
    }
}

function getAddr(){
    document.getElementById("btn1").innerHTML = "Submit Address";

    if (addresses.style.display = 'none'){
        addresses.style.display = 'block';
        //addrCities.style.display = 'block'
        //zips.style.display = 'block';
        //states.style.display = 'block';
        ranges.style.display = 'block'
        //if they change the option
        latitudes.style.display = 'none';
        longitudes.style.display = 'none';
        cities.style.display = 'none';
    }
    else {
    }

}
function getCoord(){
    document.getElementById("btn1").innerHTML = "Submit Coordinates";
    if (latitudes.style.display = 'none'){
        latitudes.style.display = 'block';
        longitudes.style.display = 'block';
        ranges.style.display = 'block'
        addresses.style.display = 'none';
        cities.style.display = 'none';
        //zips.style.display = 'none';
        //states.style.display = 'none';
    }
    else {
    }
}


