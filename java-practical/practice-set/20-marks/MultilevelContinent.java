import java.util.Scanner;

class Continent {
  String continent;

  Continent(String continent) {
    this.continent = continent;
  }
}

class Country extends Continent {
  String country;

  Country(String continent, String country) {
    super(continent);
    this.country = country;
  }
}

class State extends Country {
  String state, place;

  State(String continent, String country, String state, String place) {
    super(continent, country);
    this.state = state;
    this.place = place;
  }

  void display() {
    System.out.println("Place      : " + place);
    System.out.println("State      : " + state);
    System.out.println("Country    : " + country);
    System.out.println("Continent  : " + continent);
  }
}

public class MultilevelContinent {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter Continent: ");
    String cont = sc.nextLine();
    System.out.print("Enter Country: ");
    String cnt = sc.nextLine();
    System.out.print("Enter State: ");
    String st = sc.nextLine();
    System.out.print("Enter Place: ");
    String pl = sc.nextLine();
    new State(cont, cnt, st, pl).display();
    sc.close();
  }
}
