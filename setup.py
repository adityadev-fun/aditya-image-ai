from setuptools import setup, find_packages

setup(
    name="aditya-image-ai",
    version="0.1.0",
    description="A Discord bot module for AI image generation using OpenAI and custom models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Aditya Verma",
    author_email="businessaditya98@gmail.com",
    url="https://github.com/adityadev-fun/aditya-image-ai",
    install_requires=[
        "discord.py",
        "openai",
        "Pillow",
        "requests",
        "torch"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
