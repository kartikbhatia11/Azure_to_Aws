# Databricks notebook source
# MAGIC %md
# MAGIC ##Mounting Azure Blob Storage Container to Databricks DBFS

# COMMAND ----------



# COMMAND ----------


# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting AWS S3 Bucket to Databricks DBFS

# COMMAND ----------


# COMMAND ----------

# MAGIC %md
# MAGIC ##Reading Data from Azure Container

# COMMAND ----------

medications_df = spark.read.format("csv").option("header",True).option("inferSchema",True).load(azureMntLoc+"/medications.csv")
display(medications_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Writing Data to AWS S3 Bucket

# COMMAND ----------

medications_df.write.format("csv").save(awsMntLoc+"/medication_data1")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Unmounting Azure Blob Storage Container

# COMMAND ----------

dbutils.fs.unmount(azureMntLoc)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Unmounting AWS S3 Bucket

# COMMAND ----------

dbutils.fs.unmount(awsMntLoc)
