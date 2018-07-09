import pymssql


def int_exec(s_server, s_port, s_user, s_password, s_database, s_str_sql):
    conn = pymssql.connect(server=s_server, user=s_user, password=s_password
                           , database=s_database, charset='UTF-8', port=s_port, autocommit=False)
    cursor = conn.cursor()
    cursor.execute(s_str_sql)
    rows = cursor.fetchall()
    conn.close()

    return len(rows)


