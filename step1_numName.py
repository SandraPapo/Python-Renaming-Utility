import os

os.chdir('/Users/Sandra/Desktop/tecumseh and lanlois area')
i=0

for Filename in os.listdir('/Users/Sandra/Desktop/tecumseh and lanlois area'):
  os.rename(Filename, str(i).zfill(3) + ".jpg")
  i=i+1

    
for Filename in os.listdir('/Users/Sandra/Desktop/tecumseh and lanlois area'):
  if Filename.endswith("00.jpg"):
    os.remove(Filename)
