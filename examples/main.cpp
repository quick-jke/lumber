#include <iostream>
#include "user_generated.hpp"

int main() {
    quick::User user("Alice", 30);
    user.setAge(31);
    std::cout << "New age: " << user.getAge() << std::endl;
    std::cout << "Name: " << user.getName() << std::endl;
    return 0;
}