import time
import os

def run_image_classification():
    os.system("python3 image_classification.py")

def main():
    while True:
        if os.path.exists("management_signal.txt"):
            with open("management_signal.txt", "r") as f:
                signal = f.read().strip()

            if signal == "In button clicked":
                run_image_classification()
            elif signal == "Out button clicked":
                run_image_classification()

            with open("management_signal.txt", "w") as f:
                f.write("")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
