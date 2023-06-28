import proxyServer
from multiprocessing import Process


def main():
    black_proxy = Process(target=proxyServer.start, args=("10.130.1.112", "10.130.7.49", 5000, "schemas", "tls_black.crt", "tls_black.key", ))
    red_proxy = Process(target=proxyServer.start, args=("192.168.5.1", "192.168.5.1", 5000, "schemas", "tls_red.crt", "tls_red.key", ))

    black_proxy.start()
    red_proxy.start()

    black_proxy.join()
    red_proxy.join()


if __name__ == '__main__':
    main()
