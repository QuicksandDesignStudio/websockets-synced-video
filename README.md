# websockets-synced-video

Very WIP : Full python web sockets based implementation of video sync across clients

**main_module**

- server.py : accepts a time code from any client and broadcasts to all clients
- timekeeper.py : right now
  it just creates a random number between 1 and 600000 miliseconds on a seprate thread
  every 10 seconds (send_freq) sends it to the server

**client_module**

- client.py
  creates a player object to play the video on a separate thread
  listens for timecode braodcast from server and when it comes calls the set\*time() method on the player object
- player.py
  creates instance of vlc player and plays videos
  seeks to time when the set_time() method is called
