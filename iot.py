from sense_hat import SenseHat
import time

sense = SenseHat()

sense.get_temperature()


def get_temp():
    t = sense.get_temperature()
    t = round(t, 2)
    sense.show_message(str(t))


def main():
    while True:
        get_temp()
        time.sleep(5)


if __name__ == '__main__':
    main()


