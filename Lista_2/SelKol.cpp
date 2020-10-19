#include <iostream>
#include <string>
#include <sstream>
#include <vector>

long toInt(const char *input) {
    try {
        long code = strtol(input, nullptr, 10);
        return code;
    } catch (std::invalid_argument&) {}

    return -1;
}

int main(int argc, char* argv[]) {

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        std::vector<std::string> tempVec;
        std::istringstream iss(myStrign);
        for (std::string res; iss >> res; )
            tempVec.push_back(res);

        for (int i = 1; i < argc; i++) {
            long col = toInt(argv[i]);

            if (col > -1 && col < tempVec.size())
                std::cout << tempVec[col] << "\t";
        }
        std::cout << "\n";
    }

    return 0;
}
