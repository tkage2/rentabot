class Parser():
    def __init__(self, irc_socket):
        self.irc_socket = irc_socket
        
    def parse():
        msg = self.irc_socket.recv(2048).decode("UTF-8")
        msg = ircmsg.strip('nr')
        return msg