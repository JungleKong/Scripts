from pynput import keyboard

i = 1
a = []

def on_press(key):
    '按下按键时执行。'
    try:
        # print('alphanumeric key {0} pressed'.format(key.char))
        a.append(key.char)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    #通过属性判断按键类型。


def on_release(key):
    '松开按键时执行。'
    # print('{0} released'.format(key))
    if key == keyboard.Key.enter:

        # Stop listener
        return False



while True:

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print("第{}次记录，结果为：{}".format(i, "".join(a)))
    i += 1





