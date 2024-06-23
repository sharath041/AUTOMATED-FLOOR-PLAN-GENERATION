let product={
    productName:'phone',
    productNo:21193,
    model:'oneplusnord 2t',
    price:30000,
    discountPercentage:10,
    discountPrice:function(){
        return this.price-(this.price*(this.discountPercentage/100));
    }
}
console.log(product.discountPrice())