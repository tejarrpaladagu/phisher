import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = ['FacebookChatPhisher', 'tweetGenerator', 'FacebookPoster']
setuptools.setup(
    name="Automated_Spear_Phisher_Tool", 
    version="0.0.1",
    author="Abdullah Chattha",
    author_email="abdullahmeo11@gmail.com",
    description="This program is automated spear phishing tool that works on both Facebook and Twitter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abdullah-chattha/Fb-Twitter-gui",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    python_requires='>=3.8',
)