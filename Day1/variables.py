# Python không có lệnh khai báo biến.

# Một biến được tạo vào thời điểm bạn gán giá trị cho nó lần đầu tiên
x = 5
y = "John"
print(x)
print(y)

#Các biến không cần phải khai báo bằng bất kỳ loại cụ thể nào và thậm chí có thể thay đổi loại sau khi chúng được đặt
a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)

# truyền kiểu dữ liệu cho biến
b = str(3)    # x will be '3'
c = int(3)    # y will be 3
d = float(3)  # z will be 3.0
print('truyền kiểu dữ liệu', b, c, d)

# check type
e = 5
f = "John"
print(type(e))
print(type(f))
print('có thể dùng nháy đơn,', "hoặc nháy kép")

x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)

x2 = y2 = z2 = "Orange"
print(x2)
print(y2)
print(z2)

fruits = ["apple", "banana", "cherry"]
x3, y3, z3 = fruits
print(x3)
print(y3)
print(z3)