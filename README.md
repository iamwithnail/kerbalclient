# Kerbal Dashboard 

Ever wanted to have at-a-glance stats while you play Kerbal?  Well now you can! 

Updated in real-time (well, every half second).

<img src="img/readme/Screenshot%202021-01-05%20at%2015.50.23.png">

## Setup 

`pip install -r requirements.txt`

You'll need [Kerbal RPC](https://github.com/krpc/krpc). 


Get an API key from [Pusher](www.pusher.com), app key and export the vars. 
```
export PUSHER_APP_ID=pusherappidfromyouraccount
export PUSHER_KEY=pusherkey
export PUSHER_SECRET=somesecretvalue
```

Change the `pusherid` at L28 of `index.html` to your pusher key. 

## Usage

Currently only works in flight mode - will probably bork if you run it while in Space Centre mode, but who knows.  When you're at an
appropriate place (e.g. in your ship and ready to launch), run `python new.py`.  Check your pusher console is receiving updates.

Fly. Enjoy.  