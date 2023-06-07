# Databricks notebook source
# MAGIC %md
# MAGIC ##Unmounting Azure Blob Storage Container

# COMMAND ----------

azureMntLoc = ""
dbutils.fs.unmount(f"/mnt/{azureMntLoc}")
