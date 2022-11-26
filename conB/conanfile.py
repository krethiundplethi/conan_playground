

from conans import ConanFile, CMake, tools


class HelloB(ConanFile):

    name = "Hello_B"
    version = "1.1.0"
    license = "none"
    url = "https://github.com/google/fruit"
    description = "Test only"

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"


    def requirements(self):
        self.requires("Hello_C/[>1.0]")

    def package_id(self):
        self.info.requires["Hello_C"].unrelated_mode()


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("hello2", dst="bin", keep_path=False)
