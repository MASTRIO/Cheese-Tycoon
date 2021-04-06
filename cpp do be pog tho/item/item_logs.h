//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Save Data
void saveDataLogs() {
    std::ofstream saveFiles("./jagac/item_logs.cheese");
    saveFiles << logs;
    saveFiles.close();
}

// Load Data
void loadDataLogs() {
    // Make the array
    int arr[30];
    std::ifstream is("./jagac/items_logs.cheese");
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