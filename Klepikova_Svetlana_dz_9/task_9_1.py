import time, sys


class TrafficLight:
    __color: str = 'some_color'


    def running(self):
        colors = {4: 'red', 2: 'yellow', 3: 'green'}
        for key, val in colors.items():
            TrafficLight.__color = val
            for sec in range(1, key + 1):
                sys.stdout.write(f'\r{TrafficLight.__color} {sec} сек')
                time.sleep(1)
            print()


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
