#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 project_name"
    exit 1
fi

PROJECT_NAME=$1

# Create project directory structure
mkdir -p $PROJECT_NAME/{include,src,build,.vscode}

# Create CMakeLists.txt
cat <<EOL > $PROJECT_NAME/CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project($PROJECT_NAME)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_executable($PROJECT_NAME \${SOURCES})
EOL

# Create .vscode/settings.json
cat <<EOL > $PROJECT_NAME/.vscode/settings.json
{
    "cmake.generator": "MinGW Makefiles",
    "cmake.configureOnOpen": true
}
EOL

# Create .vscode/tasks.json
cat <<EOL > $PROJECT_NAME/.vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "CMake Build",
            "type": "shell",
            "command": "cmake --build build",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": ["\$gcc"],
            "detail": "Generated task by CMake Tools."
        }
    ]
}
EOL

# Create .vscode/launch.json
cat <<EOL > $PROJECT_NAME/.vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "\${workspaceFolder}/build/$PROJECT_NAME.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "\${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "CMake Build",
            "miDebuggerPath": "C:/mingw/bin/gdb.exe",
            "logging": {
                "trace": true,
                "engineLogging": true,
                "programOutput": true,
                "exceptions": true
            }
        }
    ]
}
EOL

# Create a sample header file
cat <<EOL > $PROJECT_NAME/include/myheader.h
#ifndef MYHEADER_H
#define MYHEADER_H

void say_hello();

#endif // MYHEADER_H
EOL

# Create a sample source file
cat <<EOL > $PROJECT_NAME/src/main.cpp
#include "myheader.h"
#include <iostream>

void say_hello() {
    std::cout << "Hello, world!" << std::endl;
}

int main() {
    say_hello();
    return 0;
}
EOL

echo "Project $PROJECT_NAME setup completed."
