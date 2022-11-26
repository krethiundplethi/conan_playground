

from conans import ConanFile, CMake, tools


class HelloC(ConanFile):

    name = "Hello_C"
    version = "1.7.9"
    license = "none"
    url = "https://github.com/google/fruit"
    description = "Test only"

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"


    def requirements(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("hello3", dst="bin", keep_path=False)
