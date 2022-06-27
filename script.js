var text=document.getElementById('change');
var button1=document.getElementById('b1');
var button2=document.getElementById('b2');

button1.onclick=function(){
    text.innerHTML='You have clicked button-1';
};

button2.onclick=function(){
    text.innerHTML='You have clicked button-2';
};
