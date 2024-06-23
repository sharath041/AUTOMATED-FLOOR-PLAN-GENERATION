let input=document.querySelector("input");
let result=document.querySelector('h2');
let btn=document.querySelector("button");



btn.addEventListener("click",()=>{

    let number=input.value;
    for(let i=0;i<=number;i++){
        if(number%i==0){
            result.textContent=result.textContent+i+'  ';
        }
    }
})
