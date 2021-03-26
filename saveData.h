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

// Cheese Jumpers
void saveDataCheeseJumpers() {
    std::ofstream saveFiles("./jagac/item_cheese_jumpers.cheese");
    saveFiles << cheese_jumpers;
    saveFiles.close();
}

// Blue Cheese
void saveDataBlueCheese() {
    std::ofstream saveFiles("./jagac/item_blue_cheese.cheese");
    saveFiles << blue_cheese;
    saveFiles.close();
}