from tinydb import TinyDB, Query

db = TinyDB("/tmp/lala/db.json")

a = {"FileLogName" : "error/log15.log", "LastWritten": 114333, "Size": 408}
b = {"FileLogName" : "error/log14.log", "LastWritten": 117333, "Size": 401}
c = {"FileLogName" : "error/log11.log", "LastWritten": 111333, "Size": 403}
d = {"FileLogName" : "error/log10.log", "LastWritten": 115333, "Size": 404}

#db.insert(a)
#db.insert(b)

e = [c, d]
#db.insert_multiple(e)
print(db.all())

Log = Query()

result = db.search(Log.FileLogName == "error/log11.log")
print("Result: {0}".format(result))

result = db.search(Log.FileLogName == "a")
print("Result: {0}".format(result))

db.update({"LastWritten": 150009}, Log.FileLogName == "error/log10.log")

result = db.search(Log.FileLogName == "error/log10.log")
print("Result: {0}".format(result))
