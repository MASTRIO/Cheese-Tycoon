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
// Convert Loaded Data
int multipliedInt = 1;
std::string convertedValues;
std::string whatToSave;
int convertInputStr;
bool isConvertingLoadedData = false;
std::vector<int> loadedDigits;
int loadingNumber = 0;
// Items
int apples = 0;



//// * Functions
// Convert Save Data to Usable Int because haha yes go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
void convertSaveData() {
    if (convertList[convertListData] == "a") {
        convertInputInt = convertInputInt + (1 * convertMultiplier);
    } else if (convertList[convertListData] == "b") {
        convertInputInt = convertInputInt + (2 * convertMultiplier);
    } else if (convertList[convertListData] == "c") {
        convertInputInt = convertInputInt + (3 * convertMultiplier);
    } else if (convertList[convertListData] == "d") {
        convertInputInt = convertInputInt + (4 * convertMultiplier);
    } else if (convertList[convertListData] == "e") {
        convertInputInt = convertInputInt + (5 * convertMultiplier);
    } else if (convertList[convertListData] == "f") {
        convertInputInt = convertInputInt + (6 * convertMultiplier);
    } else if (convertList[convertListData] == "g") {
        convertInputInt = convertInputInt + (7 * convertMultiplier);
    } else if (convertList[convertListData] == "h") {
        convertInputInt = convertInputInt + (8 * convertMultiplier);
    } else if (convertList[convertListData] == "i") {
        convertInputInt = convertInputInt + (9 * convertMultiplier);
    } else if (convertList[convertListData] == "j") {
        convertInputInt = convertInputInt + (0 * convertMultiplier);
    }
}

// Convert Loaded Data to Saveable String because ciursehgdrufyvjgsedjxfgbvkjezrsdxbgnvkurh ggvhgdkjghvrzkuydgverkjhgbdfjkxc
void convertLoadedData() {
    while (convertInputStr > 0) {
        loadedDigits.push_back(convertInputStr % 10);
        convertInputStr / 10;
    }

    reverse(loadedDigits.begin(), loadedDigits.end());

    while (loadedDigits[loadingNumber]) {
        std::cout << "test\n";

        // Converting process pog
        

        loadingNumber++;
    }
}



// * Save Loaded Data
// Apples
void saveDataApples() {
    // Convert to saveable string or something idk
    convertLoadedData();

    // Save the stupid data already!
    std::ofstream saveFiles("./data/item_apples.cheese");
    saveFiles << whatToSave;
    saveFiles.close();
}



// * Load Saved Data
// Apples
void loadDataApples() {
    std::string loadText;
    std::ifstream loadFiles("./data/item_apples.cheese");

    while (std::getline (loadFiles, loadText)) {
        convertList.push_back(loadText);

        convertSaveData();

        std::cout << "\n" << messageTypes[3] << convertInputInt;

        convertListData++;
        convertMultiplier = convertMultiplier * 10;
    }

    loadFiles.close();
}



// * Load Data Funky
void loadData(std::string itemToLoad) {
    convertMultiplier = 1;
    convertListData = 0;

    convertList.clear();

    if (itemToLoad == "apples") {
        loadDataApples();
    }
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
        std::cout << messageTypes[2] << "Do not do anything while the game is saving, otherwise your save might get corrupted";

        convertInputStr = apples;
        saveDataApples();

    }
    if (inputCommandStringArg1 == "load") {
        // OUTPUT
        std::cout << messageTypes[0] << "Loading game data\n";
        std::cout << messageTypes[2] << "Do not do anything while the game is loading save data, otherwise your save might get corrupted\n";

        /// * Load Data
        // Apples
        convertInputInt = apples;
        loadData("apples");
        apples = convertInputInt;
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