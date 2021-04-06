// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

// Class
public class CommandList {

  // Define Items
  public static void defineItems(String accessType) {

    ItemAPI.newItem(accessType, Item__ShinyGems.name, Item__ShinyGems.iD, Item__ShinyGems.icon, Item__ShinyGems.amount, Item__ShinyGems.sellPrice, Item__ShinyGems.buyPrice);
    ItemAPI.newItem(accessType, Item__CheeseJumpers.name, Item__CheeseJumpers.iD, Item__CheeseJumpers.icon, Item__CheeseJumpers.amount, Item__CheeseJumpers.sellPrice, Item__CheeseJumpers.buyPrice);

  }

  // COMMANDS
  // Inventory Command Method
  public static void cInventory() {

    // Inventory
    if (CommandCompiler.commandArgs[0].equals("inventory")) {

      // OUTPUT
      defineItems("inventory");

      UI.outputText("Showing the user their inventory", ItemAPI.inventoryOutput);

      ItemAPI.inventoryOutput = "Here is your inventory:\n";

    }

  }

  // Balance Command Method
  public static void cBalance() {

    // Inventory
    if (CommandCompiler.commandArgs[0].equals("balance")) {

      UI.outputText("Showing the user their balance", "Here is your balance:\n> You have " + Currency__Cheese.amount + " [" + Currency__Cheese.icon + "] " + Currency__Cheese.name);

    }

  }

}
