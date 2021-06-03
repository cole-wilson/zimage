from PIL import Image

tweet = Image.open('tweet.jpg')
orig = Image.open('unsplash.jpg').resize((1200,900))
orig.save('unsplash_sized.jpg')
a = Image.new("RGB", (1200, 900), color=0)

adata = []

tdata = tweet.getdata()
odata = orig.getdata()

print('Tweet # of colors:', len(set(tdata)))
print('Original # of colors:', len(set(odata)))

input()

for c, i in enumerate(tdata):
	if c % 1000 == 0:
		print(c, len(odata))
	if i != odata[c]:
		amount = sum([abs(i[x] - odata[c][x]) for x in range(len(i))])
		adata.append((amount * 10, 0, 0))
	else:
		adata.append((0, 0, 0))

a.putdata(adata)
a.save('out.jpg')