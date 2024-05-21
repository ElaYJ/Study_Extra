import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.title = "Info"

ws.append(["1", "2", "3", "4", "5"])
ws.append(["1", "2", "3", "4", "5"])
ws.append(["1", "2", "3", "4", "5"])
ws.append(["1", "2", "3", "4", "5"])
ws.append(["1", "2", "3", "4", "5"])

ws.merge_cells("A1:D1")

ws.insert_rows(3)
ws.insert_rows(3)
ws.insert_rows(3)

wb.save("info.xlsx")

