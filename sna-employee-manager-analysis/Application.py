from reader.CsvReader import CsvReader


class Application:

    reader = CsvReader()
    nodeList = reader.readEmployee()
    tesekkurList = reader.readRelationship('tesekkur')
    takdirList = reader.readRelationship('takdir')
    dogumgunuList = reader.readRelationship('dogumgunu')
    print("blabla")