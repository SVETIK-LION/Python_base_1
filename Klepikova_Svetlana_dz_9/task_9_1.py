import time, sys


class TrafficLight:
    __color: str = 'some_color'


    def running(self):
        colors = {4: 'red', 2: 'yellow', 3: 'green'}
        for key, val in colors.items():
            TrafficLight.__color = val
            print(f'{TrafficLight.__color} {key} сек', end='\n')
            time.sleep(key)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
