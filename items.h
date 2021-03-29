//// * Include
#include <iostream>
#include <fstream>
#include <string>

//// * Classes
// Creates a new Item
class NewItem {
public:
    // * Variables
    std::string itemName;
    int sellPrice;
    int buyPrice;
    // * Functions
    // Save Data
    void saveItem() {
        whereToSave(itemName);
    }
};

//// * Functions
void whereToSave(std::string itemToSave) {
    if (itemToSave == "shiny_gems") {
        std::ofstream saveFiles("./jagac/item_shiny_gems.cheese");
        saveFiles << shiny_gems;
        saveFiles.close();
    }
}

void createItems() {
    NewItem ShinyGems; ShinyGems.itemName = "shiny_gems"; ShinyGems.buyPrice = 0; ShinyGems.sellPrice = 0;
}