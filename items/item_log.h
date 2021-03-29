//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataLog() {
    std::ofstream saveFiles("./jagac/item_log.cheese");
    saveFiles << log;
    saveFiles.close();
}

// Load Data
void loadDataLog() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_log.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        log = arr[i];
    }

    // ! Outputs Data
    std::cout << log << "\n";

    // Close the file
    is.close();
}