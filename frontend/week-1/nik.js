let x=0;
let btninstead = document.getElementById("btn-instead");
let login = document.getElementById("login");
let head = document.getElementById("head");

function instead(){
    if(x===0){
        x=1;
        btninstead.innerText="Log In Instead";
        head.innerText = "Hi, New User!";
        login.innerText = "Please Sign Up your Account";
    }
    else{
        x=0; 
        btninstead.innerText="Sign Up Instead";
        head.innerText = "Welcome Back, User!";
        login.innerText = "Please Log In to your Account";
    }
}
