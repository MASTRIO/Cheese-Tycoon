//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataCheeseJumpers() {
    std::ofstream saveFiles("./jagac/item_cheese_jumpers.cheese");
    saveFiles << cheese_jumpers;
    saveFiles.close();
}

// Load Data
void loadDataCheeseJumpers() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_cheese_jumpers.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        cheese_jumpers = arr[i];
    }

    // ! Outputs Data
    std::cout << cheese_jumpers << "\n";

    // Close the file
    is.close();
}