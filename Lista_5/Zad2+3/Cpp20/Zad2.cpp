#include <iostream>
#include <fstream>
#include <sstream>

int main() {
    std::ifstream myFile("../../Covid19.txt");
    std::string line;
    int sum = 0;
    auto startTime = std::chrono::steady_clock::now();

    while (std::getline(myFile, line)) {
        std::istringstream stringStream(line);
        int stringIterator = 0;

        for (std::string word; stringStream >> word; stringIterator++) {
            if (stringIterator == 4)
                try {
                    sum += (int)std::stof(word);
                } catch (std::invalid_argument&) {}
        }
    }

    auto timeDiff = std::chrono::steady_clock::now() - startTime;

    std::cout << "Sum: " << sum << "\n";
    std::cout << "Exec time: " << std::chrono::duration <double, std::milli> (timeDiff).count() << "ms\n";

    return 0;
}
