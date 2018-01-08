#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
