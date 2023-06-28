import proxyServer
from multiprocessing import Process


def main():
    black_proxy = Process(target=proxyServer.start, args=("10.130.1.112", "10.130.7.49", 5000,))
    red_proxy = Process(target=proxyServer.start, args=("192.168.5.1", "192.168.5.1", 5000,))

    black_proxy.start()
    red_proxy.start()

    black_proxy.join()
    red_proxy.join()


if __name__ == '__main__':
    main()
>>>>>>> d1aa8d7 (added validator skeleton, a flask proxy server skeleton and an example main program to run the two proxies)
