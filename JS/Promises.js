let preperation='Good';
console.log("Promise of getting full marks is made");
let gettingFullMarks= new Promise((fullfilled,rejected)=>
{    setInterval(()=>{
        if(preperation=='Good'){
        fullfilled("Got full marks");
        }
        else{
        rejected("Did not got full marks");
        }
    },5000);
} );

gettingFullMarks.then(
    (result)=>console.log('result is:',result)
).catch((result)=>console.log('result is:',result))