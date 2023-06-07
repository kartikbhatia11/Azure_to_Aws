# Databricks notebook source
# MAGIC %md
# MAGIC ##Refreshes Mount to Latest version

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ##Reading Data from Azure Container

# COMMAND ----------

readLoc = ""
medications_df = spark.read.format("csv").option("header",True).option("inferSchema",True).load("/mnt/"+readLoc)
display(medications_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Writing Data to AWS S3 Bucket

# COMMAND ----------

writeLoc = ""
medications_df.write.format("csv").save("/mnt/"+writeLoc)
