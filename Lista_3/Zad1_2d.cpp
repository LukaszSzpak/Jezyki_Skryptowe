//
// Created by Łukasz on 24/10/2020.
//

#include <string>
#include <iostream>

int main() {
    int sum = 0;

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        if (myStrign.substr(0, 2) == "It"
            && myStrign.substr(myStrign.size()-2, std::string::npos) == "of")
            sum++;
    }

    std::cout << sum;

}