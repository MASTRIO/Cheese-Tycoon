//// * Include
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include <vector>
#include <sys/stat.h>
#include <algorithm>
// Import
#include "commands.h"

//// * Functions
// * Other Functions
// Get Command Type
void getCommandType() {
    if (commandType == "debug") {
        std::cin >> inputCommandStringArg1;

        if (inputCommandStringArg1 == "add") {
            std::cin >> inputCommandStringArg2 >> inputCommandIntArg1;
        }

        cDebug();
    } else if (commandType == "game") {
        std::cin >> inputCommandStringArg1;
        cSave();
    } else if (commandType == "help") {
        cHelp();
    }
}

// Input Command Function
void typeInCommand() {
// pog
    std::cout << "\n\n>>> ";
    std::cin >> commandType;

    getCommandType();
}

// Main Function
int main() {
    // Console Window Title
    SetConsoleTitle( TEXT("Just Another Game About Cheese {Alpha v0.3}"));

    // Ask to type in command
    while (gameRunning == true) {
        typeInCommand();
    }
}