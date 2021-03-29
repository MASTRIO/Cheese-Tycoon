//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataLeaf() {
    std::ofstream saveFiles("./jagac/item_leaf.cheese");
    saveFiles << leaf;
    saveFiles.close();
}

// Load Data
void loadDataLeaf() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_leaf.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        leaf = arr[i];
    }

    // ! Outputs Data
    std::cout << leaf << "\n";

    // Close the file
    is.close();
}