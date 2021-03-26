//// * Include
#include <iostream>

//// * Variables
int debugIncreaseInt;

//// * Functions
// Get Item to Set
void dGetItemSet(std::string item) {
    if (item == "shiny_gems") {
        shiny_gems = debugIncreaseInt;
    } else if (item == "cheese_jumpers") {
        cheese_jumpers = debugIncreaseInt;
    }
}
// Get Item to Increase
void dGetIncreasedItem(std::string item) {
    if (item == "shiny_gems") {
        debugIncreaseInt = shiny_gems;
    } if (item == "cheese_jumpers") {
        debugIncreaseInt = cheese_jumpers;
    }
}
// Increase Item
void dIncreaseItem(std::string item, int amount) {
    // Get Item
    dGetIncreasedItem(item);

    // Increase Var
    debugIncreaseInt = debugIncreaseInt + amount;

    // Get Item
    dGetItemSet(item);
}