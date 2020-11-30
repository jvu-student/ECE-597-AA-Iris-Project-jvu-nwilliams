import dhash
from PIL import Image
import time
start_time = time.time()

image = Image.open('osoba20a.png') # Original
row, col = dhash.dhash_row_col(image)
a = "0x" + dhash.format_hex(row, col)

image2 = Image.open('osaba20a_pic_resized_BW.png')  # Print Attack
row, col = dhash.dhash_row_col(image2)
b = "0x" + dhash.format_hex(row, col)

image3 = Image.open('osoba20a_vertflip.png')
row, col = dhash.dhash_row_col(image3)
c = "0x" + dhash.format_hex(row, col)

d = int(a,0)
e = int(b,0)
f = int(c,0)

print("Original")
print(dhash.get_num_bits_different(d,d))
print("Print Attack:")
print(dhash.get_num_bits_different(d,e))
print("Vertical Flip")
print(dhash.get_num_bits_different(d,f))
print("Time taken: ", (time.time() - start_time), "seconds")



# Used for Data Collection:
#valuelist = [0xc08701468687d7cf40003341dfaf1fff,0xc08700468f8fc74fc08033405fbfbfff,0xc04302264646c767800013215f3f9fff,0xc00f130c8e0f1f9780003f41bf7f7fbf,0xc0870744c68687c7c0001e4140be3fff,0xc087034c8e8cd3c6000033419fbdffff]

#for i in valuelist:
    #print(dhash.get_num_bits_different(0xb2c3812707474767f08093202f3fdf3f,i))