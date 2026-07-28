from sqlalchemy.testing import fixtures
from sqlalchemy.testing import mock
from sqlalchemy.testing import provision


class TruncateTableTest(fixtures.TestBase):
    def test_default_uses_unconditional_delete(self):
        connection = mock.Mock()
        table = mock.Mock()
        statement = table.delete.return_value

        provision.truncate_table("sqlite://", connection, table)

        table.delete.assert_called_once_with()
        connection.execute.assert_called_once_with(statement)
