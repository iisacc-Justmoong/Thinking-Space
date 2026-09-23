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

if(APPLE AND TARGET WrapOpenGL::WrapOpenGL)
    # Qt 6.8's OpenGL wrapper still advertises AGL, which current SDKs omit.
    # The arm64 Widgets application does not call the legacy AGL API.
    get_target_property(_opengl_links WrapOpenGL::WrapOpenGL INTERFACE_LINK_LIBRARIES)
    list(FILTER _opengl_links EXCLUDE REGEX "(^|[ /])AGL($|[ /.])|AGL\\.framework")
    set_property(TARGET WrapOpenGL::WrapOpenGL PROPERTY INTERFACE_LINK_LIBRARIES "${_opengl_links}")
endif()

add_executable(Thinking_Space src/main.cpp)
target_link_libraries(Thinking_Space
        PRIVATE Qt::Core
        Qt::Gui
        Qt::Widgets
)
