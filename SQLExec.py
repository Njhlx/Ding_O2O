import pymssql


def int_exec(s_server: object, s_port: object, s_user: object, s_password: object, s_database: object, s_str_sql: object) -> object:
    conn = pymssql.connect(server=s_server, user=s_user, password=s_password
                           , database=s_database, charset='UTF-8', port=s_port, autocommit=False)
    cursor = conn.cursor()
    cursor.execute(s_str_sql)
    rows = cursor.fetchone()

    conn.close()

    return rows

    #返回条数
    # return len(rows)


