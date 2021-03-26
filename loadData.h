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

// Cheese Jumpers
void loadDataCheeseJumpers() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_cheese_jumpers.cheese");
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

// Blue Cheese
void loadDataBlueCheese() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_blue_cheese.cheese");
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