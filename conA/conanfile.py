from conans import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class HelloA(ConanFile):

    name = "Hello_A"
    version = "1.1.0"
    license = "none"
    url = "https://github.com/google/fruit"
    description = "Test only"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "cmake_find_package"
    
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "https://github.com/krethiundplethi/conan_playground.git",
        "revision": "auto"
    }


    def requirements(self):
        self.requires("Hello_B/[~1.1]")
        self.requires("Hello_C/[~2.1]")

    def layout(self):
        self.folders.root = ".."
        self.folders.subproject = "conA"
        cmake_layout(self)
    
    #def package_id(self):
    #    self.info.requires["Hello1"].semver_direct_mode()


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("hello2", dst="bin", keep_path=False)
