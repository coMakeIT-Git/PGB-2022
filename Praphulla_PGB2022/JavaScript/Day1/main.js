
//Choose a random color
const button = document.querySelector('button')
const body = document.querySelector('body')
const colors = ['#d39bab', '#d3a79b', '#d39bc7', '#c7d39b', '#abd39b', '#DAA520', '#FFB6C1', '#BA55D3', '#DDA0DD']
body.style.backgroundColor = 'white'
button.addEventListener('click', changeBackground)

function changeBackground(){
const colorIndex= parseInt(Math.random()*colors.length)
body.style.backgroundColor = colors[colorIndex]
}



