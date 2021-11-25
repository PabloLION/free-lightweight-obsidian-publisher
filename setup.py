from setuptools import setup

setup(
    name="free-lightweight-obsidian-publisher",
    version="0.1.0",
    packages=["."],
    entry_points={"console_scripts": ["flop = FlopCLI:main"]},
)
