# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #prepare a server socket
  serverSocket.bind(("127.0.0.1", port))
  serverSocket.listen(1)




  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024)
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:],)
      
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"

      #This variable can store your headers you want to send for any valid or invalid request.
      #Content-Type above is an example on how to send a header as bytes
      valid = "HTTP/1.1 200 OK\r\n\r\n".encode()
      e = "404 File Not Found\r\n".encode()


      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in start
      connectionSocket.send(valid)
      connectionSocket.send(f)


      #Fill in end
               

      #Send the content of the requested file to the client
      for i in f: #for line in file
       connectionSocket.send(i)


      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start
      connectionSocket.send(Exception)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
