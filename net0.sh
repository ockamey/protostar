echo -e "$(cat)" | nc 127.0.0.1 2999

# In python: 
# struct.pack("I", <variable>)
# don't forget to send EOF (ctrl - d)
