import gdown
import zipfile
import os

def download_and_extract():
    # ID lấy từ link
    file_id = '1NhrOG5QBqKfNoIaxR8NoFC9vIwlprDqR'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'dataset.zip'
    
    # Kiểm tra nếu đã có dữ liệu rồi thì thôi
    if os.path.exists('data/'):
        print("Thư mục 'data/' đã tồn tại. Bỏ qua tải về.")
        return

    # 1. Tải về
    print("Đang tải file nén từ Google Drive...")
    gdown.download(url, output, quiet=False)

    # 2. Giải nén
    print("Đang giải nén vào thư mục 'data/'...")
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall('data/')

    # 3. Xóa file zip
    os.remove(output)
    print("Hoàn tất! Bạn có thể bắt đầu train model.")

if __name__ == "__main__":
    download_and_extract()