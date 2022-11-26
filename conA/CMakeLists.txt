
cmake_minimum_required(VERSION 3.15)

project(Hello2)

add_executable(hello2 src/main.c)
install(TARGETS hello2 DESTINATION bin)

