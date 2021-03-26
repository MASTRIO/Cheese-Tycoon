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

// Pebbles
void saveDataPebbles() {
    std::ofstream saveFiles("./jagac/item_pebbles.cheese");
    saveFiles << pebbles;
    saveFiles.close();
}

// Sticks
void saveDataSticks() {
    std::ofstream saveFiles("./jagac/item_sticks.cheese");
    saveFiles << sticks;
    saveFiles.close();
}

// Logs
void saveDataLogs() {
    std::ofstream saveFiles("./jagac/item_logs.cheese");
    saveFiles << logs;
    saveFiles.close();
}

// Ruby
void saveDataRuby() {
    std::ofstream saveFiles("./jagac/item_ruby.cheese");
    saveFiles << ruby;
    saveFiles.close();
}

// Leaf
void saveDataLeaf() {
    std::ofstream saveFiles("./jagac/item_leaf.cheese");
    saveFiles << leaf;
    saveFiles.close();
}