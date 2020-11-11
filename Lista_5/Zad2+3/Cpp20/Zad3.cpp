#include <iostream>
#include <fstream>
#include <sstream>

int main() {
    std::ifstream myFile("../../Covid19.txt");
    std::string line;
    std::string country;

    std::cout << "Write your country: ";
    std::cin >> country;

    int covidSum = 0;
    int tempCovidCount;
    auto startTime = std::chrono::steady_clock::now();

    while (std::getline(myFile, line)) {
        std::istringstream stringStream(line);
        int stringIterator = 0;

        for (std::string word; stringStream >> word; stringIterator++) {
            if (stringIterator == 4)
                try {
                    tempCovidCount = (int)std::stof(word);
                } catch (std::invalid_argument&) {}

            if(stringIterator == 6 && word == country)
                covidSum += tempCovidCount;

        }
    }

    auto timeDiff = std::chrono::steady_clock::now() - startTime;

    std::cout << "Sum: " << covidSum << "\n";
    std::cout << "Exec time: " << std::chrono::duration <double, std::milli> (timeDiff).count() << "ms\n";

    return 0;
}


