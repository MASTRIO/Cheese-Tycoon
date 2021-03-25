//// * Include
#include <iostream>
#include <fstream>

//// * Functions
// Shiny Gems
void saveDataShinyGems() {
    std::ofstream saveFiles("./jagac/item_shiny_gems.cheese");
    saveFiles << shiny_gems;
    saveFiles.close();
}