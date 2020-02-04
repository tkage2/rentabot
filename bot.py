import socket
import parser
import connection

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
port = 6667
channel = "##bot-testing-123"
botnick = "PythonBot123"
admin = ""
password = "12345"

admin_list = []

ircsock.connect((server, port))
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "n", "UTF-8"))
ircsock.send(bytes("NICK "+ botnick +"n", "UTF-8"))


def join_channel(chan): # join channel(s).
    ircsock.send(bytes("JOIN "+ chan +"n", "UTF-8")) 
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:  
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('nr')
        print(ircmsg)
    
def ping(): # respond to server Pings.
    ircsock.send(bytes("PONG :pingisn", "UTF-8"))
  
def sendmsg(msg, target=channel): # sends messages to the target.
    ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"n", "UTF-8"))
  
def main():
    join_channel(channel)
    while 1:
  
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
            if len(name) < 17:
                if message.find('Hi ' + botnick) != -1:
                    sendmsg("Hello " + name + "!")
                if message.find(password) != -1:
                    admin_list.append(name)
                    sendmsg("You are now added to admin-list!")
                if message[:5].find('.tell') != -1:
                    target = message.split(' ', 1)[1]
                if target.find(' ') != -1:
                    message = target.split(' ', 1)[1]
                    target = target.split(' ')[0]
                else:
                    target = name
                    message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
            sendmsg(message, target)