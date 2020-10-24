//
// Created by Łukasz on 24/10/2020.
//

#include <string>
#include <iostream>

int main() {

    for (std::string myStrign; std::getline(std::cin, myStrign); ) {
        bool flag = true;

        if (!(myStrign[0] == 't' && myStrign[1] == 'h'))
            flag = false;

        for (int i = 0; i < myStrign.size() && flag; i++) {
            if (myStrign[i] == 'n' || myStrign[i] == 'a' || myStrign[i] == 'e')
                flag = false;
        }

        if (flag)
            std::cout << myStrign << "\n";
    }
}