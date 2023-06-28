import proxyServer
from multiprocessing import Process


def main():
    black_proxy = Process(target=proxyServer.start, args=("192.168.2.41", "10.0.6.20", 443, "schemas", "tls_black.crt", "tls_black.key", ))
    red_proxy = Process(target=proxyServer.start, args=("10.0.5.144", "192.168.8.20", 443, "schemas", "tls_red.crt", "tls_red.key", ))

    black_proxy.start()
    red_proxy.start()

    black_proxy.join()
    red_proxy.join()


if __name__ == '__main__':
    main()
