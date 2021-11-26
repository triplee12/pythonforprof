import os


__author__ = "Ejie Emmanuel Ebuka"

# Simple app, dir stats
# Simple application that can scans a directory recursively

stats = dict(path='', folders=0, files=0, links=0, size=0)
# Get user input
def get_input():
    global stats
    ret = os.path.abspath(input("Enter a folder to scan: "))
    if not os.path.exists(ret):
        print(f"Oops! ({ret}) does not exist")
        exit(1)
    if not os.path.isdir(ret):
        print(f"Oops! ({ret}) is not a directory")
        exit(2)
    stats['path'] = ret

# Scan the path recursively
def scan(path):
    global stats
    print(f"Scanning... {path}")
    for root, dirs, files in os.walk(path, onerror=None, followlinks=False):
        stats['folders'] += len(dirs)
        stats['files'] += len(dirs)
        for name in files:
            fullname = os.path .join(root, name)
            size = os.path.getsize(fullname)
            stats['size'] += size
        for dir in dirs:
            print(f'{dir}')

# Display
def display():
    global stats
    print("Results: ")
    for k, v in stats.items():
        print(f'{k} = {v}')

# Main
def main():
    global stats
    get_input()
    scan(stats['path'])
    display()

if __name__ == "__main__":
    main()

# If you want me to add more features to this app, use the comment section in github and tell me feature(s) you want there.
