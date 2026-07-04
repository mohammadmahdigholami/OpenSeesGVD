from setuptools import Distribution, find_packages, setup


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(
    package_dir={"": "python_package"},
    packages=find_packages(where="python_package"),
    include_package_data=True,
    package_data={
        "gvd_openseespy": ["*.pyd"],
    },
    distclass=BinaryDistribution,
)
