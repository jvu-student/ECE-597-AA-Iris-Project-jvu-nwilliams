from PIL import Image
import imagehash
import time
start_time = time.time()

a = imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a.png"))
b = imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_pic_resized_BW.png"))
c = imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_vertflip.png"))
print(a)
print(b)
print(c)
print("Difference in phash for same photo",a - a)
print("Difference in phash for print attack",a - b)
print("Difference in phash for vertical flip attack",a - c)

# phash_list = []
# phash_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20.png")))
# phash_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a.png")))
# phash_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20b.png")))
# phash_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20c.png")))
# phash_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20d.png")))
# phash_attack_list = []
# phash_attack_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_pic_resized_BW.png")))
# phash_attack_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_horiflip_vertflip.png")))
# phash_attack_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_horiflip.png")))
# phash_attack_list.append(imagehash.phash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_vertflip.png")))
# for x in range(len(phash_list)):
#     print("Starting new row")
#     for y in range(len(phash_list)):
#         print("Difference in phash for column ",phash_list[x] - phash_list[y])
#
# print("\nStarting attacks, print, horivert, hori, vert")
# for x in range(len(phash_list)):
#     print("Starting new row")
#     for y in range(len(phash_attack_list)):
#         print("Difference in phash for column ",phash_list[x] - phash_attack_list[y])

print("Time taken: ", (time.time() - start_time), "seconds")