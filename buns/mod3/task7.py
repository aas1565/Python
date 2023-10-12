a=str(input())

def res (seq):
    return len(set(seq)) != len(seq)

print(res(a))