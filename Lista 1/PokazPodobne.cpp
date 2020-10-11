#include <cstdlib>
#include <string>
#include <iostream>

int main(int argc, char* argv[], char* env[]) {
    if (argc > 1) {
        std::string myArg = argv[1];

        while (*env != nullptr) {
            std::string myString = *env;
            std::size_t pos = myString.find(myArg);

            if (pos != std::string::npos) {
                std::size_t equalSignPos = myString.find('=');
                if (equalSignPos != std::string::npos){
                    std::cout << myString.substr(0, equalSignPos) << "\n";
                    std::cout << '=' << '\n';

                    std::size_t newPos = equalSignPos;
                    do {
                        myString = myString.substr(newPos + 1);
                        newPos = myString.find(';');
                        std::cout << myString.substr(0, newPos) << "\n";

                    } while (newPos != std::string::npos);


                    std::cout << "\n";
                }
            }
            env++;
        }
    }
}
