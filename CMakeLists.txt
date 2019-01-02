# cmake_minimum_required(VERSION <specify CMake version here>)
project(source_code)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(source_code
        file.one
        file.two
        README.md python_study/practice.cpp)
