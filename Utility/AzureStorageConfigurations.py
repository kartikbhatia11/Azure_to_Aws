# Databricks notebook source
# MAGIC %md
# MAGIC ##Refreshes Mount to Latest version

# COMMAND ----------

dbutils.fs.refreshMounts()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Creating connection to Azure Storage Account using SAS Key

# COMMAND ----------

containerName = dbutils.widgets.get("containerName")
storageAccountName = dbutils.widgets.get("storageAccountName")
sas = dbutils.widgets.get("sas")
config = "fs.azure.sas." + containerName+ "." + storageAccountName + ".blob.core.windows.net"
configs = {config: sas}

# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting Azure container to Databricks DBFS

# COMMAND ----------

azureMntLoc = f"/mnt/{dbutils.widgets.get('azureMntLocName')}"
dbutils.fs.mount(
  source = f"wasbs://{containerName}@{storageAccountName}.blob.core.windows.net/",
  mount_point = azureMntLoc,
  extra_configs = configs)

azureMntLoc