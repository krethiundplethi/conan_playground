
cmake_minimum_required(VERSION 3.15)

project(Hello1)

add_executable(hello1 main.c)
install(TARGETS hello1 DESTINATION bin)

