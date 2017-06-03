#!/usr/bin/python3
import socket
import os
import stopwords.stopstrip as stopstrip

print("Setting up....\n\n\n")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#This is the name of the server and channel we’ll be connecting to. We could hard code these, but having a variable makes a couple of steps easier. 
server = "card.freenode.net" # Server
channel = "##botbot" # Channel
#This is what we’ll be naming the bot. It is how other users will see the bot in the channel. 
botnick = "asciime" # nick
print("Joining IRC network...\n\n\n")
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
#Once we’ve established the connection we need to send some information to the server to let the server know who we are.
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) # user information
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot
#So here we take in the channel name, as part of the function, then send the join command to the IRC network. 
print("Setting up functions...\n\n\n")
def joinchan(chan): # join channel(s).
  print("Auth...\n")
  passcode = input("Password: ")
  ircsock.send(bytes("NICKSERV identify "+ passcode +"\n", "UTF-8"))
  print("Joining channel....\n\n\n")
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8"))
  #Something to note, the "\n” at the end of the line denotes to send a new line character. It lets the server know we’re finished with that command rather than chaining all the commands onto the same line.
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1: 
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)

def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
#All we need for this function is to accept a variable with the message we’ll be sending and who we’re sending it to. We will assume we are sending to the channel by default if no target is defined. 

def sendmsg(msg, target=channel): # sends messages to the target.
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ str(msg) +"\n", "UTF-8"))
#Main function of the bot.
def main():
  # start by joining the channel we defined in the Global Variables section.
  joinchan(channel)
  print("Ready....\n\nRunning....\n\n\n")
  while 1:
    #We then assign it to the ircmsg variable for processing.
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    # This part will remove any line break characters from the string. If someone types in "\n” to the channel, it will still include it in the message just fine. 
    ircmsg = ircmsg.strip('\n\r')
    #For debug:
    print(ircmsg)
    #Here we check if the information we received was a PRIVMSG.
    if ircmsg.find("PRIVMSG") != -1:
      name = ircmsg.split('!',1)[0][1:]
      #Above we split out the name, here we split out the message.
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
      #So with this check we make sure we’re not responding to an invalid user or some other message.
      if len(name) < 17:
        if message.find('Hi ' + botnick) != -1:
          sendmsg("Hello " + name + "!")
        if message[:6].find(".stop") != -1:
            question = message.split(' ', 1)[1]
            riddedobj = stopstrip.ridstop(question)
            ridded = riddedobj.stripstop()
            sendmsg(ridded.stripstop)
        #The whole message should look like ".tell [target] [message]” to work properly.
        if message[:5].find('.tell') != -1:
          target = message.split(' ', 1)[1]
          if target.find(' ') != -1:
              message = target.split(' ', 1)[1]
              target = target.split(' ')[0]

          #if there is no defined message and target separation, botbot sends a message to the user letting them know they did it wrong.
          else:

            target = name
            message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
          #And finally we send the message to our target.
          sendmsg(message, target)
        # says something to the channel
        if message[:4].find(".say") != -1:
              junk = message.split(" ", 1)[1]
              sendmsg(junk)
        # uses urandom      
        if message[:7].find(".random") != -1:
            encrypt = int(message.split(" ",1)[1])
            sendmsg("creating random string...")
            msg = os.urandom(encrypt)
            message = str(msg)
            sendmsg(message)
          
    else:
      #Check if the information we received was a PING request. If so, we call the ping() function we defined earlier so we respond with a PONG.
      if ircmsg.find("PING :") != -1:
        ping()
#start your engines...
main()
