//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataShinyGems() {
    std::ofstream saveFiles("./jagac/item_shiny_gems.cheese");
    saveFiles << shiny_gems;
    saveFiles.close();
}

// Load Data
void loadDataShinyGems() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_shiny_gems.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        shiny_gems = arr[i];
    }

    // ! Outputs Data
    std::cout << shiny_gems << "\n";

    // Close the file
    is.close();
}