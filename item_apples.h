//// * Include
#include <iostream>
#include <fstream>
// Import Scripts
#include "variables.h"

// * Load Data
void loadDataApples() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_apples.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        apples = arr[i];
    }

    // ! Outputs Data
    std::cout << apples << "\n";

    // Close the file
    is.close();
}