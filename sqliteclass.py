import sqlite3
import logging as LOGGER

class sqlite3class:
    def __init__(self):
        self.conn = sqlite3.connect("pythonsqlite.db")
        print(sqlite3.version)

        self.cursor = self.conn.cursor()
        self.cursor.row_factory = lambda cursor, row: row[0]

    def query_gif(self, inurl):
        # inurl: url
        # returns url ID
        print('query_gif', inurl)
        self.cursor.execute("SELECT * FROM object_table WHERE object_name=? ", [inurl])
        result = self.cursor.fetchone()
        if result:
            result_id = result
            return result_id
        else:
            return None

    def query_tag(self, intag):
        query_tag = intag
        self.cursor.execute("SELECT * FROM tag_table WHERE tag_name=? ", [query_tag])
        result = self.cursor.fetchone()
        if result:
            result_tag = result
            result_tag_id = result_tag

            return result_tag_id
        else:
            return None

    def create_tag(self, intag):
        query_tag = intag
        self.cursor.execute("INSERT INTO tag_table (tag_name) VALUES (?)", [intag])
        self.conn.commit()
        result_tag_id = self.cursor.lastrowid
        return result_tag_id

    def map_tag_to_gif(self, tagid, gifid):
        try:
            self.cursor.execute(
                "INSERT INTO object_tag_mapping VALUES (?,?)", (gifid, tagid)
            )
            self.conn.commit()
        except Exception as e:
            pass

    def fetch_gif(self, intag):
        self.cursor.execute(
            "SELECT object_name from object_tag_mapping JOIN object_table ON object_reference = object_table.id JOIN tag_table ON tag_reference = tag_table.id WHERE tag_name = ?",
            [intag],
        )
        result = self.cursor.fetchall()
        return result

    def insert(self, inurl):
        self.cursor.execute(
            "INSERT INTO object_table (object_name) VALUES (?)", [inurl]
        )
        self.conn.commit()
        result_tag_id = self.cursor.lastrowid
        return result_tag_id

    def tag(self, inurl, intag):
        print('tag')
        urlid = self.query_gif(inurl)
        print("tag urlid",urlid)
        if not urlid:
            urlid = self.insert(inurl)
        tagid = self.query_tag(intag)
        print("tag tagid",tagid)
        if not tagid:
            tagid = self.create_tag(intag)
        self.map_tag_to_gif(tagid, urlid)

    def untag(self, inurl, intag):
        urlid = self.query_gif(inurl)
        tagid = self.query_tag(intag)
        if (urlid and tagid):
            self.cursor.execute("DELETE FROM object_tag_mapping  WHERE object_reference = ? AND tag_reference = ?", (urlid, tagid))
            self.conn.commit()
            
        test_tag_has_url = self.fetch_gif(intag)
        
        if not test_tag_has_url:
            self.cursor.execute("DELETE FROM tag_table WHERE tag_name = ?", (intag,))
            self.conn.commit()
        


if __name__ == "__main__":
    db = sqlite3class()
    query_in = input("enter search term: ")
    url_in = input("enter url: ")
    db.untag("https://media.giphy.com/media/xuFza8ogutelGYr00k/giphy.gif","woi")

    result_tag_id = db.fetch_gif(query_in)
    LOGGER.error("result_tag_id", result_tag_id)
    if result_tag_id:
        res = db.fetch_gif(query_in)
        print(res)
    else:
        print("no result")
