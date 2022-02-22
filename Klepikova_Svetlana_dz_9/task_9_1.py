import time


class TrafficLight:
    __color: dict = {4: 'red', 2: 'yellow', 3: 'green'}


    def running(self):
        for key, val in self.__color.items():
            print(f'{val} {key} сек', end='\n')
            time.sleep(key)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
