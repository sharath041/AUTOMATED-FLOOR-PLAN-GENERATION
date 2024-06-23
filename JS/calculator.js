let input1=document.querySelector('#first');
let input2=document.querySelector('#second');
let sumButton=document.querySelector("#sum");
let subractionButton=document.querySelector("#difference");
let multiplicationButton=document.querySelector("#multiplication");
let divisionButton=document.querySelector("#division");
let finalResult=document.querySelector("#finalResult");
let first;
let second;
function getValues(){
    first=Number(input1.value);
    second=Number(input2.value);
}
sumButton.addEventListener("click",()=>{
    getValues();
    finalResult.textContent=first+second;
});
subractionButton.addEventListener("click",()=>{
    getValues();
    finalResult.textContent=first-second;
})
multiplicationButton.addEventListener("click",()=>{
    getValues();
    finalResult.textContent=first*second;
})
divisionButton.addEventListener("click",()=>{
    getValues();
    finalResult.textContent=first/second;
})