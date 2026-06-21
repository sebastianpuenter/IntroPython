from colorama import init, Fore, Back, Style

# Initialize Colorama (mandatory for Windows, safe for other OS)
init(autoreset=True)

# Print colored foreground text
print(Fore.RED + 'This is red text!')
print(Fore.GREEN + 'This is green text!')

# Combine text color with a background color
print(Fore.WHITE + Back.BLUE + 'White text on a blue background')

# Apply text styling (e.g., BRIGHT)
print(Style.BRIGHT + Fore.YELLOW + 'This is bright yellow text')
