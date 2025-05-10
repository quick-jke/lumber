cmake_minimum_required(VERSION 3.14)
project(CppLombok)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${PROJECT_SOURCE_DIR}/examples)
include_directories(${PROJECT_SOURCE_DIR}/include)
include_directories(${PROJECT_BINARY_DIR}/generated)  

set(SOURCE_DIR ${PROJECT_SOURCE_DIR}/examples)
set(GENERATED_DIR ${PROJECT_BINARY_DIR}/generated)

file(MAKE_DIRECTORY ${GENERATED_DIR})

add_custom_command(
    OUTPUT ${GENERATED_DIR}/User.hpp ${GENERATED_DIR}/user_generated.cpp
    COMMAND python3 ${PROJECT_SOURCE_DIR}/scanner/scanner.py ${GENERATED_DIR}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    COMMENT "Generating code using Lombok-like scanner"
)

add_executable(example
    ${SOURCE_DIR}/main.cpp
    ${GENERATED_DIR}/user_generated.cpp  
)


set_property(SOURCE ${GENERATED_DIR}/user_generated.cpp PROPERTY GENERATED TRUE)