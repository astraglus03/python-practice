# a:b:c:d -> a#b#c#d로 바꾸기

a="a:b:c:d"
b=a.split(":")
print("#".join(b))

