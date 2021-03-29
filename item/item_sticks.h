//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataSticks() {
    std::ofstream saveFiles("./jagac/item_sticks.cheese");
    saveFiles << sticks;
    saveFiles.close();
}

// Load Data
void loadDataSticks() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_sticks.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        sticks = arr[i];
    }

    // ! Outputs Data
    std::cout << sticks << "\n";

    // Close the file
    is.close();
}