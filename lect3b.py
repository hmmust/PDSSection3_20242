def get_names(n):
    for i in range(1,n+1):
        yield "Ahmad"*i
for v in get_names(5):
    print(v)