// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

// Class
public class ItemAPI {

  // Variables
  static String inventoryOutput = "Here is your inventory:\n";

  // New Item Method
  public static void newItem(String accessType, String name, int iD, String icon, int amount, int sellPrice, int buyPrice) {

    // Inventory
    if (accessType.equals("inventory")) {

      // OUTPUT
      inventoryOutput = inventoryOutput + ">  [" + icon + "]  " + amount + "  |  " + name + "\n";

    }

  }

}
