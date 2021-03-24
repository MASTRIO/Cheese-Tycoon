//// * Include
#include <iostream>
// Import Scripts
#include "variables.h"
#include "resources.h"
#include "saveData.h"
#include "loadData.h"

//// * Functions
// Debug
void cDebug() {
    // why
        // Add
        if (inputCommandStringArg1 == "add") {
            // Apples
            if (inputCommandStringArg2 == "apples") {
                // OUTPUT
                apples = apples + inputCommandIntArg1;
    
                std::cout << messageTypes[3] << "You got " << inputCommandIntArg1 << " apples\n";
                std::cout << messageTypes[3] << "You now have " << apples << " apples";
            }
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
        saveDataApples();

    }
    if (inputCommandStringArg1 == "load") {
        // OUTPUT
        std::cout << messageTypes[0] << "Loading game data\n";
        std::cout << messageTypes[2] << "Do not do anything while the game is loading save data, otherwise your save might get corrupted\n";

        // Load Data
        loadDataApples();

    }
}