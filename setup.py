from setuptools import setup, find_packages

setup(
    name="certbot_dns_",
    version="1.0",
    author="miigotu",
    url="hhttps://github.com/miigotu/certbot-dns-godaddy",
    description="Obtain certificates using a DNS TXT record for GoDaddy domains",
    long_description="This is a plugin for certbot that allows one to Obtain certificates using a DNS TXT record for GoDaddy domains",
    long_description_content_type="text/plain",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: System :: Systems Administration"
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "certbot>=1.18.0,<3.0",
        "requests>=2.20.0,<3.0",
        "dnspython>=2.0.0,<3.0"
    ],
    entry_points={
        "certbot.plugins": [
            "dns-godaddy = certbot_dns_godaddy:Authenticator",
        ]
    }
)
