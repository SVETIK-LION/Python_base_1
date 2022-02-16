import time


class TrafficLight:
    __color: str = 'some_color'


    def running(self, timing = 4):
        if timing == 4:
            __color = 'red'
            print(f'{__color} {timing} сек')
            time.sleep(4)
            timing -= 2

        if timing == 2:
            __color = 'yellow'
            print(f'{__color} {timing} сек')
            time.sleep(2)
            timing += 1


        if timing == 3:
            __color = 'green'
            print(f'{__color} {timing} сек')
            time.sleep(3)
            timing -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
