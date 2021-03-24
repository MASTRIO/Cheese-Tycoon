//// * Include
#include <iostream>
#include <string>
#include <vector>

//// * Variables
// hrrrrrrrr
bool gameRunning = true;
// Message Type
std::string messageTypes[4] = {
    "[LOG] ",
    "[ERR] ",
    "[WARN] ",
    "[DEBUG] "
};
// Command Type
std::string commandType;
// Command Inputs
std::string inputCommandStringArg1;
std::string inputCommandStringArg2;
std::string inputCommandStringArg3;
int inputCommandIntArg1;
// Convert Save Data
int convertInputInt;
int convertMultiplier = 1;
std::vector<std::string> convertList;
int convertListData = 0;
int convertTimesLoaded = 0;