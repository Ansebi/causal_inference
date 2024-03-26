# Databricks notebook source
from data_ops import load_spark_df

# COMMAND ----------

spark_df = load_spark_df(spark)

# COMMAND ----------

spark_df.show()

# COMMAND ----------

spark_df.count()

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

spark_df_filtered = spark_df.filter((col("CUST_GEO_FDRL_DSTRCT_NM") == "Центральный") & (col("PROD_CTGY_VW_DSC") == "ENERGY") & (col("PROD_MKU_DSC") == "ADRENALINE RUSH CAN 0.449 ENERGY"))

# COMMAND ----------

spark_df_filtered.show()

# COMMAND ----------

spark_df_filtered.count()

# COMMAND ----------

df_filtered = spark_df_filtered.toPandas()

# COMMAND ----------

display(df_filtered)
