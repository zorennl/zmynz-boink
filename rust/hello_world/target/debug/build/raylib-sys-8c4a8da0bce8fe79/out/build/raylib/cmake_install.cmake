# Install script for directory: /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/libraylib.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/raylib.h"
    "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/rlgl.h"
    "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/raymath.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/raylib.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/raylib" TYPE FILE FILES "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/raylib-config-version.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/raylib" TYPE FILE FILES "/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/../cmake/raylib-config.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/external/glfw/cmake_install.cmake")

endif()

