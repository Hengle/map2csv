from PIL import Image
import os


backgrounds = {'default': {'name': 'Desert', 'bgColor1': '#ec9e6f', 'bgColor2': '#f9a575'},
    'mine': {'name': 'Mine', 'bgColor1': '#5b4150', 'bgColor2': '#5f4454'},
    'oasis': {'name': 'Oasis', 'bgColor1': '#deab71', 'bgColor2': '#eab477'},
    'grassfield': {'name': 'Grassy Field', 'bgColor1': '#388e52', 'bgColor2': '#3c9657'},
    'city': {'name': 'City', 'bgColor1': '#8d546d', 'bgColor2': '#945973'},
    'neon': {'name': 'Retropolis', 'bgColor1': '#543f69', 'bgColor2': '#5a426f'},
    'ship': {'name': 'Pirate Ship', 'bgColor1': '#d57454', 'bgColor2': '#e07a59'},
    'arcade': {'name': 'Arcade', 'bgColor1': '#2f2a4b', 'bgColor2': '#322c4f'},
    'survival': {'name': 'Wasteland', 'bgColor1': '#bc7e5c', 'bgColor2': '#c58562'},
    'mortuary': {'name': 'Mortuary', 'bgColor1': '#46314e', 'bgColor2': '#4a3452'},
    'holiday': {'name': 'Holiday', 'bgColor1': '#2c9af2', 'bgColor2': '#2ea2ff'}}


events = {'custom': {'name': 'Custom', 'bannerColor1': '#05a1f7'},
	'gemGrab': {'name': 'Gem Grab', 'bannerColor1': '#9a3cf3'},
	'showdown': {'name': 'Showdown', 'bannerColor1': '#81d61f'},
	'duoShowdown': {'name': 'Duo Showdown', 'bannerColor1': '#81d61f', 'notDesignable': True},
	'heist': {'name': 'Heist', 'bannerColor1': '#d65cd3'},
	'bounty': {'name': 'Bounty', 'bannerColor1': '#00cfff'},
	'brawlBall': {'name': 'Brawl Ball', 'bannerColor1': '#8ca0e0'},
	'siege': {'name': 'Siege', 'bannerColor1': '#f05030'},
	'takedown': {'name': 'Takedown', 'bannerColor1': '#387efc'},
	'loneStar': {'name': 'Lone Star', 'bannerColor1': '#da3f5c'},
	'bigGame': {'name': 'Big Game', 'bannerColor1': '#dc2423'},
	'roboRumble': {'name': 'Robo Rumble', 'bannerColor1': '#dc2423'},
	'bossFight': {'name': 'Boss Fight', 'bannerColor1': '#dc2423'},
	'presentPlunder': {'name': 'Present Plunder', 'bannerColor1': '#00da48'},
	'hotZone': {'name': 'Hot Zone', 'bannerColor1': '#e33752'},
	'powerPlay': {'name': 'Power Play', 'bannerColor1': '#0098ec', 'notDesignable': True}}


for map_image in os.listdir('maps'):
    im = Image.open(f'maps/{map_image}', 'r')
    width, height = im.size

    print("Width: {}".format(width))
    print("Height: {}".format(height))

    im.show()

    pixel_values = set(im.getdata())
    for pixel in pixel_values:
        R, G, B = pixel[0], pixel[1], pixel[2] 
        if map_image.endswith('.png'): opacity = pixel[3]
        color_hex = (int.to_bytes(R, 1, 'big')+int.to_bytes(G, 1, 'big')+int.to_bytes(B, 1, 'big')).hex()
        for bgr in backgrounds:
            if f'#{color_hex}' == backgrounds[bgr]['bgColor1'] or f'#{color_hex}' == backgrounds[bgr]['bgColor2']:
                print(f'Background is {backgrounds[bgr]["name"]}')
        for event in events:
            if f'#{color_hex}' == events[event]['bannerColor1']:
                print(f'{events[event]["name"]} was found')
            else:
                print(f'#{color_hex}')
