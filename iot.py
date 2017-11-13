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
        message = input('Enter message to display: ')
        sense.show_message(message)

# temp_calibrated = temp - ((cpu_temp - temp)/5.466)


if __name__ == '__main__':
    main()


