print("===== MÁY TÍNH TOÁN VÀ HÌNH HỌC =====")
print("[1] Tính dtích/chu vi hình học\n[2] Phân tích tam giác\n[3] Phương trình bậc 2\n")

while True:
    try:
        choice = int(input("Chọn chức năng (Nhập số theo mục được cho sẵn):"))
        if choice > 0 and choice < 4:
            break
    except ValueError:
        print("\nKhông hợp lệ!\n")
        continue
def solve_quadratic(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2
    elif delta == 0:
        x1 = x2 = (-b) / (2*a)
        return x1, "kép"
    if delta < 0:
        return "Phương trình vô nghiệm", "toilet"

def triangle_analyser(a, b, c):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        answer = "Tam giác vuông"
    elif a == b == c:
        answer = "Tam giác đều"
    elif a == b or a == c or b == c:
        answer = "Tam giác cân"
    else:
        answer = "Tam giác thường"
    return answer

if choice == 1:
    while True:
        try:
            choice1 = int(input("\nChọn hình bạn muốn tính diện tích/chu vi:\n[1]Hình tam giác\n[2]Hình chữ nhật\n[3]Hình vuông\nChọn:"))
            if choice1 > 0 and choice1 < 4:
                break
        except ValueError:
            print("\nKhông hợp lệ!\n")
            continue
    if choice1 == 1:
        
        while True:
            try:
                a = float(input("Nhập cạnh a của tam giác:"))
                if a > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue

        while True:
            try:
                b = float(input("Nhập cạnh b của tam giác:"))
                if b > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue

        while True:
            try:
                c = float(input("Nhập cạnh c của tam giác:"))
                if c > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
        area = (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5
        perimeter = a + b + c
        print(f"Diện tích của tam giác là: {area}\nChu vi của tam giác là: {perimeter}")
    elif choice1 == 2:

        while True:
            try:
                a = float(input("Nhập chiều rộng của hình chữ nhật:"))
                if a > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
        while True:
            try:
                b = float(input("Nhập chiều dài của hình chữ nhật:"))
                if b > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
        area = a*b
        perimeter = 2*(a+b)
        print(f"Diện tích của hình chữ nhật là: {area}\nChu vi của hình chữ nhật là: {perimeter}")
    elif choice1 == 3:

        while True:
            try:
                a = float(input("Nhập cạnh của hình vuông:"))
                if a > 0:
                    break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
        area = a*a
        perimeter = a*4
        print(f"Diện tích của hình vuông là: {area}\nChu vi của hình vuông là: {perimeter}")
elif choice == 2:
    while True:
        try:
            a = float(input("Nhập cạnh a của tam giác:"))
            if a > 0:
                break
        except ValueError:
            print("\nKhông hợp lệ!\n")
            continue
    while True:
        try:
            b = float(input("Nhập cạnh b của tam giác:"))
            if b > 0:
                break
        except ValueError:
            print("\nKhông hợp lệ!\n")
            continue
    while True:
        try:
            c = float(input("Nhập cạnh c của tam giác:"))
            if c > 0:
                break
        except ValueError:
            print("\nKhông hợp lệ!\n")
            continue

    if a + b > c and a + c > b and b + c > a:
        print("Thỏa mảng bất đẳng thức tam giác!")
        print(f"Phân loại: {triangle_analyser(a,b,c)}\nChu vi: {a+b+c}\nDiện tích: {(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5}")
        print(f"Bán kính đường tròn nội tiếp tam giác: {((((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5)/(a+b+c)/2}")
        print(f"Bán kính đường tròn ngoại tiếp tam giác: {(a*b*c)/4*((((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5)}")
    else:
        print("Không phải là tam giác\n==> Không thể tiếp tục phân tích tam giác")
elif choice == 3:
    while True:
            try:
                a = float(input("Nhập a:"))
                break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
    while True:
            try:
                b = float(input("Nhập b:"))
                break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
    while True:
            try:
                c = float(input("Nhập c:"))
                break
            except ValueError:
                print("\nKhông hợp lệ!\n")
                continue
    x1,x2 = solve_quadratic(a,b,c)
    if x2 == "toilet":
        print("Phương trình vô nghiệm!")
    elif x2 == "kép":
        print(f"Phương trình có hai nghiệm kép là {x1}")
    else:
        print(f"Phương trình có hai nghiệm phân biệt là {x1} và {x2}")
