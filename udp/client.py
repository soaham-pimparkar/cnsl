import socket
import os

HOST = "192.168.130.78"
PORT = 8080

with socket.socket( socket.AF_INET , socket.SOCK_DGRAM ) as client_socket:

    while True:
        file_path = input( "yaha pe file path enter kar!: " )
        with open( file_path , "rb" ) as file:
            file_bytes = file.read()
        file_name = os.path.basename( file_path )
        message = "{}{}".format( chr( len( file_name ) ) , file_name )
        message += "{}{}".format( chr( len( file_bytes ) ) , file_bytes )
        client_socket.sendto( message.encode() , ( HOST , PORT ) )