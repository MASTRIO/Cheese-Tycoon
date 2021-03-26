//// * Include
#include <iostream>

//// * Variables
int debugIncreaseInt;

//// * Functions
// Get Item to Set
void dGetItemSet(std::string item) {
    if (item == "cheese") {
        cheese = debugIncreaseInt;
    } else if (item == "shiny_gems") {
        shiny_gems = debugIncreaseInt;
    } else if (item == "cheese_jumpers") {
        cheese_jumpers = debugIncreaseInt;
    } else if (item == "blue_cheese") {
        blue_cheese = debugIncreaseInt;
    } else if (item == "pebbles") {
        pebbles = debugIncreaseInt;
    } else if (item == "sticks") {
        sticks = debugIncreaseInt;
    } else if (item == "logs") {
        logs = debugIncreaseInt;
    } else if (item == "ruby") {
        ruby = debugIncreaseInt;
    } else if (item == "leaf") {
        ruby = debugIncreaseInt;
    } else if (item == "carrots") {
        carrots = debugIncreaseInt;
    } else if (item == "potato") {
        potato = debugIncreaseInt;
    } else if (item == "bread") {
        bread = debugIncreaseInt;
    } else if (item == "brick") {
        brick = debugIncreaseInt;
    } else if (item == "mouldy_potato") {
        mouldy_potato = debugIncreaseInt;
    } else if (item == "child") {
        child = debugIncreaseInt;
    } else if (item == "toy_bear") {
        toy_bear = debugIncreaseInt;
    } else if (item == "moose") {
        moose = debugIncreaseInt;
    }
}
// Get Item to Increase
void dGetIncreasedItem(std::string item) {
    if (item == "cheese") {
        debugIncreaseInt = cheese;
    } else if (item == "shiny_gems") {
        debugIncreaseInt = shiny_gems;
    } else if (item == "cheese_jumpers") {
        debugIncreaseInt = cheese_jumpers;
    } else if (item == "blue_cheese") {
        debugIncreaseInt = blue_cheese;
    } else if (item == "pebbles") {
        debugIncreaseInt = pebbles;
    } else if (item == "sticks") {
        debugIncreaseInt = sticks;
    } else if (item == "logs") {
        debugIncreaseInt = logs;
    } else if (item == "ruby") {
        debugIncreaseInt = ruby;
    } else if (item == "leaf") {
        debugIncreaseInt = leaf;
    } else if (item == "carrots") {
        debugIncreaseInt = carrots;
    } else if (item == "potato") {
        debugIncreaseInt = potato;
    } else if (item == "bread") {
        debugIncreaseInt = bread;
    } else if (item == "brick") {
        debugIncreaseInt = brick;
    } else if (item == "mouldy_potato") {
        debugIncreaseInt = mouldy_potato;
    } else if (item == "child") {
        debugIncreaseInt = child;
    } else if (item == "toy_bear") {
        debugIncreaseInt = toy_bear;
    } else if (item == "moose") {
        debugIncreaseInt = moose;
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