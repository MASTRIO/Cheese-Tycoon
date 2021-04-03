//// * Include
#include <iostream>
// * Import
#include "items/item_shiny_gem.h"
#include "items/item_cheese_jumpers.h"
#include "items/item_blue_cheese.h"
#include "items/item_pebbles.h"
#include "items/item_sticks.h"
#include "items/item_logs.h"
#include "items/item_ruby.h"
#include "items/item_leaf.h"

//// * Functions
// Save
void saveData() {
    saveDataShinyGems();
    saveDataCheeseJumpers();
    saveDataBlueCheese();
    saveDataPebbles();
    saveDataSticks();
    saveDataLogs();
    saveDataRuby();
    saveDataLeaf();
}

// Load
void loadData() {
    loadDataShinyGems();
    loadDataCheeseJumpers();
    loadDataBlueCheese();
    loadDataPebbles();
    loadDataSticks();
    loadDataLogs();
    loadDataRuby();
    loadDataLeaf();
}