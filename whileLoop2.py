large = 1
smaller = 0

while large < 100:
    print (large)

    temp = large
    large = temp+smaller
    smaller = temp

    if large == 34:
        print("found 34")
        break
