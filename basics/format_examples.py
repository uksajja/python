def format_comma(num):
    return(f"{num:,}")

x = float(input("X:"))
y = float(input("Y:"))
z = round(x/y, 5)
val = x/y
print("z:", z)
print("val:", val)
print(f"val: {val:0.5f}")

x = 100000
y = 20000000000000
sum = x+y
print(f"x: {x:,} y: {y:,} Sum: {sum:,}")

str = format_comma(350005.46)
print(str)