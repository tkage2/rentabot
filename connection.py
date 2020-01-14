class Connection:
    def __init__(self, port, server, channel, botnick):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.server = server
        self.channel = channel
        self.botnick = botnick
        
    def connect(self):
        self.connection_socket.connect((server, 6667))
        self.connection_socket.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "n", "UTF-8"))
        self.connection_socket.send(bytes("NICK "+ botnick +"n", "UTF-8"))