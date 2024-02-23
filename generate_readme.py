from glob import glob

images = glob('scripts/**/*.png') + glob('scripts/**/*.jpeg') + glob('scripts/**/*.mp4') 

md_images = []
for path in images:
    md_images.append('![img](./' + path + ')')

with open("readme.md", "a") as myfile:
    myfile.write("## Scripts gallery\n\n")
    for x in md_images:
        myfile.write(x + "\n")