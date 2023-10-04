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

def custom_abs(x):
    """Return the custom_absolute value of x."""
    if x < 0:
        return -x
    return x

def custom_max(x):
    """Return max value of x."""
    x_list = list(x)  # Convert the generator to a list
    if not x_list:
        raise ValueError("Input sequence is empty")  # Handle empty sequence
    max_value = x_list[0]
    for i in x_list:
        if i > max_value:
            max_value = i
    return max_value

def custom_min(x, y):
    """Return the custom_minimum between x and y."""
    if x < y:
        return x
    return y