//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataPebbles() {
    std::ofstream saveFiles("./jagac/item_pebbles.cheese");
    saveFiles << pebbles;
    saveFiles.close();
}

// Load Data
void loadDataPebbles() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_pebbles.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        pebbles = arr[i];
    }

    // ! Outputs Data
    std::cout << pebbles << "\n";

    // Close the file
    is.close();
}