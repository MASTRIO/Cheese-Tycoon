//// * Include
#include <iostream>

//// * Variables
int debugIncreaseInt;

//// * Functions
// Get Item to Set
void dGetItemSet() {
    if (inputCommandStringArg2 == "shiny_gems") {
        shiny_gems = debugIncreaseInt;
    }
}
// Get Item to Increase
void dGetIncreasedItem() {
    if (inputCommandStringArg2 == "shiny_gems") {
        debugIncreaseInt = shiny_gems;
    }
}
// Increase Item
void dIncreaseItem() {
    // Get Item
    dGetIncreasedItem();

    // Increase Var
    debugIncreaseInt = debugIncreaseInt + inputCommandIntArg1;
    
    // Send Message to Console
    std::cout << messageTypes[3] << "You got " << inputCommandIntArg1 << " " << inputCommandStringArg2 << "\n";
    std::cout << messageTypes[3] << "You now have " << debugIncreaseInt << " " << inputCommandStringArg2;

    // Get Item
    dGetItemSet();
}