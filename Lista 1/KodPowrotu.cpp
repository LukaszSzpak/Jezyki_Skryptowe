//
// Created by Łukasz on 11/10/2020.
//

#include <cstdio>
#include <cstdlib>
#include <sstream>

int toInt(char *input) {
    int code = atoi(input);
    if (code == 0 && input[0] != '0')
        code = 12;
    return code;
}

int main (int argc, char *argv[], char *env[]) {
    int code = 0;
    bool shouldIPrint = true;

    if (argc >= 2)
        if (argv[1][0] == '/' && (argv[1][1] == 's' || argv[1][1] == 'S'))
            shouldIPrint = false;

    if (argc > 3)
        code = 13;
    else if ((argc == 2 && !shouldIPrint) || argc == 1)
        code = 11;
    else {
        code = toInt(argv[2]);
    }

    if(shouldIPrint) {
        std::ostringstream result;
        result << code;
        puts(const_cast<char*>(result.str().c_str()));
    }

    return code;
}
