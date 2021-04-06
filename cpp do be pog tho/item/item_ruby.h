//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataRuby() {
    std::ofstream saveFiles("./jagac/item_ruby.cheese");
    saveFiles << ruby;
    saveFiles.close();
}

// Load Data
void loadDataRuby() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_ruby.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        ruby = arr[i];
    }

    // ! Outputs Data
    std::cout << ruby << "\n";

    // Close the file
    is.close();
}