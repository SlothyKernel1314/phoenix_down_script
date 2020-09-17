# Phoenix Down Script

Phoenix Down Script is a back-end application whose goal is to manage many scripts, intended to save some user information for certain sites (Trello, Steam, Youtube, Reddit, Twitter, Pocket...), via their respective APIs.

This application also allows you to save Firefox profiles and JDownloader link collectors.

The data is then saved as log files, saved locally, and uploaded to a server.

## Why I developed Phoenix Down Script ?

No one is safe from the loss or/and theft of their accounts on the Internet. If Phoenix Down Script won't allow you to recover them, this application will at least make it easier for you to recover your data, by regularly saving them in log files.

Just one example : if you lose your Twitter account, it would be very useful to have the list of your followers on hand to recreate an account.

Please note that the application does not allow reimporting this data as is, but that it provides a sound basis to develop your own reimport methods, using the relevant APIs.

The logs offer for this purpose your saved data in human readable form, but also in computer format (often data in JSON format, requested by most APIs).

## How can Phoenix Down Script help you ?

Phoenix Down Script is not designed to be used on a "turnkey" basis, as it primarily meets my own needs. Nevertheless, a developer could adapt it relatively easily to his own needs. In addition, the highly modular nature of this application facilitates the execution of each script independently of the others ; and independently of the application itself. Finally, as this application uses many APIs, it is an appropriate study object to analyze the basic functioning of these APIs (cf. script folder). The developer will be able to see it as an easy way to get started with them (cf. sample folder).

## What data does the script backup ?

This list may not be complete.

* Firefox :

    1. backup of bookmarks (bookmarkbackups file)
    2. backup of bookmark favicons (favicons.sqlite)
    3. backup of the browsing history, downloads, bookmarks (places.sqlite)
    
* JDownloader :

    1. backup of the download list (latest downloadList*.zip)
    2. backup of the link collector (latest linkcollector*.zip)
    
* Pocket :
    
    1. backup of your articles (ids, titles, URLs + all data in JSON format)
    
* Reddit : 
    
    1. backup of your subscribed subreddits (names + all data in JSON format)
    2. backup of your saved posts (all data in JSON format)
    
* Steam :

    1. backup of your friends list (ids, usernames)
    2. backup of your owned games (ids)
    3. backup of your wishlist (all data in JSON format)
    
* Trello :
    
    1. backup of all your boards (all data in JSON format)
    2. backup of your favorite cards (all data in JSON format)
    
* Twitter :

    1. backup of your followers (ids)
    2. backup of your friends (ids)
    
* Youtube :
    1. backup of your suscribed channels (ids, youtuber usernames + all data in JSON format)
    2. backup of your playlists (names, video ids, video titles + all data in JSON format)

    

## How to run Phoenix Down Script ?