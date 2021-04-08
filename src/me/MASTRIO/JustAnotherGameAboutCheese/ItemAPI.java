// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

// Class
public class ItemAPI {

  // Variables
  static String inventoryOutput = "Here is your inventory:\n";
  static String sellOutput;

  // Define Items
  public static void defineItems(String accessType) {

    newItem(accessType, "shiny_gems", "Shiny Gems", 0, "✨💎", 30, 40);
    newItem(accessType, "cheese_jumpers", "Cheese Jumpers", 1, "🧀🥋", 90, 100);

  }

  // New Item Method
  public static void newItem(String accessType, String code_name, String name, int ID, String icon, int sellPrice, int buyPrice) {

    // Inventory
    if (accessType.equals("inventory")) {

      // OUTPUT
      inventoryOutput = inventoryOutput + "> [" + icon + "] " + Resources.items[ID] + " | " + name + "\n";

    }
    // Sell
    if (accessType.equals("sell")) {

      // OUTPUT
      if (CommandCompiler.commandArgs[1].equals(code_name)) {

        // OUTPUT
        sellOutput = "You sold " + CommandCompiler.commandArgs[2] + " " + icon + " For " + (Integer.parseInt(CommandCompiler.commandArgs[2]) * sellPrice + " 🧀");

      }


    }

  }

}
