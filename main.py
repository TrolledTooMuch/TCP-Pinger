import socket, time
import argparse
import os

clear = lambda: os.system('cls' if os.name == \
                  'nt' else 'clear')

def tcping(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start_time = time.time()
        s.connect((host, port))
        end_time = time.time()
        
        return 1000 * (end_time - start_time)
    except TimeoutError:
        print('Error connecting to the host.')
    

def isvalidhost(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False


if __name__ == '__main__':
    clear() 

    parser = argparse.ArgumentParser()
    parser.add_argument('host', metavar='', type=str, help='Host/IP the TCP ping goes to.')
    parser.add_argument('-p', '--port', metavar='', required=True, type=int, help='The TCP ping port.')
    parser.add_argument('-t', '--timeout', metavar='', required=False, type=int, help='Timeout of the ping connection.')
    args = parser.parse_args()

    if args.timeout:
        socket.setdefaulttimeout(args.timeout)
    if isvalidhost(args.host) == True:
        for index in range(50):
            try:
                host = args.host
                port = args.port
                ping = tcping(host=host, port=port)
                print('Connected to %s:%s - connect time: %.3f' % (host, port, ping))
                time.sleep(1)
            except KeyboardInterrupt:
                os._exit(0)
        print('Finished TCP Ping on %s:%s' % (host, port))
    else:
        print('Invalid Host IP. Try again.'); os._exit(0)
