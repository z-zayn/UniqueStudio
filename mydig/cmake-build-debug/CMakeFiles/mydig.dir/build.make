# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/zaynz/clion-2019.2.5/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/zaynz/clion-2019.2.5/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zaynz/UniqueStudio/mydig

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zaynz/UniqueStudio/mydig/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/mydig.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/mydig.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mydig.dir/flags.make

CMakeFiles/mydig.dir/main.c.o: CMakeFiles/mydig.dir/flags.make
CMakeFiles/mydig.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/zaynz/UniqueStudio/mydig/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/mydig.dir/main.c.o"
	/usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mydig.dir/main.c.o   -c /home/zaynz/UniqueStudio/mydig/main.c

CMakeFiles/mydig.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mydig.dir/main.c.i"
	/usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/zaynz/UniqueStudio/mydig/main.c > CMakeFiles/mydig.dir/main.c.i

CMakeFiles/mydig.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mydig.dir/main.c.s"
	/usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/zaynz/UniqueStudio/mydig/main.c -o CMakeFiles/mydig.dir/main.c.s

# Object files for target mydig
mydig_OBJECTS = \
"CMakeFiles/mydig.dir/main.c.o"

# External object files for target mydig
mydig_EXTERNAL_OBJECTS =

mydig: CMakeFiles/mydig.dir/main.c.o
mydig: CMakeFiles/mydig.dir/build.make
mydig: CMakeFiles/mydig.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/zaynz/UniqueStudio/mydig/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable mydig"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mydig.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/mydig.dir/build: mydig

.PHONY : CMakeFiles/mydig.dir/build

CMakeFiles/mydig.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mydig.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mydig.dir/clean

CMakeFiles/mydig.dir/depend:
	cd /home/zaynz/UniqueStudio/mydig/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zaynz/UniqueStudio/mydig /home/zaynz/UniqueStudio/mydig /home/zaynz/UniqueStudio/mydig/cmake-build-debug /home/zaynz/UniqueStudio/mydig/cmake-build-debug /home/zaynz/UniqueStudio/mydig/cmake-build-debug/CMakeFiles/mydig.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/mydig.dir/depend
