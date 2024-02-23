import glob

images = glob.glob('scripts/**/*.png')

md_images = []
for path in images:
    md_images.append('![img](./' + path + ')')

with open("readme.md", "a") as myfile:
    myfile.write("## Scripts gallery\n\n")
    for x in md_images:
        myfile.write(x + "\n")