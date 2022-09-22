'''
Lưu trữ danh sách các hình chữ nhật từ file input.db
Lưu danh sách các hình chữ nhật xuống file output.db theo định dạng
    rong-dai-chuvi-dientich

Lưu ý: Trong các file mỗi hàng là thông tin một hình chữ nhật

'''
import Rectangle as rect

# Tải dữ liệu từ file vào listRectangle
fr = open('./codehcn_sv/input.db', mode='r', encoding='utf-8')
listRectangle = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    cr = float(ds[0])
    cd = float(ds[1])
    hcn = rect.Rectangle(cr, cd)
    listRectangle.append(hcn)
fr.close()

# Ghi dữ liệu từ listRectangle xuống file
fw = open('./codehcn_sv/output.db', mode='w', encoding='utf-8')
for item in listRectangle:
    fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
fw.close()
