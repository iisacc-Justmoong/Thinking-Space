# Thinking Space

The current project is a Qt 6 Widgets application scaffold. It does not yet
consume any workspace SDK package. SDK source projects live in `../../SDK`,
and installed packages live under `$HOME/.local/SDK`; add a package dependency
only when application code actually uses it.
The executable links the Core, Gui, and Widgets modules found by CMake.
It uses no Qt Quick API, so a fresh configuration does not require a
previously cached or indirectly imported `Qt6::Quick` target.
On macOS, CMake removes the redundant legacy AGL entry from Qt 6.8's
OpenGL wrapper so SDKs without AGL can link the app. The Widgets executable keeps
its normal AppKit and OpenGL dependencies.

Keep all generated CMake output in `build/`. The CLion Debug profile uses that
same directory. Configure and validate from the project directory:

```sh
cmake --fresh -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Debug \
  -DQt6_DIR="/Volumes/Storage/Qt/6.8.3/macos/lib/cmake/Qt6"
cmake --build build
ctest --test-dir build --output-on-failure --no-tests=error
```

No automated application tests are currently registered. The final command
reports that absence as an error instead of claiming a passing test suite.
