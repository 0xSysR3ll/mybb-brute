
<div align="center">

<!--  <img src="assets/logo.png" alt="logo" width="200" height="auto" />-->
  <h1>MyBB bruteforce tool</h1>
  
  <p>
    A python tool to bruteforce user/passwords on a <a href="https://mybb.com">MyBB</a> forum ! 
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/0xsysr3ll/mybb-brute/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/0xsysr3ll/mybb-brute" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/0xsysr3ll/mybb-brute" alt="last update" />
  </a>
  <a href="https://github.com/0xsysr3ll/mybb-brute/network/members">
    <img src="https://img.shields.io/github/forks/0xsysr3ll/mybb-brute" alt="forks" />
  </a>
  <a href="https://github.com/0xsysr3ll/mybb-brute/stargazers">
    <img src="https://img.shields.io/github/stars/0xsysr3ll/mybb-brute" alt="stars" />
  </a>
  <a href="https://github.com/0xsysr3ll/mybb-brute/issues/">
    <img src="https://img.shields.io/github/issues/0xsysr3ll/mybb-brute" alt="open issues" />
  </a>
</p>
 
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
- [Usage](#eyes-usage)
- [Contributing](#wave-contributing)
- [Disclaimer](#warning-disclaimer)
- [Contact](#handshake-contact)

  

<!-- About the Project -->
## :star2: About the Project

While doing a box on TryHackMe, I had to bruteforce a MyBB Forum.
Because I didn't find any tool to do it, I decided to develop my own. And here it is !

<!-- Getting Started -->
## :toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

<img src="https://img.shields.io/github/pipenv/locked/python-version/0xsysr3ll/mybb-brute?style=flat-square">

This tool has been tested on the latest version available at the time of the development (`1.8.31`)

<!-- Installation -->
### :gear: Installation

```bash
git clone https://github.com/0xSysR3ll/mybb-brute
cd mybb-brute && pip3 install -r requirements.txt
```

<!-- Usage -->
## :eyes: Usage

> This tool can only be used on environments where there is no login attempts limiting (Labs, CTFs, etc)
By default, MyBB added an anti-bruteforce system - you can only do 3 login attempts. After that, you have to wait a certain amount of time + a captcha to solve.


```bash
    __  ___      ____  ____     ____             __     
   /  |/  /_  __/ __ )/ __ )   / __ )_______  __/ /____ 
  / /|_/ / / / / __  / __  |  / __  / ___/ / / / __/ _ \
 / /  / / /_/ / /_/ / /_/ /  / /_/ / /  / /_/ / /_/  __/
/_/  /_/\__, /_____/_____/  /_____/_/   \__,_/\__/\___/ 
       /____/                                           

v1.0 by 0xsysr3ll

usage: mybb-brute.py [-h] -t TARGET (-u USERNAME | -U USER_FILE) (-p PASSWORD | -P PASS_FILE)

A simple MyBB bruteforce tool

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        MyBB Forum ip/domain target (without http/https), eg. 10.10.10.1:8080

Usernames:
  -u USERNAME, --username USERNAME
                        Username to use for bruteforce
  -U USER_FILE, --user-file USER_FILE
                        Usernames file to use for bruteforce

Passwords:
  -p PASSWORD, --password PASSWORD
                        Password to use for bruteforce
  -P PASS_FILE, --pass-file PASS_FILE
                        Passwords file to use for bruteforce
```
<!-- Contributing -->
## :wave: Contributing


Contributions are always welcome, I am not a pro developer !


<!-- License -->
## :warning: Disclaimer

This tool has been developed in the context of a TryHackMe box. I am not in any way responsible for the use you may make with it.


<!-- Contact -->
## :handshake: Contact

0xSysr3ll - [@0xsysr3ll](https://twitter.com/0xsysr3ll) - 0xsysr3ll@pm.me
