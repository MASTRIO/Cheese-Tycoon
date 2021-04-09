// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

// Class
public class ItemAPI {

  // Variables
  static String inventoryOutput = "Here is your inventory:\n";
  static String sellOutput;

  // Define Items
  public static void defineItems(String accessType) {

    newItem(accessType, "shiny_gems", "Shiny Gems", 0, "✨💎", 10, 15);
    newItem(accessType, "cheese_jumpers", "Cheese Jumpers", 1, "🧀🥋", 40, 45);

  }

  // New Item Method
  public static void newItem(String accessType, String code_name, String name, int id, String icon, int sellPrice, int buyPrice) {

    // Inventory
    if (accessType.equals("inventory")) {

      // OUTPUT
      inventoryOutput = inventoryOutput + "> [" + icon + "] " + Resources.items[id] + " | " + name + "\n";

    }
    // Sell
    if (accessType.equals("sell")) {

      // OUTPUT
      if (CommandCompiler.commandArgs[1].equals(code_name) && (Resources.items[id]) > (Integer.parseInt(CommandCompiler.commandArgs[2]))) {

        // OUTPUT
        // How much you sold
        sellOutput = "You sold " + CommandCompiler.commandArgs[2] + " " + icon + " For " + (Integer.parseInt(CommandCompiler.commandArgs[2]) * sellPrice + " 🧀\n");

        // Sell Stuff
        Resources.items[id] = Resources.items[id] - Integer.parseInt(CommandCompiler.commandArgs[2]);
        Resources.currency[0] = Resources.currency[0] + (Integer.parseInt(CommandCompiler.commandArgs[2]) * sellPrice);

        // Sellage result
        sellOutput = sellOutput + "You now have " + Resources.items[id] + " " + icon + " and " + Resources.currency[0] + " 🧀";

      }


    }
    // Buy
    if (accessType.equals("buy")) {

      // OUTPUT
      if (CommandCompiler.commandArgs[1].equals(code_name) && (Integer.parseInt(CommandCompiler.commandArgs[2])) < (Resources.currency[0])) {

        // OUTPUT
        // How much you sold
        sellOutput = "You bought " + CommandCompiler.commandArgs[2] + " 🧀 For " + (Integer.parseInt(CommandCompiler.commandArgs[2]) * buyPrice + " " + icon + "\n");

        // Sell Stuff
        Resources.items[id] = Resources.items[id] + Integer.parseInt(CommandCompiler.commandArgs[2]);
        Resources.currency[0] = Resources.currency[0] - (Integer.parseInt(CommandCompiler.commandArgs[2]) * buyPrice);

        // Sellage result
        sellOutput = sellOutput + "You now have " + Resources.currency[0] + " 🧀 and " + Resources.items[id] + " " + icon;

      }


    }

  }

}
