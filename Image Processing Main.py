import cv2 as pp
import ImageFilters as flt
pic = pp.imread("K:\\Blogspot\\pics\\program output\\latest.png")
print()
if pic is None:
    print("Picture not found")
else:
    print(type(pic))

    pic=flt.fullBW(pic)
    output=pp.imshow("Show Picture", pic)
    print(output)
    pp.imwrite("K:\\Blogspot\\pics\\program output\\bw.png",pic)
    output=pp.waitKey(0)
