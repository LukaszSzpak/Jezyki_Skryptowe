//
// Created by Łukasz on 18/10/2020.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int toInt(char *input) {
    int code = atoi(input);
    if (code == 0 && input[0] != '0')
        code = -1;
    return code;
}


int main(int argc, char* argv[]) {

    std::ifstream myFile;
    std::string myStrign;
    std::vector<std::string> myVec;

    myFile.open("Zakup.txt");

    if (myFile.is_open()) {
        while (getline(myFile, myStrign)) {
            myVec.push_back(myStrign);
        }
    }

    if (!myVec.empty()) {
        for (int i = 1; i < argc; i++) {
            int col = toInt(argv[i]);

            if (col > -1 && col < myVec.size())
                std::cout << myVec[col] << "\n";
        }
    }


    return 0;
}
