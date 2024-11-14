class Product{
    constructor(public name:string, public  price: number){}
}

class cart {
    private products: Map<string, number> = new Map()
    private quantities: Map<string, number> = new Map()

    addProduct(product: Product, quantity: number = 1): void {
        const {name, price } = product
        this.products.set(name, price)
        this.quantities.set(name, (this.quantities.get(name) || 0 + quantity))
        console.log(`added ${quantity} ${name} to cart`);
    }

    removeProduct(productName: string): void {
        if (this.products.has(productName)){
            this.products.delete(productName)
            this.quantities.delete(productName)
            console.log(`Removed ${productName} from cart`)
        }
        console.log(`Product ${productName} not found in Cart`)

    }

    calculateTotal() : number {
        let total = 0;
        this.quantities.forEach(quantity, name) => {
            const price = this.products.get(name)
            if (price != undefined){
                total += price * quantity;
            };
            return total;
        }

    }
}