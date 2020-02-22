import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="predict_attire_for_weather_using_fargate",
    version="0.0.1",

    description="Predict attire for weather using fargate",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "attire_predictor_stacks"},
    packages=setuptools.find_packages(
        where="attire_predictor_stacks"),

    install_requires=[
        "aws-cdk.core==1.24.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
