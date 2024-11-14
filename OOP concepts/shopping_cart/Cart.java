import java.util.HashMap;
import java.util.Map;

class Product{
    private String name;
    private double price;

    public Product(String name, double price){
        this.name = name;
        this.price = price;
    }

    public String getName(){
        return this.name;
    }

    public double getPrice(){
        return this.price;
    }
}

class Cart{
    private Map<String, Double> products = new HashMap<>();
    private Map<String, Integer> quantities = new HashMap<>();

    public void addProduct(Product product, int quantity){
        String name = product.getName();
        double price = product.getPrice();

        products.put(name, price);
        quantities.put(name, quantities.getOrDefault(name, 0)+ quantity);
        System.out.println("Added" + quantity + "of" + name + "to cart");

    }

    public void removeProduct(String ProductName){
        if (products.containsKey(ProductName)){
            products.remove(ProductName);
            quantities.remove(ProductName);
            System.out.println("Removed"+ ProductName+ "from cart");
        } else{
            System.out.println("Product not in cart");
        }
    }

    public double calculateTotal(){
        double total = 0;
        for (String name : quantities.keySet()){
            total += products.get(name)*quantities.get(name);
        }
        return total;
    }

    public void showCart(){
        if (products.isEmpty()){
            System.out.println("Your cart is empty");
            return;
        } 
        System.out.println("Cart Contents");
        for (String name : products.keySet()){
            double price = products.get(name);
            int quantity = quantities.get(name);
            System.out.println(name + ": $"+ price + "x" + quantity );
        }
        System.out.println("Total cost:"+ calculateTotal());
    }

    public static void main (String [] args){
       Cart cart = new Cart();
       Product Laptop = new Product("Lenovo", 2100);
       Product Watch = new Product("rolex", 250);

       cart.addProduct(Laptop, 4);
       cart.addProduct(Watch, 3);
       cart.showCart();

       cart.removeProduct("rolex");
       cart.showCart();

    }
}