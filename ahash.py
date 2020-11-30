from PIL import Image
import imagehash
import time
start_time = time.time()

a = imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a.png"))
b = imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_pic_resized_BW.png"))
c = imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_vertflip.png"))
print(a)
print(b)
print(c)
print("Difference in average_hash for same photo",a - a)
print("Difference in average_hash for print attack",a - b)
print("Difference in average_hash for vertical flip attack",a - c)

# average_hash_list = []
# average_hash_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20.png")))
# average_hash_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a.png")))
# average_hash_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20b.png")))
# average_hash_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20c.png")))
# average_hash_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20d.png")))
# average_hash_attack_list = []
# average_hash_attack_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_pic_resized_BW.png")))
# average_hash_attack_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_horiflip_vertflip.png")))
# average_hash_attack_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_horiflip.png")))
# average_hash_attack_list.append(imagehash.average_hash(Image.open(r"C:\Users\johnsonvu\Desktop\IrisRecognition\png folder\osoba20\osoba20a_vertflip.png")))
#
# for x in range(len(average_hash_list)):
#     print("Starting new row")
#     for y in range(len(average_hash_list)):
#         print("Difference in average_hash for column ",average_hash_list[x] - average_hash_list[y])
#
# print("\nStarting attacks, print, horivert, hori, vert")
# for x in range(len(average_hash_list)):
#     print("Starting new row")
#     for y in range(len(average_hash_attack_list)):
#         print("Difference in average_hash for column ",average_hash_list[x] - average_hash_attack_list[y])

print("Time taken: ", (time.time() - start_time), "seconds")