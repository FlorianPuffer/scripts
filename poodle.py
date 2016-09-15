import socket
import ssl
import argparse


parser = argparse.ArgumentParser(description='Poodle scanner')
parser.add_argument('--host', '-H', default=None,required=True, help='hostname/IP')
parser.add_argument('--port', '-p', default="443", help='port to connect to (default=443)')



def doCheck(host, port):
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    ctx.verify_mode = ssl.CERT_NONE

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        ssl_sock = ctx.wrap_socket(s, server_hostname=str(host), do_handshake_on_connect=True)
        ssl_sock.connect((str(host), int(port)))
        ssl_sock.close()
        return "enabled"
    except Exception as e:
        return str(e)


def main():
    args = parser.parse_args()
    args = vars(args)

    host = args["host"]
    port = args["port"]

    print("Connect to host " + host + ":" + port + " with SSLv3")
    ret = doCheck(host, port)
    if(ret == "enabled"):
        print("SSLv3 is enabled, vulnerable for POODLE attack")
    else:
        print("Socket returns following message:" + ret)
        print("Not vulnerable to POODLE attack")
    print("Check is done")

main()
