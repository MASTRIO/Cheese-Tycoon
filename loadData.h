//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Shiny Gems
void loadDataShinyGems() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_shiny_gems.cheese");
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