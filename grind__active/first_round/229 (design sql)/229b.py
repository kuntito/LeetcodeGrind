# https://leetcode.com/problems/design-sql/description/

class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {}
        
        for nm, colCount in zip(names, columns):
            self.tables[nm] = Table(nm, colCount)

    def ins(self, name: str, row: list[str]) -> bool:
        if name not in self.tables:
            return False
        
        table = self.tables[name]
        return table.insertRow(row)

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return None
        
        table = self.tables[name]

        table.removeRow(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        
        table = self.tables[name]
        res = table.selectValue(rowId, columnId)
        return "<null>" if res is None else res


    def exp(self, name: str) -> list[str]:
        if name not in self.tables:
            return []
        
        table = self.tables[name]
        return table.selectAll()        
    
# we'd use OOP
# a class for tables
# each table would have properties
# name
# columnCount
# table_rows

# for O(1) removal of table rows
# make each row a doubly linked list
# structure table with two pointers
# `top` and `bottom`
# every new row should be placed before `bottom`

class Table:
    def __init__(self, name, colCount):
        pass
        self.name = name
        self.colCount = colCount
        
        self.rowId = 1
        self.cache = {}
        self.top, self.bottom = self.getTopBottomPointers()
        
    def getTopBottomPointers(self):
        top = Row("top", "top")
        bottom = Row("bottom", "bottom")

        top.nex = bottom
        bottom.prev = top

        return top, bottom

    def getRowId(self):
        res = self.rowId
        
        self.rowId += 1
        
        return res

    def insertRow(self, row: list[str]):
        if len(row) != self.colCount:
            return False
        
        rowId = self.getRowId()
        
        ## create the row
        row = Row(
            rowId=rowId,
            rowData=row
        )
        
        ## insert into the cache
        self.cache[rowId] = row
        
        ## insert into doubly linked list
        # you want to place each row before the last
        bottom = self.bottom
        
        currLast = bottom.prev

        currLast.nex = row
        row.prev = currLast
        
        row.nex = bottom
        bottom.prev = row
        
        return True
        
        

    def removeRow(self, rowId):
        if rowId not in self.cache:
            return None
        
        row = self.cache[rowId]
        self.connectNeighbours(row)
        
        del self.cache[row.rowId]
        
    def connectNeighbours(self, node):
        before, after = node.prev, node.nex
        
        before.nex = after
        after.prev = before
        
        node.nex = None
        node.prev = None
    
    def selectValue(self, rowId: int, columnId: int):
        if rowId not in self.cache:
            return None
        
        row = self.cache[rowId]
        value = row.getValue(columnId)
        
        return value
    
    def selectAll(self):
        curr = self.top.nex
        
        arr = []
        while curr != self.bottom:
            pass
            rowId = curr.rowId
            rowIdString = f"{rowId}"
            item = [rowIdString]
            
            item.extend(curr.rowData)
            
            csv = ",".join(item)
            arr.append(csv)
            
            
            curr = curr.nex
    
        # print(arr)
        return arr
    
    def __str__(self):
        curr = self.top.nex
        
        arr = []
        while curr != self.bottom:
            arr.append(str(curr))
            curr = curr.nex
            
        return f'*************{self.name}***************\n' + "\n".join(arr) + '\n'
    
    def __repr__(self):
        return str(self)


class Row:
    def __init__(self, rowId, rowData, nex=None, prev=None):
        self.rowId = rowId
        self.rowData = rowData
        self.nex = nex
        self.prev = prev
        
    def getValue(self, columnId):
        # this addresses pythons negative indexing
        if columnId > len(self.rowData) or columnId < 1:
            return None
        
        idx = columnId - 1
        return self.rowData[idx]
    
    def __str__(self):
        return f"{self.rowData}"
    
    def __repr__(self):
        return str(self)
        
        
# tab = Table("cats", 3)

# row = ["panther", "lion", "jaguar"]
# tab.insertRow(row)
# row = ["cheetah", "leopard", "lynxx"]
# tab.insertRow(row)
# print(tab)

# tab.removeRow(1)
# print(tab)

# res = tab.selectValue(1, 3)
# print(res)

# res = tab.selectAll()
# print(res)

names = ["one","two","three"]
columns = [2, 3, 1]
sol = SQL(names, columns)
sol.ins("two",["first","second","third"])
sol.sel("two",1,3)
sol.ins("two",["fourth","fifth","sixth"])
res = sol.exp("two")
# print(res)

sol.rmv("two",1)
sol.sel("two",2,2)
res = sol.exp("two")
print(res)