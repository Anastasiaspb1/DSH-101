SYMBOL_SIZE = 4
line_size = 25 * SYMBOL_SIZE
page_size = 50 * line_size
book_size = 100 * page_size

disk_size_mb = 1.44
disk_size_kb = disk_size_mb * 1024
disk_size_b = disk_size_kb * 1024

books_in_disk = int(disk_size_b // book_size)  # TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_in_disk)
