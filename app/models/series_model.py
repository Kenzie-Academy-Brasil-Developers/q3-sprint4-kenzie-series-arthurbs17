from app.services.database_service import DatabaseConnector

class Series(DatabaseConnector):
    def __init__(self, *args, **kwargs) -> None:
        self.serie = kwargs["serie"].title()
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"].title()
        self.imdb_rating = kwargs["imdb_rating"]

    def to_add_serie(self):
        self.get_conn_cur()

        query = """
            INSERT INTO
                ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *;
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        added_serie = self.cur.fetchone()

        self.commit_and_close()
        
        return added_serie

    @classmethod
    def read_all_series(cls):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series"

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        cls.commit_and_close()

        return series
    
    @classmethod
    def read_specific_serie(cls, id: int):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series WHERE id= %s"

        cls.cur.execute(query, str(id))
        specific_serie = cls.cur.fetchone()
        
        cls.commit_and_close()
        return specific_serie