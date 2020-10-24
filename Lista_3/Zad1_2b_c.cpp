//
// Created by Łukasz on 24/10/2020.
//

#include <string>
#include <iostream>

int main(int argc, char *argv[]) {
    if(argc > 1) {
        int sum = 0;
        std::string test_string = argv[1];

        for (std::string myStrign; std::getline(std::cin, myStrign); ) {
            if (myStrign.substr(0, test_string.size()) == test_string)
                sum++;
        }

        std::cout << sum;
    }
}