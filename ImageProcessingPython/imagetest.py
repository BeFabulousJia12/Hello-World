import Image
import time

'''
I'm trying to process a character image(background is white)
My way processing:
1. Open an image.(only one character without any hot pixel)
2. Convert it into grey image. It can reduce the difficulty by this way.
3. Get Pixels of character, and then fill it with white color.
Turn background as black color.
'''

def convert(img,imgsize):
    array = []
    for x in xrange(max(imgsize)):
        for y in xrange(min(imgsize)):
            r,g,b= img.getpixel((x,y))
            grey = (r*30 + g*59 + b*11)/100
            r = grey
            g = grey
            b = grey 
            if (r not in array):
                array.append(r)
            img.putpixel((x,y), (r,g,b))
    #array is used to check how many different pixels after conversion.
    #Which is meaningless, just to meet my curiosity...
    #And I don't know why there were so many different pixels?
    #It's supposed to be 2 kinds of pixels..........
    array.sort()
    print(array)

    img.save("greyinit.jpg")
    '''
    255 is white color, 50 is D-value set as my pleasure.
    !!!TODO: There must be an algorithm for lerning and training but I don't know
    '''
    for x in xrange(max(imgsize)):
        for y in xrange(min(imgsize)):
            r,g,b= img.getpixel((x,y))
            if(abs(r-255)<=50): #if r is closed to white, then turn it to black
                r=0 #turn it to black
                g=0
                b=0
            else:
                r=255 #turn it to white
                g=255
                b=255
            img.putpixel((x,y), (r,g,b))
    img.save("WhiteBlack.jpg")
    #img.show

#crop the whiteBlack.jpg
def crop(img, imgsize, islib):
    isExisting = False
    isUpper = False
    whitearray = []
    for x in xrange(max(imgsize)):
        for y in xrange(min(imgsize)):
            r,g,b= img.getpixel((x,y))
            if(255==r):
                isExisting = True
                break
        if(isExisting):
            leftx = x
            break

    if (isExisting):
        for x in xrange(leftx, max(imgsize)):
            for y in xrange(min(imgsize)):
                r,g,b= img.getpixel((x,y))
                whitearray.append(r)    
            if(255 not in whitearray):
                break
            else:
                whitearray = []
        rightx = x-1
            
    else:
        print("No any characters")

    for y in xrange(min(imgsize)):
        for x in xrange(leftx, rightx):
            r,g,b= img.getpixel((x,y))
            if(255 == r):
                isUpper = True
                break
        if(isUpper):
            uppery = y
            break
                
    whitearray =[]
    for y in xrange(uppery, min(imgsize)):
        for x in xrange(leftx,rightx):
            r,g,b= img.getpixel((x,y))
            whitearray.append(r)
        if(255 not in whitearray):
            break
        else:
            whitearray = []
    lowery = y-1

    box =(leftx, uppery, rightx, lowery)         
    region = img.crop(box)
    if(islib):
        region.save("cropsample.jpg")
    else:
        region.save("cropcode.jpg")

def pixels(imgtarget):
    array = []
    target = Image.open(imgtarget)
    for x in xrange(max(target.size)):
        for y in xrange(min(target.size)):
            r,g,b= target.getpixel((x,y))
            array.append(r)
    print(array)
    return array

def dvalue(array01, array02):
    d = 0
    for i in xrange (len(array01)):
        d += (abs(array01[i] - array02[i]))
    avr = d/len(array01)
    return avr     

def lib(imglibname):
    imglib = Image.open(imglibname)
    imglibsize = imglib.size
    crop(imglib, imglibsize, True)
    cropsample = Image.open("cropsample.jpg")
    outsample= cropsample.resize((25,25))
    outsample.save("outsample.jpg")
    arraycode = pixels("outcode.jpg")
    arraysample = pixels("outsample.jpg")
    d = dvalue(arraycode, arraysample)
    return d
      
if __name__ == '__main__':    
    imgcode = Image.open("A.jpg")
    imgcodesize = imgcode.size
    convert(imgcode,imgcodesize)
    imgwb = Image.open("WhiteBlack.jpg")
    crop(imgwb, imgcodesize, False)
    cropcode = Image.open("cropcode.jpg")
    outcode = cropcode.resize((25,25))
    outcode.save("outcode.jpg")
    mword = lib("Mlib.jpg")
    aword = lib("Alib.jpg")
    print("!!!!!!")
    print(aword)
    print(mword)
    if(mword != aword):
        if (mword > aword):
            print("this is A character!!")
        else:
            print("this is M character!!")
    else:
        print("Impossible.....")
        
        
    
    
