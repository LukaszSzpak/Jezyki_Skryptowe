//
// Created by Łukasz on 11/10/2020.
//

#include <cstdio>
#include <cstdlib>
#include <sstream>

int toInt(char *input) {
    int code = atoi(input);
    if (code == 0)
        code = 12;
    return code;
}

int main (int argc, char *argv[], char *env[]) {
    int code = 0;
    char buffer[33];
    bool shouldIPrint = 1;

    if (argc > 2)
        if (argv[2][0] == '/' && (argv[2][1] == 's' || argv[2][1] == 'S'))
            shouldIPrint = 0;

    if (argc > 3)
        code = 13;
    else if (argc == 2 && !shouldIPrint)
        code = 11;
    else {
        code = toInt(argv[1]);
    }

    if(shouldIPrint) {
        std::ostringstream result;
        result << code;
        puts(const_cast<char*>(result.str().c_str()));
    }

    return code;
}
