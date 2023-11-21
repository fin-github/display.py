from colorama import Fore, Back, Style



class Display:
    
    class Presets:
        def __init__(self):
            self.redOutline = {
                (1,1): Fore.RED,
                (1,2): Fore.RED,
                (1,3): Fore.RED,
                (1,4): Fore.RED,
                (1,5): Fore.RED,
                (2,5): Fore.RED,
                (3,5): Fore.RED,
                (4,5): Fore.RED,
                (5,5): Fore.RED,
                (5,4): Fore.RED,
                (5,3): Fore.RED,
                (5,2): Fore.RED,
                (5,1): Fore.RED,
                (2,1): Fore.RED,
                (3,1): Fore.RED,
                (4,1): Fore.RED
    }
    
    def render(pixels:dict = {}, symbol:str = " x", defaultColor:Fore = "", size:tuple = (5,5)):
        for x in range(1,size[0]+1):
            for y in range(1,size[1]+1):
                if (y,x) in pixels:
                    temp = pixels[(y,x)]
                else:
                    temp = defaultColor
                print(temp + f" {symbol}" + Style.RESET_ALL, end="")
            print()
