import time


class TrafficLight:
    __color: str = 'some_color'


    def running(self, timing = 4):
        if timing == 4:
            TrafficLight.__color = 'red'
            print(f'{TrafficLight.__color} {timing} сек')
            time.sleep(4)
            timing -= 2

        if timing == 2:
            TrafficLight.__color = 'yellow'
            print(f'{TrafficLight.__color} {timing} сек')
            time.sleep(2)
            timing += 1


        if timing == 3:
            TrafficLight.__color = 'green'
            print(f'{TrafficLight.__color} {timing} сек')
            time.sleep(3)
            timing -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
