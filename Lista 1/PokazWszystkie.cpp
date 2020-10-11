//
// Created by Łukasz on 11/10/2020.
//

#include <cstdio>

int main (int argc, char *argv[], char *env[]) {
    while (not *env)
        puts(*env++);
}