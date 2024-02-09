interface WaterVehicle {
    void sail();
}

interface LandVehicle {
    void drive();
}

// This class implements both interfaces, achieving multiple inheritance-like behavior.
class AmphibiousVehicle implements WaterVehicle, LandVehicle {
    public void sail() {
        System.out.println("Sailing on water.");
    }

    public void drive() {
        System.out.println("Driving on land.");
    }
}