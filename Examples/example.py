from tool import Display
from colorama import Fore

# Example preset
# Display.render(Display.Presets().redOutline)



Display.render(
    {
        (1,3): Fore.BLUE
    }
)
print("\n\n")
Display.render(
    Display().Presets().redOutline
)
