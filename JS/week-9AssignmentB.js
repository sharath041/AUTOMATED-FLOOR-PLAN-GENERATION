import { employees } from "./week-9AssignmentA.js";
let hyderabadEmployees=employees.filter(n=>{
    if(n.address.city=='hyderabad'){
        return (n.name);
    }
});
console.log(hyderabadEmployees);

let age1=employees.filter((n)=>{
    if(n.age>40 && n.age<50){
        return n;
    }
})
console.log(age1);



let names1=employees.filter(n=>{
    if(n.address.city!='hyderabad'){
        return n.name;
    }
});
console.log(names1);

let skill=employees.filter(n=>{
    if(n.skills.includes('reactjs')){
        return n.name;
    }
});

console.log(skill);






//let names=hyderabadEmployees.forEach(element => {
  //  return element.name;
//});
//console.log(names)



//let nameAddress=hyderabadEmployees.forEach(element => {
  //  console.log(element.name);
    // console.log(element.address);
// });
