# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build

# Utility rule file for update_mappings.

# Include any custom commands dependencies for this target.
include raylib/external/glfw/src/CMakeFiles/update_mappings.dir/compiler_depend.make

# Include the progress variables for this target.
include raylib/external/glfw/src/CMakeFiles/update_mappings.dir/progress.make

raylib/external/glfw/src/CMakeFiles/update_mappings:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Updating gamepad mappings from upstream repository"
	cd /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/external/glfw/src && /usr/bin/cmake -P /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/external/glfw/CMake/GenerateMappings.cmake mappings.h.in mappings.h

update_mappings: raylib/external/glfw/src/CMakeFiles/update_mappings
update_mappings: raylib/external/glfw/src/CMakeFiles/update_mappings.dir/build.make
.PHONY : update_mappings

# Rule to build all files generated by this target.
raylib/external/glfw/src/CMakeFiles/update_mappings.dir/build: update_mappings
.PHONY : raylib/external/glfw/src/CMakeFiles/update_mappings.dir/build

raylib/external/glfw/src/CMakeFiles/update_mappings.dir/clean:
	cd /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/external/glfw/src && $(CMAKE_COMMAND) -P CMakeFiles/update_mappings.dir/cmake_clean.cmake
.PHONY : raylib/external/glfw/src/CMakeFiles/update_mappings.dir/clean

raylib/external/glfw/src/CMakeFiles/update_mappings.dir/depend:
	cd /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/raylib/src/external/glfw/src /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/external/glfw/src /home/zmynz/vss/git-repo/zmynz-boink/rust/hello_world/target/debug/build/raylib-sys-8c4a8da0bce8fe79/out/build/raylib/external/glfw/src/CMakeFiles/update_mappings.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : raylib/external/glfw/src/CMakeFiles/update_mappings.dir/depend

