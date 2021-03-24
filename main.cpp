//// * Include
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include <vector>
#include <sys/stat.h>
#include <algorithm>



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
// Convert Save Data
int convertInputInt;
int convertMultiplier = 1;
std::vector<std::string> convertList;
int convertListData = 0;
int convertTimesLoaded = 0;
// Items
int apples = 0;



//// * Functions
// TODO: Save Data
void saveDataApples() {
    std::ofstream saveFiles("./data/item_apples.cheese");
    saveFiles << apples;
    saveFiles.close();
}



// * Load Data
void loadDataApples() {
    // Make the array
    int arr[30];
    std::ifstream is("data/item_apples.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        apples = arr[i];
    }

    // ! Outputs Data
    std::cout << apples << "\n";

    // Close the file
    is.close();
}



// * Commands
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