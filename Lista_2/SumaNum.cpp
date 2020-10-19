//
// Created by Łukasz on 18/10/2020.
//

#include <iostream>
#include <sstream>

int main() {
    float sum = 0;

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        std::istringstream iss(myStrign);
        for (std::string res; iss >> res; ) {
            try {
                sum += std::stof(res);
            } catch (std::invalid_argument&) {}
        }
    }

    std::cout << sum;

    return 0;
}
