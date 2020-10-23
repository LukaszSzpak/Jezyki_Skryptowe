#include <iostream>

void splitWords() {
    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        std::string tempStr;
        for (char i : myStrign) {
            if ((i >= 'a' && i <= 'z') || (i >= 'A' && i <= 'Z')) {
                tempStr += i;
            } else if (!tempStr.empty()){
                std::cout << tempStr << "\n";
                tempStr = "";
            }
        }
    }
}

void split() {
    std::string tempStr;
    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        for (char i : myStrign) {
            if (tempStr.size() > 1
                && (tempStr[tempStr.size() - 2] == '.' || tempStr[tempStr.size() - 2] == '?' || tempStr[tempStr.size() - 2] == '!')
                && (i >= 'A' && i <= 'Z'))
            {
                std::cout << tempStr << "\n\n\n";
                tempStr.clear();
                tempStr += i;
            } else {
                tempStr += i;
            }
        }
    }
    std::cout << tempStr;
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        if (argv[1][0] == '/' && argv[1][1] == 'Z')
            split();
    } else
        splitWords();

    return 0;
}
