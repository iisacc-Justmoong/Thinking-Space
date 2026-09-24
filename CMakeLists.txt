cmake_minimum_required(VERSION 3.31)
include("${CMAKE_CURRENT_LIST_DIR}/cmake/single-app/Defaults.cmake")
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
set_target_properties(Thinking_Space PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER "com.iisacc.thinkingspace"
    MACOSX_BUNDLE_BUNDLE_NAME "Thinking Space")
target_link_libraries(Thinking_Space
        PRIVATE Qt::Core
        Qt::Gui
        Qt::Widgets
)

# Apply after Qt/LVRS finalizers, which may enable bundles for test targets.
include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/single-app/SingleApp.cmake")
product_plain_executables("${CMAKE_SOURCE_DIR}" Thinking_Space)
cmake_language(DEFER CALL product_single_app Thinking_Space "")

product_deploy_app(Thinking_Space "")
