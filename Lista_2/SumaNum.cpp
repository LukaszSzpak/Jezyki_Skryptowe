//
// Created by Łukasz on 18/10/2020.
//

#include <iostream>
#include <fstream>
#include <sstream>


int main() {

    std::ifstream myFile;
    std::string myStrign;
    float sum = 0;

    myFile.open("Zakup.txt");

    if (myFile.is_open()) {
        while (getline(myFile, myStrign)) {
            std::istringstream iss(myStrign);
            for (std::string res; iss >> res; ) {
                try {
                    sum += std::stof(res);
                } catch (std::invalid_argument) {

                }
            }
        }
    }

    std::cout << sum;

    return 0;
}
