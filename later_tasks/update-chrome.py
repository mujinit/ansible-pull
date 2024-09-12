import os
import subprocess

def terminate_chrome():
    """Terminates Chrome if it is running."""
    print("Terminating Chrome if running...")
    try:
        # Kill all instances of Chrome
        subprocess.run(['pkill', 'chrome'], check=True)
        print("Chrome terminated.")
    except subprocess.CalledProcessError:
        print("Chrome is not running or could not be terminated.")

def update_chrome():
    """Updates Chrome to the latest version."""
    print("Updating Chrome to the latest version...")
    try:
        # Update package list and install the latest version of Chrome
        subprocess.run(['sudo', 'apt', 'update', '-qq'], check=True)
        subprocess.run(['sudo', 'apt', 'install', '-y', '--reinstall', 'google-chrome-stable'], check=True)
        print("Chrome updated to the latest version.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update Chrome: {e}")

def launch_chrome():
    """Launches Chrome."""
    print("Launching Chrome...")
    try:
        # Start Chrome in the background
        subprocess.run(['google-chrome', '&'], check=True)
        print("Chrome launched.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Chrome: {e}")

def main():
    terminate_chrome()
    update_chrome()
    launch_chrome()

if __name__ == "__main__":
    main()
