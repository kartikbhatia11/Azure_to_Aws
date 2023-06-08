# Databricks notebook source
# MAGIC %md
# MAGIC ##Unmounting Azure Blob Storage Container

# COMMAND ----------

azureMntLoc = dbutils.widgets.get("azureMntLoc")
dbutils.fs.unmount(f"/mnt/{azureMntLoc}")
