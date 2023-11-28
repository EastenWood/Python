from shutil import *
from glob import glob

print("BEFORE:", glob("some.txt"))
move(r"F:\some.txt ", "E:")
print("AFTER:", glob("some.txt"))
