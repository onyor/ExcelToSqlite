import os
import pandas as pd
from sqlalchemy import create_engine

# pip install pandas sqlalchemy
# pip install xlrd
# pip install openpyxl

# Veritabanı bağlantısını oluşturma
engine = create_engine('sqlite:///eSinav.db')

# eSinav klasörünün yolu
folder_path = 'eSinav'

# eSinav klasöründeki tüm Excel dosyaları için
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xls') or file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        table_name = file_name.replace('.xls', '').replace('.xlsx', '')
        
        # Excel dosyasını oku
        df = pd.read_excel(file_path)
        
        # Veritabanına yaz
        df.to_sql(table_name, con=engine, index=False, if_exists='replace')

print("Tüm Excel dosyaları veritabanına başarıyla aktarıldı.")
