from pdf2image import convert_from_path

file_name = f"failure_cases"

# 設定PDF檔案路徑
pdf_path = f'./{file_name}.pdf'

# 將PDF頁面轉換為圖片
images = convert_from_path(pdf_path, dpi=300)

# 保存圖片
image = images[0]
image.save(f'./{file_name}.png', 'PNG')

