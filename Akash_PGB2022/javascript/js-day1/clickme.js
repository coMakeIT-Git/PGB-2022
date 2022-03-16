

function onIncrementCount() {
    let counterE = document.getElementById("counterValue");
    let clickCount = localStorage.getItem("clickCount");
    if (clickCount === null) {
        counterE.textContent = 0;
    } else {
        counterE.textContent = clickCount;
    }
    let c = counterE.textContent;
    let d = parseInt(c) + 1;
    localStorage.setItem("clickCount", d);
    counterE.textContent = d;
}


