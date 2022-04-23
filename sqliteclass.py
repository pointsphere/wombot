import sqlite3


class sqlite3class:
    def __init__(self):
        self.conn = sqlite3.connect("pythonsqlite.db")
        print(sqlite3.version)

        self.cursor = self.conn.cursor()

    def query_gif(self, inurl):
        # inurl: url
        # returns url ID
        self.cursor.execute("SELECT * FROM object_table WHERE object_name=? ", [inurl])
        result = self.cursor.fetchone()
        if result:
            result_id = result[0]
            return result_id
        else:
            return None

    def query_tag(self, intag):
        query_tag = intag
        self.cursor.execute("SELECT * FROM tag_table WHERE tag_name=? ", [query_tag])
        result = self.cursor.fetchone()
        if result:
            print("we have a result")
            print(result)
            print(result[0])
            print(result[1])
            result_tag = result
            result_tag_id = result_tag[0]

            return result_tag_id
        else:
            return None

    def create_tag(self, intag):
        query_tag = intag
        self.cursor.execute("INSERT INTO tag_table (tag_name) VALUES (?)", [intag])
        self.conn.commit()
        result_tag_id = self.cursor.lastrowid
        # cursor_obj.execute("SELECT * FROM tag_table WHERE tag_name=? ", [intag])
        # result = cursor.fetchone()
        # print(result)
        # result_tag = result
        # result_tag_id = result_tag[0]

        return result_tag_id

    def map_tag_to_gif(self, tagid, gifid):
        try:
            self.cursor.execute(
                "INSERT INTO object_tag_mapping VALUES (?,?)", (gifid, tagid)
            )
            self.conn.commit()
        except Exception as e:
            # print(e)
            pass

    def fetch_gif(self, intag):
        self.cursor.row_factory = lambda cursor, row: row[0]
        self.cursor.execute(
            "SELECT object_name from object_tag_mapping JOIN object_table ON object_reference = object_table.id JOIN tag_table ON tag_reference = tag_table.id WHERE tag_name = ?",
            [intag],
        )
        result = self.cursor.fetchall()
        # print("hopefully a result")
        return result

    def insert(self, inurl):
        self.cursor.execute(
            "INSERT INTO object_table (object_name) VALUES (?)", [inurl]
        )
        result_tag_id = self.cursor.lastrowid
        return result_tag_id

    def tag(self, inurl, intag):
        urlid = self.query_gif(inurl)
        if not urlid:
            urlid = self.insert(inurl)
        tagid = self.query_tag(intag)
        if not tagid:
            tagid = self.create_tag(intag)
        self.map_tag_to_gif(tagid, urlid)


if __name__ == "__main__":
    db = sqlite3class()
    query_in = input("enter search term: ")
    print("searching for", query_in)

    result_tag_id = db.query_tag(query_in)
    print("result_tag_id", result_tag_id)
    if result_tag_id:
        res = db.fetch_gif(query_in)
        print(res)
    else:
        print("no result")
