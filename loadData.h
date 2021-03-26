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

// Pebbles
void loadDataPebbles() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_pebbles.cheese");
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

// Sticks
void loadDataSticks() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_sticks.cheese");
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

// Logs
void loadDataLogs() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_logs.cheese");
    int cnt= 0;
    int x;

    // Make sure the array isn't full
    while (cnt < arr[30] && is >> x)

    // And that it can read the integer
    arr[cnt++] = x;

    // Saves the Data
    for (int i = 0; i < cnt; i++) {
        logs = arr[i];
    }

    // ! Outputs Data
    std::cout << logs << "\n";

    // Close the file
    is.close();
}

// Ruby
void loadDataRuby() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_ruby.cheese");
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

// Leaf
void loadDataLeaf() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/item_leaf.cheese");
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