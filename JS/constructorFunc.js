function Employee(name,age,basic){
    this.name=name;
    this.age=age;
    this.basic=basic;
}
Employee.prototype.getSalary=function(){
    let da=this.basic*0.1;
    return this.basic+da;
}
let emp1=new Employee('Ravi',32,50000);
let emp2=new Employee('Raju',33,40000);
let emp3=new Employee('Ramesh',32,50000);
let emp4=new Employee('ramu',35,45000);
let emp5=new Employee('Rakesh',39,70000);
console.log(emp1);
console.log(emp2);
console.log(emp3);
console.log(emp4);
console.log(emp5);
console.log(emp1.getSalary());
console.log(emp2.getSalary());
console.log(emp3.getSalary());
console.log(emp4.getSalary());
console.log(emp5.getSalary());



















// second function


class product{
    constructor(brand,price,model,discount){
        this.brand=brand;
        this.price=price;
        this.model=model;
        this.discount=discount;
    }
    discountPrice=function(){
        return this.price-((this.discount/100)*this.price);
    }
}
let product1= new product('oneplus',30000,'nord 2t',5);
let product2= new product('samsung',35000,'M 51',10);
let product3= new product('redmi',20000,'note 12 pro',5);
let product4= new product('nokia',3000,'base',7);
let product5= new product('pixel',40000,'7 a',12);
console.log(product1);
console.log(product2);
console.log(product3);
console.log(product4);
console.log(product5);
console.log(product1.discountPrice());
console.log(product2.discountPrice());
console.log(product3.discountPrice());
console.log(product4.discountPrice());
console.log(product5.discountPrice());