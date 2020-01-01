import os, time
os.system('clear')

filenames = ["planet_art.txt", "planet_art2.txt", "planet_art3.txt", "planet_art4.txt", "planet_art5.txt", "planet_art6.txt", "planet_art7.txt", "planet_art8.txt", "planet_art9.txt", "planet_art10.txt", "planet_art11.txt", "planet_art12.txt", "planet_art13.txt"]
frames = []

for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.read())
for i in range(1):
    for frame in frames:
            print("".join(frame))
            time.sleep(1)
            os.system('clear')