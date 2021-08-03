let h1=document.querySelector("#aboutus-title")

let title=h1.textContent
splitText=title.split("")
h1.innerHTML=""
splitText.forEach(element => {
    h1.innerHTML+=`<span class="title">${element}</span>`  
});

let timer=setInterval(onThick,50);
let char=0;

function onThick(){
    let span=h1.querySelectorAll(".title")[char]
    span.classList.add("show")
    char++;
    if(char === splitText.length ){
        clearInterval(timer);
        return;
    }
}


console.log(splitText)