from conans import ConanFile, tools, Meson
import os


class LibCameraConanFile(ConanFile):
    name = "libcamera"
    version = "0.1"
    generators = "pkg_config"
    build_requires = "ninja/1.10.2"
    requires = "boost/1.77.0"
    settings = "os", "compiler", "build_type"
    exports_sources = "*", "!build"
    _meson = None

    def __configure_meson(self):
        if self._meson is None:
            _meson = Meson(self)
            _meson.configure(build_folder="build")
            self._meson = _meson
        return self._meson

    def build(self):
        meson = self.__configure_meson()
        meson.build()

    def package(self):
        meson = self.__configure_meson()
        meson.install()
