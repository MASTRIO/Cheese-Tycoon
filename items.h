//// * Include
#include <iostream>
#include <fstream>
#include <string>

//// * Classes
// Creates a new Item
class NewItem {
public:
    // * Variables
    int arr[30];
    int cnt= 0;
    int x;
    // Declarables
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
// Where To Save
std::string whereToSave(std::string itemToSave) {
    if (itemToSave == "shiny_gems") {
        std::ofstream saveFiles("./jagac/item_shiny_gems.cheese");
        saveFiles << shiny_gems;
        saveFiles.close();
    }
    return;
}
// Where To Load
void whatToLoad(std::string itemToLoad) {
    if (itemToLoad == "shiny_gems") {
        std::ifstream is("./jagac/items_sticks.cheese");
    }
}

void createItems() {
    NewItem ShinyGems; ShinyGems.itemName = "shiny_gems"; ShinyGems.buyPrice = 0; ShinyGems.sellPrice = 0;
}