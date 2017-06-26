h = int(raw_input("Height? "))
i = 1
while i <= 1:
    i = i + 1
    row = ""
    w = (h * 2) - 1
    j = 1
    while j <= h:
        print (" " * (h - j) + "*" * (j * 2 - 1) + " " * (h -j))
        j = j + 1