from typing import Tuple

from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession


def init_spark_session() -> Tuple[SparkSession, SparkContext]:
    """
    Function responsible for starting the SparkSession.

    Returns:
        Tuple[SparkSession, SparkContext]: Spark session and context
    """
    spark_conf = SparkConf().setAll(
        [
            ("spark.driver.memory", "8g"),
            ("spark.driver.maxResultSize", "8g"),
            ("spark.sql.caseSensitive", "true"),
            ("spark.sql.shuffle.partitions", "200"),
            ("spark.default.parallelism", "800"),
            ("spark.sql.execution.arrow.enabled", "true"),
            ("spark.sql.parquet.compression.codec", "snappy"),
            ("spark.memory.fraction", "0.7"),
            ("spark.memory.storageFraction", "0.5"),
            ("spark.shuffle.memoryFraction", "0.2"),
            ("spark.executor.memoryOverhead", "2g"),
            ("spark.driver.memoryOverhead", "2g"),
            ("spark.sql.parquet.summary.metadata.level", "ALL"),
            ("spark.sql.parquet.datetimeRebaseModeInWrite", "CORRECTED"),
            (
                "spark.sql.sources.partitionOverwriteMode",
                "dynamic",
            ),
        ]
    )
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    sc = spark.sparkContext

    spark.sparkContext.setLogLevel("ERROR")

    return spark, sc
