//// * Include
#include <iostream>
// Import Scripts
#include "resources.h"
#include "saveData.h"
#include "loadData.h"
#include "resetData.h"
#include "debug.h"

//// * Variables
// hrrrrrrrr
bool gameRunning = true;
// Message Type
std::string messageTypes[4] = {
    "[LOG] ",
    "[ERR] ",
    "[WARN] ",
    "[DEBUG] "
};
// Command Type
std::string commandType;
// Command Inputs
std::string inputCommandStringArg1;
std::string inputCommandStringArg2;
std::string inputCommandStringArg3;
int inputCommandIntArg1;



//// * Functions
// Help
void cHelp() {
    // OUTPUT
    std::cout << "Here is a list of Commands:\n";
    std::cout << "Order: MAIN COMMAND | Argument 1 , Argument 2 , Argument 3\n";
    std::cout << "  - help |\n";
    std::cout << "  - save | save/load/reset\n";
}

// Debug
void cDebug() {
    // Add
    if (inputCommandStringArg1 == "add") {
        // OUTPUT
        dIncreaseItem();
    }
}
    
// Save
void cSave() {
// this is really overcomplicated and bad, oh well!
    
    // Save
    if (inputCommandStringArg1 == "save") {
        // OUTPUT
        std::cout << messageTypes[0] << "Saving game data\n";
        std::cout << messageTypes[2] << "Do not do anything while the game is saving, otherwise your save might get corrupted\n";
    
        // Save Data
        saveDataShinyGems();

    }
    // Load
    if (inputCommandStringArg1 == "load") {
        // OUTPUT
        std::cout << messageTypes[0] << "Loading game data\n";
        std::cout << messageTypes[2] << "Do not do anything while the game is loading save data, otherwise your save might get corrupted\n";

        // Load Data
        loadDataShinyGems();

    }
    // Reset
    if (inputCommandStringArg1 == "reset") {
        // OUTPUT
        // Confirm Reset
        std::cout << "Are you sure you want to reset ALL of your save data? (y/n)\n# ";
        std::cin >> inputCommandStringArg1;
        // Reset Data
        if (inputCommandStringArg1 == "y") {
            std::cout << "\nResetting Data";
            resetData();
        } else {
            std::cout << "\nData Reset cancelled";
        }
    }
}