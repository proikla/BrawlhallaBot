# BrawlhallaBot
BrawlHalla bot for grinding exp and money.
This bot can farm some coins and exp while you sleep

![image](https://user-images.githubusercontent.com/58581541/173185294-d33aad46-3b42-4788-a22b-69c82fb99547.png)

This simple python script searches for an image of your name in brawlhalla and manipulates your character based on the coordinates of the image.

If you are on the "stage", the script will attack, but when you are "offstage", the script will return to the stage.

When the match is over script will start a new one.

## Set up
### Install git
https://github.com/git-guides/install-git
### Clone project
```
git clone https://github.com/proikla/BrawlhallaBot 
cd BrawlhallaBot
```
### Install requirements
```
pip install -r requirements.txt
```

## How to use
#### Brawlhalla settings
Open brawlhalla, set these settings : 

![image](https://user-images.githubusercontent.com/58581541/173115585-36379276-1431-4742-9834-d36277c62ce0.png)(Display mode: maximized, Camera mode: fixed, Player names: only you)

Set this avatar:

![image](https://user-images.githubusercontent.com/58581541/173119224-27f1a225-2770-4e46-bef0-ca11ba191e3f.png)

then go to Custom Game Room > Create Room > Private Room, then choose your character. 
Then you need to setup your lobby. The optimal settings are:

![image](https://user-images.githubusercontent.com/58581541/173114325-23e5fae3-84d8-487f-a0ce-688a9eef3422.png)

Then you should add the bots and set their difficulty to Easy.

![image](https://user-images.githubusercontent.com/58581541/173114690-bc17cb6d-9bd2-4003-998e-dccb4c223431.png)

Start the game on map Big Thundergard Stadium

![image](https://user-images.githubusercontent.com/58581541/173114956-ec54586a-0924-49e5-b686-b5133485cb46.png)

Then screenshot the game...

![image](https://user-images.githubusercontent.com/58581541/173115171-ebe02b15-d1fa-4506-801b-22b006864988.png)

And crop it like this 

![image](https://user-images.githubusercontent.com/58581541/173115276-dfc66b23-5bb8-4da6-805d-3b018494bf59.png)

the image must be in .png format

Put this image to BrawlhallaBot/images

#### Start script

Once you have set up the lobby and started the game at the Big Thundergard Stadium, start 'main.py':
```
python main.py
```
enter the name of the picture and switch to the brawlhalla window. The script will be executed while the active window is brawlhalla.

Make sure you're using FullHd monitor (1920x1080). Make sure active window is brawlhalla. Make sure you are using Maximised mode. Make sure attack key is 'J', Heavy attack key is 'K', Aim Up key is 'W', Jump key is 'SPACE'.

Apologies for my poor English

*Do not judge strictly, this is my very first project*
