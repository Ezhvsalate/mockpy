from colorama import Fore

global verbose
verbose = False


def error(msg):
    print(Fore.RED + msg)


def warn(msg):
    print(Fore.YELLOW + msg)


def success(msg):
    print(Fore.GREEN + msg)


def info(msg):
    print(msg)
