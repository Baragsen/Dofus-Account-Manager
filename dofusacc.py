import time
import win32api
import win32con
import win32gui

# Define the Dofus window titles
dofus_windows = [
    "Account1 - Dofus (version)",
    "Account2 - Dofus (version)",
    "Account3 - Dofus (version)",
    "Account4 - Dofus (version)",
    "Account5 - Dofus (version)"
]

# Define the keyboard shortcuts for each account
keyboard_shortcuts = [
    ord('1'),
    ord('2'),
    ord('3'),
    ord('4'),
    ord('5')
]

# Activate the Dofus window based on the keyboard shortcut
def activate_dofus_window(shortcut):
    hwnd = win32gui.FindWindow(None, dofus_windows[shortcut-1])
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    else:
        print(f"Window not found: {dofus_windows[shortcut-1]}")


# Function to perform actions for each account
def perform_account_actions(account):
    # Switch to the specified account
    activate_dofus_window(account + 1)

    # Perform actions specific to the account
    # Add your account-specific code here

# Main program loop
while True:
    for account, shortcut in enumerate(keyboard_shortcuts):
        if win32api.GetAsyncKeyState(shortcut):
            perform_account_actions(account)
            time.sleep(0.2)  # Add a small delay to avoid repeated actions
