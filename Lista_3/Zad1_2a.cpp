//
// Created by Łukasz on 24/10/2020.
//

#include <string>
#include <iostream>

int main() {
    int sum = 0;

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        sum++;
    }

    std::cout << sum;
}