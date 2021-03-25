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
        std::cin >> inputCommandStringArg1 >> inputCommandStringArg2 >> inputCommandIntArg1;
        cDebug();
    } else if (commandType == "save") {
        std::cin >> inputCommandStringArg1;
        cSave();
    }
}

// Input Command Function
void typeInCommand() {
// i don't like this
    std::cout << "\n\n|What type of command would you like to run?| ";
    std::cin >> commandType;

    std::cout << ">>> ";
    getCommandType();
}

// Main Function
int main() {
    // Console Window Title
    SetConsoleTitle( TEXT("Epic Game Pog"));

    // Ask to type in command
    while (gameRunning == true) {
        typeInCommand();
    }
}