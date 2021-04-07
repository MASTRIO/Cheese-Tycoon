// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

// Class
public class CommandList {

  // COMMANDS
  // Inventory Command Method
  public static void cInventory() {

    // Inventory
    if (CommandCompiler.commandArgs[0].equals("inventory")) {

      // OUTPUT
      ItemAPI.defineItems("inventory");

      UI.outputText("Viewing Inventory", ItemAPI.inventoryOutput);

      ItemAPI.inventoryOutput = "Here is your inventory:\n";

    }

  }

  // Balance Command Method
  public static void cBalance() {

    // Inventory
    if (CommandCompiler.commandArgs[0].equals("balance")) {

      // OUTPUT
      UI.outputText("Viewing Balance", "Here is your balance:\n> You have " + Resources.currency[0] + " [🧀] Cheese");

    }

  }

  // Sell Command Method
  public static void cSell() {

    // Sell
    if (CommandCompiler.commandArgs[0].equals("sell")) {

      // OUTPUT
      ItemAPI.defineItems("sell");

      UI.outputText("Selling " + CommandCompiler.commandArgs[2] + " " + CommandCompiler.commandArgs[1], ItemAPI.sellOutput);

    }

  }

}
