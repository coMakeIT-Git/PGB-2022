let [computer_score,user_score]=[0,0];
let result_ref = document.getElementById("result");
let choices_object = {
    'rock' : {
        'rock' : 'draw',
        'scissor' : 'win',
        'paper' : 'lose'
    },
    'scissor' : {
        'rock' : 'lose',
        'scissor' : 'draw',
        'paper' : 'win'
    },
    'paper' : {
        'rock' : 'win',
        'scissor' : 'lose',
        'paper' : 'draw'
    }

}

function reset(){
    user_score = 0;
    computer_score = 0;
    document.getElementById("computer_score").innerHTML = computer_score;
    document.getElementById("user_score").innerHTML = user_score;
    document.getElementById("result").style = "";
    document.getElementById("result").innerHTML = "";
    document.getElementById("comp_choice").innerHTML = "";
    document.getElementById("user_choice").innerHTML = "";
}

function comparer(input){
    var choices_list = ["rock", "paper", "scissor"];
    let computer_choice = choices_list[Math.floor(Math.random()*3)];

    document.getElementById("comp_choice").innerHTML = 
    ` Computer choice : <span> ${computer_choice.toUpperCase()} </span>`;

    document.getElementById("user_choice").innerHTML = 
    ` Your choice : <span> ${input.toUpperCase()} </span>`;

    switch(choices_object[input][computer_choice]){
        case 'win':
            result_ref.style.cssText = "background-color: green; color: black";
            result_ref.innerHTML = "YOU WIN";
            user_score++;
            break;
        case 'lose':
            result_ref.style.cssText = "background-color: red; color: black";
            result_ref.innerHTML = "YOU LOSE";
            computer_score++;
            break;
        default:
            result_ref.style.cssText = "background-color: grey; color: black";
            result_ref.innerHTML = "DRAW";
            break;
    }
    document.getElementById("computer_score").innerHTML = computer_score;
    document.getElementById("user_score").innerHTML = user_score;
}