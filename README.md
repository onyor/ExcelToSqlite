# ExcelToSqlite

Bu proje, belirli bir klasörde yer alan tüm Excel dosyalarını (`*.xls` ve `*.xlsx`) okuyarak bu verileri bir SQLite veritabanına aktarır. Bu işlem, özellikle büyük miktarda Excel verisini programatik olarak yönetmek ve analiz etmek isteyenler için yararlıdır.

## Özellikler

- Klasördeki tüm Excel dosyalarını otomatik olarak tanır ve işler.
- Verileri kolayca erişilebilir bir SQLite veritabanına aktarır.
- `.xls` ve `.xlsx` formatlarını destekler.

## Gereksinimler

Projenin düzgün çalışabilmesi için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:

- `pandas`: Veri işleme ve CSV/Excel dosyalarıyla çalışma işlevselliği sağlar.
- `sqlalchemy`: Python için SQL araç kiti ve Nesne İlişkisel Haritalama (ORM) kütüphanesi.
- `xlrd`: `.xls` dosyalarını okumak için gereklidir.
- `openpyxl`: `.xlsx` dosyalarını okumak için gereklidir.

## Kurulum

Gerekli kütüphaneleri kurmak için aşağıdaki komutları terminalinizde çalıştırabilirsiniz:

```bash
pip install pandas sqlalchemy xlrd openpyxl
