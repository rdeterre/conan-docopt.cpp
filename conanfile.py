from conans import ConanFile, CMake

class DocoptConan(ConanFile):
    name = "docopt.cpp"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    version = "master"
    exports = "*"
    description = "Command-line parser"
    url = "https://github.com/docopt/docopt.cpp"
    license = "MIT"
    options = {"static": [True, False]}
    default_options = "static=True"

    def source(self):
        self.run('git clone {}'.format(self.url))

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd docopt.cpp && cmake {}'.format(cmake.command_line))
        self.run('cd docopt.cpp && cmake --build . {}'.format(cmake.build_config))

    def package(self):
        self.copy("docopt.h", dst="include", src="docopt.cpp", keep_path=False)
        self.copy("docopt_value.h", dst="include", src="docopt.cpp", keep_path=False)
        self.copy("docopt_util.h", dst="include", src="docopt.cpp", keep_path=False)
        if self.options.static:
            self.copy("*.a*", dst="lin", src="docopt.cpp", keep_path=False)
            self.copy("*.lib", dst="lib", src="docopt.cpp", keep_path=False)
        else:
            self.copy("*.dll", dst="bin", src="docopt.cpp", keep_path=False)
            self.copy("*.so*", dst="lib", src="docopt.cpp", keep_path=False)
            self.copy("*.lib", dst="lib", src="docopt.cpp", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["docopt"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]
