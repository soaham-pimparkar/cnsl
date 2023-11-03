import socket
import sys

print( 
    """
    What do you want to do??:
    1. Get IP from Name
    2. Get Name from IP
    """
)
option = int( input( "Enter option: " ) )
if option == 1:
    name = input( "Enter url: " ) 
    print( socket.gethostbyname( name ) ) 
elif option == 2:
    addr = input( "Enter IP: " )
    print( socket.gethostbyaddr( addr )[0] )