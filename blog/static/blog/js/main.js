
function createArticle(){
    document.querySelector("#create-article-form").style.display="block"
   
}

//Toggle Like

let likeBtn =document.querySelectorAll(".bi")
likeBtn.forEach(element =>{
    element.addEventListener("click",()=>{
        let post_id=element.dataset.id
        let user=element.dataset.user
        let liked=element.attributes.fill.value.trim()==='red' ? true : false;
        
        console.log(user)
        fetch(`toggle_like/${post_id}`,{
            method: "PUT",
            body:JSON.stringify({
                liked :!liked
            })
        });
        
        let like_count=Number(document.querySelector(`#like-count-${post_id}`).innerText);
        if (liked){
            like_count=like_count-1
            document.querySelector(`#like-count-${post_id}`).innerText=`${like_count}`
            element.setAttribute("fill","black")
        }
        else{
            like_count=like_count+1
            document.querySelector(`#like-count-${post_id}`).innerText=`${like_count}`
            element.setAttribute("fill","red")
        }
    })
})

let content=document.querySelectorAll(".content-abb")
content.forEach(element=>{
    
    abbText=element.innerText
    abbText=abbText.split(" ")
    if (abbText.length >20 ){
        result=[]
        for(let i=0;i<20;i++){
            
            result.push(abbText[i])
        }
        console.log(" result: ",result)
        result=result.join(" ")
        
        
        element.innerHTML=`${result} ...`
    }
})
console.log(content.length)

