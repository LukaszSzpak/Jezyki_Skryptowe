//
// Created by Łukasz on 18/10/2020.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>


int main(int argc, char* argv[]) {
    std::ifstream myFile;
    std::string myStrign;

    myFile.open("Zakup.txt");

    if (myFile.is_open()) {
        while (getline(myFile, myStrign)) {
            std::istringstream iss(myStrign);
            bool flag = true;

            for (std::string res; iss >> res && flag; )
                for (int i = 1; i < argc && flag; i++) {
                    if (res == argv[i]) {
                        std::cout << myStrign << "\n";
                        flag = false;
                    }
                }
        }
    }


    return 0;
}
