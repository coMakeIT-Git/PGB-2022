function up() {
    document.getElementById("pic").style.transform = "rotate(180deg)";


}
function down() {
    document.getElementById("pic").style.transform = "none";

}
function left() {
    document.getElementById("pic").style.transform = "none";
}

function right() {
    document.getElementById("pic").style.transform = "scaleX(-1)";
}