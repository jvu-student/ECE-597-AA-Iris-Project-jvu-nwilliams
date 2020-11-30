import cv2
import numpy as np
import time
start_time = time.time()


def is_flip(original, target):
    # temp = cv2.flip() # flip 0 vertical, 1 horizontal, -1 both
    print("\nChecking if images are equal : ", np.array_equal(original,target))
    if np.array_equal(original, target) == False:
        print("Images were not equal \n Will now check if it was vertically flipped")
        temp = cv2.flip(target, 0)
        if np.array_equal(original, temp) == False:
            print("Images were not equal \n Will now check if it was horizontally flipped")
            temp2 = cv2.flip(target, 1)
            if np.array_equal(original, temp2) == False:
                print("Images were not equal \n Will now check if it was horizontally and vertically flipped")
                temp3 = cv2.flip(target, -1)
                if np.array_equal(original, temp3) == False:
                    print("Images are not equal, they must be different images")
                else:
                    print("Images are equal, it was horizontally and vertically flipped")
            else:
                print("Images are equal, it was horizontally flipped")
        else:
            print("Images are equal, it was vertically flipped")
    else:
        print("Images are equal")
    return 0

image = cv2.imread(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a.png") # r fix
image2 = cv2.imread(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_pic_resized_BW.png")
image3 =  cv2.imread(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_vertflip.png")

is_flip(image,image) # same photo inserted
is_flip(image,image2) # print attack
is_flip(image,image3) # vertical attack

print("Time taken: ", (time.time() - start_time), "seconds")

