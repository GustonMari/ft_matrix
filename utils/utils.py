from colorama import Fore

def green(text):
    """Print green text."""
    print(Fore.GREEN + text + Fore.RESET)
    
def red(text):
    """Print red text."""
    print(Fore.RED + text + Fore.RESET)

def yellow(text):
    """Print yellow text."""
    print(Fore.YELLOW + text + Fore.RESET)

def blue(text):
    """Print blue text."""
    print(Fore.BLUE + text + Fore.RESET)

def abs(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    return x

def max(x, y):
    """Return the maximum between x and y."""
    if x > y:
        return x
    return y

def min(x, y):
    """Return the minimum between x and y."""
    if x < y:
        return x
    return y