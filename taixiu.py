import random

# Hàm để rút thăm quà tặng
def rut_tham_qua_tang():
    menh_gia = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 150000, 250000, 350000, 450000, 400000]
    return random.choice(menh_gia)  # Chọn ngẫu nhiên một mệnh giá từ danh sách

# Hàm để hiển thị số tiền trong các bao lì xì còn lại
def hien_thi_so_tien_con_lai(bao_li_xi_da_rut, menh_gia_bao_li_xi):
    print("Số tiền trong các bao lì xì còn lại:")
    for bao_li_xi, menh_gia in menh_gia_bao_li_xi.items():
        if bao_li_xi != bao_li_xi_da_rut:
            print(f"Bao lì xì {bao_li_xi}: {menh_gia} đồng")
import sys
import time

def print_line_by_line(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # Thời gian chờ trước khi hiển thị ký tự tiếp theo
        if char == '':
            input("")

print_line_by_line("Hello em bé thúiiii của tớ\nĐây là chương trình dành cho em bé\nChào mừng em bé đến với chương trình lì xì Tết\n")




def main():
    # Dictionary chứa mệnh giá của các bao lì xì
    menh_gia_bao_li_xi = {}

    # Khởi tạo mệnh giá ngẫu nhiên cho mỗi bao lì xì
    for i in range(1, 6):
        menh_gia_bao_li_xi[i] = rut_tham_qua_tang()

    # Biến để kiểm tra người chơi có muốn tham gia chương trình không
    tiep_tuc = True

    # Hỏi người dùng có muốn tham gia chương trình không
    while True:
        tra_loi = input("Em bé có muốn tham gia chương trình bốc thăm lì xì không? : ")
        if tra_loi.lower() == "có":
            print("Chúc em bé may mắn")
            break
        elif tra_loi.lower() == "không":
            print("Em bé không tham gia là không có lì xì đâu đó")
            break  # Dừng lại nếu người chơi không muốn tham gia
        else:
            print("Em 'có' hoặc 'không' thui, hong được nhập cái khác")

   # Bắt đầu quá trình rút thăm quà tặng
    print_line_by_line("Bé có 5 bao lì xì để chọn. Bé hãy chọn một bao lì xì từ 1 đến 5:\n")
    while True:
        chon_bao_li_xi = input("Em bé muốn chọn bao số mấy ạ: ")
        if chon_bao_li_xi.isdigit():
            bao_li_xi = int(chon_bao_li_xi)
            if 1 <= bao_li_xi <= 5:
                print ("Đố bé biết bé rút được bao nhiu")
                print(f"Bé rút bao lì xì số {bao_li_xi} và nhận được {menh_gia_bao_li_xi[bao_li_xi]} đồng")
                hien_thi_so_tien_con_lai(bao_li_xi, menh_gia_bao_li_xi)  # Hiển thị số tiền trong các bao lì xì còn lại
                break
            else:
                print("Bé chỉ được nhập số từ 1 đến 5 thuii")
        else:
            print("Nào, bé nhập một số nguyên từ 1 đến 5 thui nghe chưa")

    print_line_by_line("Chương trình kết thúc rui\nCảm ơn em bé đã tham gia chương trình của tớ\nChúc em bé cùng gia đình một năm mới vui vẻ và hạnh phúc, gặp được nhiều điều may trong năm 2024 ")

if __name__ == "__main__":
    main()
