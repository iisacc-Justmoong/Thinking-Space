cmake_minimum_required(VERSION 3.31)
project(Thinking_Space)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(Thinking_Space main.cpp)
target_link_libraries(Thinking_Space
        PRIVATE Qt6::Quick
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

