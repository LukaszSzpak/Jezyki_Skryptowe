#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int toInt(char *input) {
    int code = atoi(input);
    if (code == 0 && input[0] != '0')
        code = -1;
    return code;
}

int main(int argc, char* argv[]) {

    std::ifstream myFile;
    std::string myStrign;
    std::vector< std::vector<std::string> > myVec;

    myFile.open("Zakup.txt");

    if (myFile.is_open()) {
        while (getline(myFile, myStrign)) {
            std::vector<std::string> tempVec;
            std::istringstream iss(myStrign);
            for (std::string res; iss >> res; )
                tempVec.push_back(res);

            myVec.push_back(tempVec);
        }
    }

    if (!myVec.empty()) {
        for (int i = 0; i < myVec.size(); i++) {
            for (int j = 1; j < argc; j++) {
                int col = toInt(argv[j]);

                if (col > -1 && col < myVec[0].size()) {
                    std::cout << myVec[i][j]<<"\t";
                }
            }
            std::cout << "\n";
        }
    }



    return 0;
}
