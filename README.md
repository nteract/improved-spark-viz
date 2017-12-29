# improved-spark-viz 🐼

**WIP - This is not suitable for production use.**

Improved visualizations in Spark.

## Installation (Development)

Supports [PySpark] >= 2.2.0.

1. Clone this repo.

2. Use [`pip`] to install:

```
pip install -e .
```

## Contributing

We follow the contributing guidelines of the [nteract] project.

## References

### [pandas] documentation

- pandas DataFrame
    - [`pandas.DataFrame`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame) [\[source\]](https://github.com/pandas-dev/pandas/blob/v0.21.1/pandas/core/frame.py#L236-L6142)
    - [`pandas.DataFrame.sample`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html#pandas-dataframe-sample) [\[source\]](https://github.com/pandas-dev/pandas/blob/v0.21.1/pandas/core/generic.py#L3286-L3442)

### [PySpark] API documentation

- pyspark DataFrame
    - [`pyspark.sql.DataFrame`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame)
    - [`pyspark.sql.DataFrame.sample`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame.sample)
    - [`pyspark.sql.DataFrame.sampleBy`](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame.sampleBy)

- [pyspark.RDD](http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=storagelevel#pyspark.RDD) A Resilient Distributed Dataset (RDD), the basic abstraction in Spark)

- [pyspark.StorageLevel](http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=storagelevel#pyspark.StorageLevel)
  controls storage of an RDD

[PySpark]: http://spark.apache.org/docs/latest/api/python/
[`pip`]: https://pip.pypa.io/en/stable/
[nteract]: https://nteract.io
[pandas]: http://pandas.pydata.org/pandas-docs/stable/