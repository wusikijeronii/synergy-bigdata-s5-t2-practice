import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Car {
    String brand;
    String model;
    int year;
    String engine;
    int horsepower;
    double price;

    Car(String brand, String model, int year, String engine, int horsepower, double price) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.engine = engine;
        this.horsepower = horsepower;
        this.price = price;
    }

    void printInfo() {
        System.out.println("\nCar info:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
        System.out.println("Engine: " + engine);
        System.out.println("Horsepower: " + horsepower + " hp");
        System.out.println("Average price: $" + price);
    }
}

public class CarInfoApp {

    private static final Map<String, Car> carDatabase = new HashMap<>();

    static {
        carDatabase.put("toyota_camry_2020",
                new Car("Toyota", "Camry", 2020, "2.5L", 200, 25000));

        carDatabase.put("bmw_x5_2019",
                new Car("BMW", "X5", 2019, "3.0L", 300, 45000));

        carDatabase.put("audi_a4_2018",
                new Car("Audi", "A4", 2018, "2.0L", 190, 22000));

        carDatabase.put("tesla_model3_2021",
                new Car("Tesla", "Model 3", 2021, "Electric", 283, 35000));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Car Info App");

        System.out.print("Enter brand: ");
        String brand = scanner.nextLine().toLowerCase();

        System.out.print("Enter model: ");
        String model = scanner.nextLine().toLowerCase();

        System.out.print("Enter year: ");
        int year = scanner.nextInt();

        String key = brand + "_" + model + "_" + year;

        Car car = carDatabase.get(key);

        if (car != null) {
            car.printInfo();
        } else {
            System.out.println("\nCar not found in database.");
        }

        scanner.close();
    }
}