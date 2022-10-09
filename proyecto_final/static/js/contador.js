window.onload = function() {
    setInterval(muestraReloj, 1000);
}
let timeLimit = 10

function muestraReloj() {

    if(timeLimit<=0 ){
        window.location.replace("../homepage")
    }
    updateDisplay(timeLimit--);

}
function updateDisplay(val) {
    document.getElementById("counter-label").innerHTML = `${val} segundos`;
}


