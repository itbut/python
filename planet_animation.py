import os, time
#this doing something with console for windows it should be 'clr'
os.system('clear')
#files of the art itself
planetart = ["planet_art.txt", "planet_art2.txt", "planet_art3.txt", "planet_art4.txt", "planet_art5.txt", "planet_art6.txt", "planet_art7.txt", "planet_art8.txt", "planet_art9.txt", "planet_art10.txt", "planet_art11.txt", "planet_art12.txt", "planet_art13.txt", "planet_art.txt"]

#everything down is about animation we could change txt files and just reuse the code....bingo!
def animator(filenames, delay = 1, repeat = 1):
    frames = []
    for name in planetart:
        #set encoding to show up any characters
        with open(name, "r", encoding="utf8") as f:
            #shows files in whole but if changed to readline or readlines shows or just first line from file or somehow first line of first file appers to be white
            frames.append(f.read())
    for i in range(repeat):
        for frame in frames:
            #add some color to output - green in our case
            print("\u001b[32m".join(frame))
            #allows to speedup
            time.sleep(1)
            #ullows to show files one by one without this we see all of them at the same time and of course no animation in that
            os.system('clear')

#without it nothing is working e.g. moving as supposed to and guy from youtube said we need it
animator(planetart, delay = 0.5, repeat = 1)
#cancel coloring
print("\u001b[0mHappy New Year!")