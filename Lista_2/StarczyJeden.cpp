//
// Created by Łukasz on 18/10/2020.
//

#include <iostream>
#include <vector>
#include <sstream>


int main(int argc, char* argv[]) {

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
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

    return 0;
}
