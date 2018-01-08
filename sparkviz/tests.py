"""
Unit tests for improved Spark Viz.
"""

from sparktestingbase.sqltestcase import SQLTestCase
import sparkviz

class TestSparkViz(SQLTestCase):
  schema = ['id', 'name', 'pandas', 'favourite_number', 'call sign']
  data = [(12, "holden", 2, 3.6, "kk6jkq"), (13, "hello kitty", 2, 3.0, None),
          (None, "bad record", None, None, None)]

  @classmethod
  def setupClass(cls):
    from IPython.core.interactiveshell import InteractiveShell
    cls.display_formatter = InteractiveShell.instance().display_formatter
    super(TestSparkViz, cls).setUpClass()

  def test_basic_display(self):
    """Tests that a basic display runs and doesn't throw any exceptions"""
    df = self.sqlCtx.createDataFrame(self.data, self.schema)
    df_show_obj = df.show()
    df_show_obj._do_display()
    # TODO: Figure out how to capture the display result and verify it
    # Maybe its easier once the widget exists?
