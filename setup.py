from setuptools import setup

setup(
    name='musicapi',
    version='0.3.1',
    description='QQ音乐和网易云音乐非会员歌曲的直链获取',
    url="https://github.com/Danny-Yxzl/musicapi",
    author="Yixiangzhilv",
    author_email="mail@yixiangzhilv.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords="music qq wyy",
    install_requires=["requests", "fake_useragent"],
    packages=["musicapi"],
    project_urls={
        "Bug Reports": "https://github.com/Danny-Yxzl/musicapi/issues",
        "Say Thanks!": "https://www.yixiangzhilv.com/",
        "Source": "https://github.com/Danny-Yxzl/musicapi",
    },
)
