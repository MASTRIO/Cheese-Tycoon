//// * Include
#include <iostream>
#include <fstream>
// Import Scripts
#include "variables.h"
#include "resources.h"

//// * Functions
// Apples
void saveDataApples() {
    std::ofstream saveFiles("./jagac/item_apples.cheese");
    saveFiles << apples;
    saveFiles.close();
}