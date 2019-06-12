import psycopg2


class MemberInterface():
    def __init__(self):
        self._conn = psycopg2.connect(
            "dbname=hs-management_members user=hs-management")
        self._create_tables()
        self.get_user_by_card_id(id)

    def _create_tables(self):
        cursor = self._cursor
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS members(
            id serial,
            first_name text,
            surname text,
            username text,
            card_id text UNIQUE,
            paxton_id text UNIQUE,
            PRIMARY KEY(id)
        )
        """)
        cursor.close()

    @property
    def _cursor(self):
        return self._conn.cursor()

    def new_user(self, card_id):
        """ """

    def get_user_by_card_id(self, card_id):
        """ Lookups user by card ID """
        cursor = self._cursor
        cursor.execute("SELECT * FROM members", (card_id,))

        results = cursor.fetchall()
        print(results)
