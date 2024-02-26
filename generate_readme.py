from glob import glob

images = glob('scripts/**/*.png') + glob('scripts/**/*.jpeg')

md_images = []
for path in images:
    md_images.append('![img](./' + path + ')')
    
with open("readme.md", "r") as f:
    readme_lines = []
    for line in f:
        readme_lines.append(line)
        if line == "## Scripts gallery\n":
            break

with open("readme.md", "w") as myfile:
    for y in readme_lines:
        myfile.write(y)

    myfile.write("\n")
    
    for x in md_images:
        myfile.write(x + "\n")