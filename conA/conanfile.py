

from conans import ConanFile, CMake, tools


class HelloA(ConanFile):

    name = "Hello_A"
    version = "1.1.0"
    license = "none"
    url = "https://github.com/google/fruit"
    description = "Test only"

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"


    def requirements(self):
        self.requires("Hello_B/[~1.1]")
        self.requires("Hello_C/[~2.1]")

    #def package_id(self):
    #    self.info.requires["Hello1"].semver_direct_mode()


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("hello2", dst="bin", keep_path=False)
