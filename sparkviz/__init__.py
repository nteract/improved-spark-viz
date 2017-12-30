#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pyspark.sql as sd
from pyspark.storagelevel import StorageLevel
import pandas as pd

def special_show(self, n=2000, truncate=False, vertical=False, auto_sample=True, seed=None):
    """Special version for a Spark dataframe's `show`

    This changes the defaults to number of rows to show to 2000 and samples
    the result.

    Caches the input if not already cached.

    Parameters
    ----------
    - self: a dataframe
    - n (int): number of rows from dataframe to show (default 2000)
    - truncate (bool): whether to truncate rows (default False)
    - vertical (bool): support fancy notebook mode (default False)
    - auto_sample (bool): whether to sample the dataframe (default True)
    - seed (int): seed for sampling (default None)

    """
    if vertical:
        raise Exception("this doesn't work in fancy notebook mode")

    do_cache = auto_sample and self.storageLevel == StorageLevel(False, False, False, False, 1)
    try:
        if do_cache:
            df.cache()

        sampled_df = self
        if auto_sample:
            total_count = self.count()
            do_sample = (n < total_count) and auto_sample
            if do_sample:
                fraction = (n * 1.1) / total_count
                sampled_df = self.sample(withReplacement=False, fraction=fraction).limit(n)
            pandas_df = sampled_df.toPandas()

        return DataFrameResult(pandas_df, self, do_sample)

    finally:
        if do_cache:
            df.unpersist()


class DataFrameResult:
    """A special fake class for DataFrame results.

    Wraps a pandas df & a spark df.

    """
    def __init__(self, pdf, sdf, sampled):
        self.pdf = pdf
        self.sdf = sdf
        self.sampled = sampled
        from IPython.display import display

        # TODO(do something where we have more control besides pandas directly)
        with pd.option_context('display.html.table_schema', True):
          self.display = display(pdf, metadata={"application/json": { "sampled": sampled} }, display_id=True)


sd.DataFrame.show = special_show
