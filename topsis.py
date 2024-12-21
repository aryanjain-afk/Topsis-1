import pathlib
from setuptools import setup

# Set the current directory
CURRENT_DIR = pathlib.Path(__file__).parent

# Load the README file content
README_CONTENT = (CURRENT_DIR / "README.md").read_text()

# Define the setup configuration
setup(
    name="Topsis-Aryan-102218040",
    version="1.0.1",
    description="A tool to calculate TOPSIS scores for ranking alternatives based on criteria.",
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    url="https://github.com/aryan9855/Topsis-Aryan-102218040",
    author="Aryan",
    author_email="admin_aryan@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)
