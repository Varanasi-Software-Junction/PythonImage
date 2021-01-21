def makeBW(pic):
#Convert Image to Grayscale
    mx, my, mz = pic.shape

    for x in range(mx):
        for y in range(my):
            b = int(pic[x][y][0])
            g = int(pic[x][y][1])
            r = int(pic[x][y][2])
            bwvalue = int((r + g + b) // 3)

            pic[x][y][0] = bwvalue
            pic[x][y][1] = bwvalue
            pic[x][y][2] = bwvalue

    return pic
def fullBW(pic):
# Convert Image to pure black and white
    pic=makeBW(pic)
    mx, my, mz = pic.shape
    for x in range(mx):
        for y in range(my):
            value = int(pic[x][y][0])
            value = 0 if value<127 else 255

            pic[x][y][0] = value
            pic[x][y][1] = value
            pic[x][y][2] = value

    return pic

