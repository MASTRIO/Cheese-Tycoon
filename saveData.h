//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Apples
void saveDataApples() {
    std::ofstream saveFiles("./jagac/item_apples.cheese");
    saveFiles << apples;
    saveFiles.close();
}