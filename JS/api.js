//making http request to api
function GetApiDetails(){
    
    fetch("https://jsonplaceholder.typicode.com/posts").
    then((message)=>(message.json())).
    then((message)=>console.log(message)).
    catch((message)=>(console.log("error in fetching..",message)))
}
GetApiDetails();


// changing endpoint value
 function GetApiDetails1(){
    
    fetch("https://jsonplaceholder.typicode.com/photos").  // /photos is the end point
    then((message)=>(message.json())).
    then((message)=>console.log(message)).
    catch((message)=>(console.log("error in fetching..",message)))
}
GetApiDetails1();


//writing query params
function GetApiDetails2(){
    
    fetch("https://jsonplaceholder.typicode.com/users?name=Leanne%20Graham").    //last part after users is  query
    then((message)=>(message.json())).
    then((message)=>console.log(message)).
    catch((message)=>(console.log("error in fetching..",message)))
}
GetApiDetails2();



//json vs js obj
let jsObj={
    a:100,
    b:2
};
let json=  JSON.stringify(jsObj);
console.log("java script object :",jsObj);
console.log("after converting to json:",json);
let jsObjFromJSON=JSON.parse(json)                 //converting back to js object
console.log(jsObjFromJSON);