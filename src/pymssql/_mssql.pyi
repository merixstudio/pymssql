"""
This type stub file was generated by pyright.
"""

import datetime
import re
from collections.abc import Callable, Sequence
from typing import Any

class datetime2(datetime.datetime): ...

__full_version__: str
__version__: str
VERSION: tuple[int, ...]

class NoParams: ...

ROW_FORMAT_TUPLE: int
ROW_FORMAT_DICT: int
STRING: int
BINARY: int
NUMBER: int
DATETIME: int
DECIMAL: int
SQLBINARY: int
SQLBIT: int
SQLBITN: int
SQLCHAR: int
SQLDATETIME: int
SQLDATETIM4: int
SQLDATETIMN: int
SQLDECIMAL: int
SQLFLT4: int
SQLFLT8: int
SQLFLTN: int
SQLIMAGE: int
SQLINT1: int
SQLINT2: int
SQLINT4: int
SQLINT8: int
SQLINTN: int
SQLMONEY: int
SQLMONEY4: int
SQLMONEYN: int
SQLNUMERIC: int
SQLREAL: int
SQLTEXT: int
SQLVARBINARY: int
SQLVARCHAR: int
SQLUUID: int
SQLDATE: int
SQLTIME: int
SQLDATETIME2: int

def py2db_type(py_type: type, value: Any) -> int: ...

class MSSQLException(Exception):
    """
    Base exception class for the MSSQL driver.
    """


class MSSQLDriverException(MSSQLException):
    """
    Inherits from the base class and raised when an error is caused within
    the driver itself.
    """


class MSSQLDatabaseException(MSSQLException):
    """
    Raised when an error occurs within the database.
    """

    message: str

login_timeout: int
min_error_severity: int
wait_callback: None

def set_wait_callback(a_callable: Callable) -> None: ...

class MSSQLRowIterator:
    def __init__(self, connection: MSSQLConnection, row_format: int) -> None: ...
    def __iter__(self) -> MSSQLRowIterator: ...
    def __next__(self) -> tuple[Any, ...]: ...

class MSSQLConnection:
    charset: str
    connected: bool
    identity: tuple[Any, ...]
    query_timeout: int
    rows_affected: int
    tds_version: int
    tds_version_tuple: tuple[int, int] | None
    def __init__(
        self,
        server: str = ".",
        user: str | None = None,
        password: str | None = None,
        charset: str = "UTF-8",
        database: str = "",
        appname: str | None = None,
        port: str = "1433",
        tds_version: str | None = None,
        encryption: str | None = None,
        read_only: bool = False,
        conn_properties: str | list[str] | None = None,
    ) -> None: ...
    def __dealloc__(self) -> None: ...
    def __enter__(self) -> MSSQLConnection: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __iter__(self) -> MSSQLRowIterator: ...
    def set_msghandler(self, handler: Callable) -> None:
        """
        set_msghandler(handler) -- set the msghandler for the connection

        This function allows setting a msghandler for the connection to
        allow a client to gain access to the messages returned from the
        server.
        """
        ...

    def cancel(self) -> None:
        """
        cancel() -- cancel all pending results.

        This function cancels all pending results from the last SQL operation.
        It can be called more than once in a row. No exception is raised in
        this case.
        """
        ...

    def close(self) -> None:
        """
        close() -- close connection to an MS SQL Server.

        This function tries to close the connection.  It can be called more than once in a row. No exception is raised
        in this case.
        """
        ...

    def mark_disconnected(self) -> None: ...
    def execute_non_query(self, query_string: str, params: object = ...) -> None:
        """
        execute_non_query(query_string, params=NoParams)

        This method sends a query to the MS SQL Server to which this object
        instance is connected. After completion, its results (if any) are
        discarded. An exception is raised on failure. If there are any pending
        results or rows prior to executing this command, they are silently
        discarded. This method accepts Python formatting. Please see
        execute_query() for more details.

        This method is useful for INSERT, UPDATE, DELETE and for Data
        Definition Language commands, i.e. when you need to alter your database
        schema.

        After calling this method, rows_affected property contains number of
        rows affected by the last SQL command.
        """
        ...

    def execute_query(self, query_string: str, params: object = ...) -> None:
        """
        execute_query(query_string, params=NoParams)

        This method sends a query to the MS SQL Server to which this object
        instance is connected. An exception is raised on failure. If there
        are pending results or rows prior to executing this command, they
        are silently discarded. After calling this method you may iterate
        over the connection object to get rows returned by the query.

        You can use Python formatting here and all values get properly
        quoted:
            conn.execute_query('SELECT * FROM empl WHERE id=%d', 13)
            conn.execute_query('SELECT * FROM empl WHERE id IN %s', ((5,6),))
            conn.execute_query('SELECT * FROM empl WHERE name=%s', 'John Doe')
            conn.execute_query('SELECT * FROM empl WHERE name LIKE %s', 'J%')
            conn.execute_query('SELECT * FROM empl WHERE name=%(name)s AND \
                city=%(city)s', { 'name': 'John Doe', 'city': 'Nowhere' } )
            conn.execute_query('SELECT * FROM cust WHERE salesrep=%s \
                AND id IN (%s)', ('John Doe', (1,2,3)))
            conn.execute_query('SELECT * FROM empl WHERE id IN %s',\
                (tuple(xrange(4)),))
            conn.execute_query('SELECT * FROM empl WHERE id IN %s',\
                (tuple([3,5,7,11]),))

        This method is intended to be used on queries that return results,
        i.e. SELECT. After calling this method AND reading all rows from,
        result rows_affected property contains number of rows returned by
        last command (this is how MS SQL returns it).
        """
        ...

    def execute_row(self, query_string: str, params: object = ...) -> tuple[Any, ...]:
        """
        execute_row(query_string, params=NoParams)

        This method sends a query to the MS SQL Server to which this object
        instance is connected, then returns first row of data from result.

        An exception is raised on failure. If there are pending results or
        rows prior to executing this command, they are silently discarded.

        This method accepts Python formatting. Please see execute_query()
        for details.

        This method is useful if you want just a single row and don't want
        or don't need to iterate, as in:

        conn.execute_row('SELECT * FROM employees WHERE id=%d', 13)

        This method works exactly the same as 'iter(conn).next()'. Remaining
        rows, if any, can still be iterated after calling this method.
        """
        ...

    def execute_scalar(
        self, query_string: str, params: object = ...
    ) -> tuple[Any, ...] | None:
        """
        execute_scalar(query_string, params=NoParams)

        This method sends a query to the MS SQL Server to which this object
        instance is connected, then returns first column of first row from
        result. An exception is raised on failure. If there are pending

        results or rows prior to executing this command, they are silently
        discarded.

        This method accepts Python formatting. Please see execute_query()
        for details.

        This method is useful if you want just a single value, as in:
            conn.execute_scalar('SELECT COUNT(*) FROM employees')

        This method works in the same way as 'iter(conn).next()[0]'.
        Remaining rows, if any, can still be iterated after calling this
        method.
        """
        ...

    def fetch_next_row(self, throw: int, row_format: int) -> tuple[Any, ...] | None: ...
    def format_and_run_query(self, query_string: str, params: object = ...) -> None:
        """
        This is a helper function, which does most of the work needed by any
        execute_*() function. It returns NULL on error, None on success.
        """
        ...

    def executemany(
        self, query_string: str, seq_of_parameters: Sequence[str], batch_size: int
    ) -> None: ...
    def get_header(self) -> tuple[str, ...] | None:
        """
        get_header() -- get the Python DB-API compliant header information.

        This method is infrastructure and doesn't need to be called by your
        code. It returns a list of 7-element tuples describing the current
        result header. Only name and DB-API compliant type is filled, rest
        of the data is None, as permitted by the specs.
        """
        ...

    def get_iterator(self, row_format: int) -> MSSQLRowIterator:
        """
        get_iterator(row_format) -- allows the format of the iterator to be specified

        While the iter(conn) call will always return a dictionary, this
        meth
        """
        ...

    def init_procedure(self, procname: str) -> MSSQLStoredProcedure:
        """
        init_procedure(procname) -- creates and returns a MSSQLStoredProcedure
        object.

        This methods initializes a stored procedure or function on the server
        and creates a MSSQLStoredProcedure object that allows parameters to
        be bound.
        """
        ...

    def nextresult(self) -> int | None:
        """
        nextresult() -- move to the next result, skipping all pending rows.

        This method fetches and discards any rows remaining from the current
        resultset, then it advances to the next (if any) resultset. Returns
        True if the next resultset is available, otherwise None.
        """
        ...

    def select_db(self, dbname: str) -> None:
        """
        select_db(dbname) -- Select the current database.

        This function selects the given database. An exception is raised on
        failure.
        """
        ...

    def bcp_sendrow(self, element: list[str], column_ids: list[int]): ...

class MSSQLStoredProcedure:
    connection: MSSQLConnection
    name: str
    parameters: list[str]
    def __init__(self, name: bytes, connection: MSSQLConnection) -> None: ...
    def __dealloc__(self) -> None: ...
    def bind(
        self,
        value: Any,
        dbtype: int,
        param_name: str | None = None,
        output: int | bool = False,
        null: int | bool = False,
        max_length: int = -1,
    ) -> None:
        """
        bind(value, data_type, param_name = None, output = False,
            null = False, max_length = -1) -- bind a parameter

        This method binds a parameter to the stored procedure.
        """
        ...

    def execute(self) -> None: ...

def remove_locale(value: bytes) -> str: ...

_re_pos_param: re.Pattern[bytes]
_re_name_param: re.Pattern[bytes]

def quote_simple_value(value: Any | None) -> str | bytes | None: ...
def quote_or_flatten(data: list[Any] | tuple[Any, ...]) -> str | bytes | None: ...
def quote_data(
    data: list[Any] | tuple[Any, ...] | dict[Any, Any],
) -> str | bytes | set[Any] | tuple[Any, ...] | None: ...
def substitute_params(toformat: str, params: object = ..., charset: str = "utf-8"): ...
def connect(*args, **kwargs) -> MSSQLConnection: ...

MssqlDatabaseException = MSSQLDatabaseException
MssqlDriverException = MSSQLDriverException
MssqlConnection = MSSQLConnection

def test_err_handler(
    connection: MSSQLConnection,
    severity: int,
    dberr: int,
    oserr: int,
    dberrstr: str,
    oserrstr: str,
) -> tuple[int, str, int, int, int]:
    """
    Expose err_handler function and its side effects to facilitate testing.
    """
    ...

def get_max_connections() -> int:
    """
    Get maximum simultaneous connections db-lib will open to the server.
    """
    ...

def set_max_connections(limit: int) -> None:
    """
    Set maximum simultaneous connections db-lib will open to the server.

    :param limit: the connection limit
    :type limit: int
    """
    ...

def get_dbversion() -> str:
    """
    Return string representing the version of db-lib.
    """
    ...