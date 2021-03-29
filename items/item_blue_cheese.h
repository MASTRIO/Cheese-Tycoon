//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataBlueCheese() {
    std::ofstream saveFiles("./jagac/item_blue_cheese.cheese");
    saveFiles << blue_cheese;
    saveFiles.close();
}

// Load Data
void loadDataBlueCheese() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_blue_cheese.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        blue_cheese = arr[i];
    }

    // ! Outputs Data
    std::cout << blue_cheese << "\n";

    // Close the file
    is.close();
}