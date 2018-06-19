with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)