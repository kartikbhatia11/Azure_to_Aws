# Databricks notebook source
# MAGIC %md
# MAGIC ##Unmounting AWS S3 Bucket

# COMMAND ----------

awsMntLoc = ""
dbutils.fs.unmount(f"/mnt/{awsMntLoc}")
