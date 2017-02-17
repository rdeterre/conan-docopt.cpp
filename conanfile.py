from conans import ConanFile, CMake
from conans.tools import download, unzip
import os
import shutil

class DocoptConan(ConanFile):
    name = "docopt.cpp"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    version = "master"
    exports = "*"
    description = "Command-line parser"
    url = "https://github.com/docopt/docopt.cpp"
    license = "MIT"

    def source(self):
        self.run( "git clone {}".format(self.url))

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd docopt.cpp && cmake {}'.format(cmake.command_line))
        self.run('cd docopt.cpp && cmake --build . {}'.format(cmake.build_config))

    def package(self):
        self.copy("docopt.h", dst="include", src="docopt.cpp")
        self.copy("docopt_value.h", dst="include", src="docopt.cpp")
        self.copy("docopt_util.h", dst="include", src="docopt.cpp")
        self.copy("*.dll", dst="bin", src="docopt.cpp")
        self.copy("*.so*", dst="lib", src="docopt.cpp")
        self.copy("*.a*", dst="bin", src="docopt.cpp")
        self.copy("*.lib", dst="lib", src="docopt.cpp")

    def package_info(self):
        self.cpp_info.libs = ["docopt"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]
