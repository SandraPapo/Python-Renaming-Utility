import os

def getPath():
  global path
  path = ('/Users/Sandra/Desktop/tecumseh and lanlois area')
  return path

def increment():
  inc = input('What to increment by? ')
  return inc
  
def initial():
  global i
  i = input('What is the first value? ')


def filename(inc):
  a = 64
  i = i - inc
  for Filename in os.listdir(path):
    if Filename.endswith("opy.jpg"):
      i = i + inc
      a = 64
    else:  
      os.rename(Filename, str(i).zfill(2) + "_" + chr(a) + ".jpg")
      a = a + 1

def clean():
  for Filename in os.listdir(path):
    if Filename.endswith("opy.jpg"):
      os.remove(Filename)
    if Filename.endswith("@.jpg"):
      os.rename(Filename, Filename.replace('_@', ' '))
      
def deleteExtra():
  for Filename in os.listdir(path):
    os.remove(Filename)
    break

getPath();
os.chdir(path );
initial ();
inc.increment();
filename(inc);
clean();
deleteExtra();


