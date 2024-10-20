# TODO Найдите количество книг, которое можно разместить на дискете
symbols_in_line = 25
lines_on_page = 50
pages_in_book = 100

total_number_of_symbols = (symbols_in_line * lines_on_page) * pages_in_book

one_book_weights = total_number_of_symbols * 4

kbites_in_disk = 1.44 * 1024 * 1024

answer = int(kbites_in_disk // one_book_weights)

print("Количество книг, помещающихся на дискету:", answer)
