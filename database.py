from connection import con, cur




def make_tables():
    sql = " SELECT COUNT(*) FROM CUSTOMERS"
    cur.execute(sql)
    result = cur.fetchall()
    if result[0][0] !=0:
        return
    sql = """CREATE TABLE CUSTOMERS(
                    CUSTOMER_ID INT NOT NULL AUTO_INCREMENT,
                    FIRST_NAME VARCHAR(10) NOT NULL,
                    LAST_NAME VARCHAR(10) NOT NULL,
                    STATUS VARCHAR(10),
                    PASSWORD VARCHAR(10)
                    PRIMARY KEY (CUSTOMER_ID));"""
    cur.execute(sql)

    sql = """"CREATE TABLE ADDRESS(
                    CUSTOMER_ID INT NOT NUL AUTO_INCREMENT,
                    LINE VARCHAR(30),
                    CITY VARCHAR(30),
                    COUNTRY VARCHAR(30),
                    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID));"""
    cur.execute(sql)

    sql = """"CREATE TABLE ACCOUNTS(
                    CUSTOMER_ID INT NOT NULL AUTO_INCREMENT,
                    ACCOUNT_NO INT NOT NULL AUTO_INCREMENT,
                    OPENED_ON TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ACCOUNT_TYPE VARCAHR(10),
                    STATUS VARCHAR(20),
                    BALANCE INT,
                    FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID).
                    PRIMARY KEY (ACCOUNT_NO));"""
    cur.execute(sql)

    sql = """"CREATE TABLE TRANSACTIONS(
                    TRANSACTION_ID INT NOT NULL AUTO_INCREMENT,
                    ACCOUNT_NO INT,
                    AMMOUNT INT,
                    BALANCE INT,
                    FOREIGN KEY(ACCOUNT_NO) REFERENCES ACCOUNTS(ACCOUNT_NO));"""
    cur.execute(sql)
    con.commit()













                  
