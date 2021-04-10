// Package
package me.MASTRIO.JustAnotherGameAboutCheese;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

// Class
public class CommandList {

  // Variables
  static String saveOutput = "Attempting to save the game:";
  static String saveInfo = "";
  static int idLoad = 0;
  static String loadOutput = "";

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

  // Buy Command Method
  public static void cBuy() {

    // Sell
    if (CommandCompiler.commandArgs[0].equals("buy")) {

      // OUTPUT
      ItemAPI.defineItems("buy");

      UI.outputText("Buying " + CommandCompiler.commandArgs[2] + " " + CommandCompiler.commandArgs[1], ItemAPI.sellOutput);

    }

  }

  // Help Command Method
  public static void cHelp() {

    // Help
    if (CommandCompiler.commandArgs[0].equals("help")) {

      // OUTPUT
      UI.outputText("Showing the user the command options", "> help    (Shows this list)\n> balance   (Shows your money)\n> inventory    (Shows your inventory)\n> sell <item> <amount>   (Sell your items)\n> buy <item> <amount>   (Buy items)");

    }

  }

  // Data Command Method
  public static void cData() {

    // Data
    if (CommandCompiler.commandArgs[0].equals("data")) {

      // Save
      if (CommandCompiler.commandArgs[1].equals("save")) {

        // OUTPUT
        // Create save file
        try {

          File saveFiles = new File("saveData.cheese");

          if (saveFiles.createNewFile()) {

            saveOutput = saveOutput;

          } else {

            saveOutput = saveOutput + "\n> Rewriting existing save file";

          }

        } catch (IOException e) {

          System.out.println("uh oh error go brrrrrrrrrrrrrrrrrrr");
          e.printStackTrace();

        }

        // Save Data
        try {

          ItemAPI.defineItems("save");
          FileWriter saveData = new FileWriter("saveData.cheese");
          saveData.write(Resources.currency[0] + "\n" + saveInfo);
          saveData.close();
          saveOutput = saveOutput + "\n> Saved the data";

        } catch (IOException e) {

          System.out.println("uh oh an error occured pog");
          e.printStackTrace();

        }

        // Sent Output
        UI.outputText("Saved Game Data", saveOutput);

      }
      // Load
      if (CommandCompiler.commandArgs[1].equals("load")) {

        // OUTPUT
        idLoad = -1;

        try {

          File saveFiles = new File("saveData.cheese");
          Scanner saveReader = new Scanner(saveFiles);

          while (saveReader.hasNextLine()) {

            if (idLoad == -1) {

              Resources.currency[0] = Integer.parseInt(saveReader.nextLine());

            } else {

              Resources.items[idLoad] = Integer.parseInt(saveReader.nextLine());
              loadOutput = loadOutput + Resources.items[idLoad] + "\n";

            }

            idLoad++;

          }

          UI.outputText("Loading Game Data", "Loading Game Data:\n" + loadOutput);

          saveReader.close();

        } catch (FileNotFoundException e) {

          System.out.println("Errors are bad");
          e.printStackTrace();

        }

      }

    }

  }

}
