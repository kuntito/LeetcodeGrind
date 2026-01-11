# https://leetcode.com/problems/design-sql/description/

# use a hashmap to represent tables
# the key is the table name
# the value is a doubly linked list node

# the dll would contain a list representing each row
# it would contain a hashmap for columnnames and row idx
# this way row items can be selected in O(1)
# and rows can be removed in O(1)

# but how do you identify each row in O(1)?

# i think it's best to create a class
class Table:
    def __init__(self, name, colCount):
        pass
        self.name = name
        self.columnCount = colCount
        self.rowId = 1
        
        
        # each table needs O(1) access to it's rows
        # hence, hashmap
        self.allRows = {}
        
        # use a dll to track the order of the rows
        # that way, if a row is removed, you update the dll
        # and remove that row from `self.rows`
        # technically, self.rows should point to two things
        # the row object and the row node
        # ideally, they shouldn't be separate
        # in that case the row itself should be a linked list node
        
        # so we'd need two pointers `top` and `bottom` which are dummy rows
        # each new row is added before `bottom`
        
        self.top = Row(rowId="top", colData=colCount)
        self.bottom = Row(rowId="bottom", colData=colCount)
        
        self.top.nex, self.bottom.prev = self.bottom, self.top
        
    def __str__(self):
        curr = self.top.nex
        
        arr = []
        while curr != self.bottom:
            arr.append(str(curr))
            curr = curr.nex
            
        return "\n".join(arr) if arr else "[]"
    
    def __repr__(self):
        return str(self)
        
    def insertRow(self, rowData):
        if len(rowData) != self.columnCount:
            return False
        
        rowId = self.getCurrRowId()
        row = Row(rowId, rowData)

        # add the row to the hashmap
        self.allRows[rowId] = row
        
        # place the row before bottom
        currLast = self.bottom.prev
        
        currLast.nex = row
        row.prev = currLast
        
        # now the row has become the last row
        row.nex = self.bottom
        self.bottom.prev = row
        
        return True
        
    def getCurrRowId(self):
        rowId = self.rowId
        self.rowId += 1
        return rowId
    
    def deleteRow(self, rowId):
        if rowId not in self.allRows:
            return
        
        row = self.allRows[rowId]
        del self.allRows[rowId]
        
        # connect neighbours
        before, after = row.prev, row.nex
        
        before.nex = after
        after.prev = before
        
        row.nex = None
        row.prev = None
        
        return True
    
            
    def selectValue(self, rowId, columnId):
        if rowId not in self.allRows:
            return None
        
        row = self.allRows[rowId]
        return row.colData[columnId-1]
                
    
    def selectAll(self):
        currRow = self.top.nex
        
        while currRow != self.bottom:
            pass
            rowId = currRow.rowId
            items = [f"{rowId}", *currRow.colsData]
            print(items)
            
            
    
class Row:
    def __init__(self, rowId, colData, prev=None, nex=None):
        self.rowId = rowId
        self.colData = colData
        self.prev=prev
        self.nex=nex
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.colData)
        
class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.allTables = {}
        
        for nm, colCount in zip(names, columns):
            self.allTables[nm] = Table(
                name=nm,
                colCount=colCount
            )
        
    def ins(self, name: str, row: list[str]) -> bool:
        if name not in self.allTables:
            return False
        
        table = self.allTables[name]
        return table.insertRow(row)

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.allTables:
            return False
        
        table = self.allTables[name]
        table.deleteRow(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.allTables:
            return "<null>"
        
        table = self.allTables[name]
        res = table.selectValue(rowId, columnId)
        
        return "<null>" if res is None else res

    def exp(self, name: str) -> list[str]:
        if name not in self.allTables:
            return []
        
        table = self.allTables[name]
        table.selectAll()


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)

names = ["one","two","three"]
columns = [2, 3, 1]
sol = SQL(names, columns)
sol.ins("two",["first","second","third"])
# sol.sel("two",1,3)
# sol.ins("two",["fourth","fifth","sixth"])
# sol.exp("two")

# # sh
# sol.rmv("two",1)
# sol.sel("two",2,2)
# sol.exp("two")

# [],[],["two"]]

# tab = Table("a", 5)

# print(tab)