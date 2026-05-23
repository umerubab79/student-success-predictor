from setuptools import find_packages, setup

setup(
    name="student_success_predictor",   
    version="0.1.0",                    
    author="Ume Rubab",            
    author_email="umerubab5789@gmail.com",
    description="A machine learning project to predict student success based on performance data", 
    long_description=open("README.md").read(),   
    long_description_content_type="text/markdown",
    url="https://github.com/umerubab79/student-success-predictor", 
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "flask"
    ],  
    classifiers=[                      
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",            
)
