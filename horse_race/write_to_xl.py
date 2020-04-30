import xlwt
import xlrd
from xlutils.copy import copy


class RecordResults:
    def __init__(self, date=None, name=None, time=None, iswinner=None):

        self.date = date
        self.name = name
        self.time = time
        if iswinner == True:
            self.iswinner = "WINNER"
        else:
            self.iswinner = "LOSER"


        def read_book():
            try:
                book = xlrd.open_workbook("races_book.xls")
            except FileNotFoundError:
                book = xlwt.Workbook()
                sheet = book.add_sheet("All_races")
                book.save("races_book.xls")
                book = xlrd.open_workbook("races_book.xls")

            return book

        book_to_read = read_book()

        def get_empty_row(book):
            sheet = book.sheet_by_index(0)
            return sheet.nrows

        row_write_number = get_empty_row(book_to_read)

        book_to_write = copy(book_to_read)

        sheet_to_write = book_to_write.get_sheet(0)

        try:
            for i in range(4):
                if i == 0:
                    sheet_to_write.write(row_write_number, i, self.date)
                if i == 1:
                    sheet_to_write.write(row_write_number, i, self.name)
                if i == 2:
                    sheet_to_write.write(row_write_number, i, self.time)
                if i == 3:
                    sheet_to_write.write(row_write_number, i, self.iswinner)

            book_to_write.save('races_book.xls')
            print("Input recorded successfully")
        except:
            print("Something went wrong. Record was not saved.")




