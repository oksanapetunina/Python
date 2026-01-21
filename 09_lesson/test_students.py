from sqlalchemy import create_engine, select, text, MetaData, Table
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"

db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)
session = Session()


def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'users'


def test_select():
    rows = session.execute(text("select * from users")).all()
    row1 = rows[0]
    row2 = rows[1]
    assert row1[0] == 42568
    assert row1[1] == "igorpetrov@mail.ru"
    assert row2[0] == 85426
    assert row2[1] == "sasha555@gmail.com"


def test_select2():
    db = create_engine(db_connection_string)
    metadata = MetaData()
    your_table = Table('users', metadata, autoload_with=db)
    stmt = select(your_table)
    with db.connect() as connection:
        results = connection.execute(stmt)
    rows = results.mappings().all()
    assert rows[0]["user_id"] == 42568
    assert rows[0]["user_email"] == "igorpetrov@mail.ru"
    assert rows[1]["user_id"] == 85426
    assert rows[1]["user_email"] == "sasha555@gmail.com"


def test_select_1_param():
    user_id = 42568
    query = f"""
    SELECT * FROM users WHERE user_id = {user_id}"""
    result = session.execute(text(query)).all()
    assert len(result) == 1


def test_select_2_param():
    my_params = {
        'user_id': 42568,
        'subject_id': 1
    }
    query = """
    SELECT * FROM users
    WHERE user_id = :user_id AND subject_id = :subject_id
    """
    result = session.execute(text(query), my_params).all()
    assert len(result) == 1


def test_insert():
    new_email = "Revolver2@mail.ru"
    sql = f"""
    insert into users (user_email) values ('{new_email}')"""
    session.execute(text(sql))
    session.commit()
    query = f"""
    SELECT * FROM users WHERE user_email = '{new_email}'"""
    result = session.execute(text(query)).all()
    assert result[0][1] == new_email
    delete_query = f"""
    DELETE FROM users WHERE user_email = '{new_email}'"""
    session.execute(text(delete_query))
    session.commit()
    session.close()


def test_update():
    new_email = "Revolver12@mail.ru"
    user_id = 125
    sql = f"""
    UPDATE users SET user_email = '{new_email}' WHERE user_id = {user_id}"""
    session.execute(text(sql))
    session.commit()
    query = f"""
    SELECT user_email FROM users WHERE user_id = {user_id}"""
    result = session.execute(text(query)).scalar()
    assert result == new_email


def test_delete():
    new_email = 'sasha555@gmail.com'
    delete_query = f"""
    DELETE FROM users WHERE user_email = '{new_email}'"""
    session.execute(text(delete_query))
    session.commit()
    session.close()
    query = f"""
    SELECT * FROM users WHERE user_email = '{new_email}'"""
    result = session.execute(text(query)).all()
    assert result == []
    