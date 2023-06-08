# Databricks notebook source
# MAGIC %md
# MAGIC ##Refreshes Mount to Latest version

# COMMAND ----------

dbutils.fs.refreshMounts()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Reading Data from Azure Container

# COMMAND ----------

readLoc = dbutils.widgets.get("readLoc")
medications_df = spark.read.format("csv").option("header",True).option("inferSchema",True).load("/mnt/"+readLoc)
display(medications_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Writing Data to AWS S3 Bucket

# COMMAND ----------

# MAGIC %md
# MAGIC writeLoc = ""
# MAGIC medications_df.write.format("csv").save("/mnt/"+writeLoc)
