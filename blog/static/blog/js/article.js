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

let comment=document.querySelector("#comment")
comment.addEventListener("click",()=>{
    document.querySelector("#show-comment").style.display="block"
})
let form= document.querySelector("#comment-form")
form.addEventListener("click",()=>{
    document.querySelector("#show-comment-form").style.display="block"
})