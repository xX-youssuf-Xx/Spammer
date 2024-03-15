import pyautogui
import time
import keyboard 
import sys      
import threading

# Global variable to signal the typing thread to stop
stop_typing = False

def type_and_enter(message, times,Delay_in_sec):
    if(Delay_in_sec == ""):
        print("3 Sec delay before Typing")
        time.sleep(3) 
        # Loop for the specified number of times
        timer = 0
        for _ in range(times):
            if stop_typing:  # Check if the typing thread should stop
                break
            timer += 1
            # Type the message
            pyautogui.typewrite(message + str(timer))
            # Press Enter
            pyautogui.press('enter')
    elif(Delay_in_sec != ""):
        print("3 Sec delay before Typing")
        time.sleep(3) 
        # Loop for the specified number of times
        timer = 0
        for _ in range(times):
            if stop_typing:  # Check if the typing thread should stop
                break
            timer += 1
            # Type the message
            pyautogui.typewrite(message + str(timer))
            # Press Enter
            pyautogui.press('enter')
            # Add a small delay between each iteration (optional)
            time.sleep(int(Delay_in_sec)) 
            
    if (not stop_typing):
        message_to_type = input("Message: ")
        number_of_times = int(input("Times: "))
        Delay_in_sec = input("delay in seconds (Decimel): ")
        # Call the function to type the message and press Enter
        type_and_enter(message_to_type, number_of_times,Delay_in_sec)





def monitor_keyboard():
    global stop_typing  # Access the global variable
    print("Press ESC to exit.")
    keyboard.wait('esc')  # Wait for the ESC key press
    stop_typing = True   # Set the stop_typing flag to True
    sys.exit()  # Exit the program

def main():
    message_to_type = input("Message: ")
    number_of_times = int(input("Times: "))
    delay_in_sec = float(input("Delay in seconds (Decimal): "))
    
    # Start the typing thread
    typing_thread = threading.Thread(target=type_and_enter, args=(message_to_type, number_of_times, delay_in_sec))
    typing_thread.start()

    # Start the keyboard monitoring thread
    keyboard_thread = threading.Thread(target=monitor_keyboard)
    keyboard_thread.start()

    # Wait for the typing thread to finish
    typing_thread.join()

if __name__ == "__main__":
    main()