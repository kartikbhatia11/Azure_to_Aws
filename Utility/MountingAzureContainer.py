# Databricks notebook source
# MAGIC %md
# MAGIC ##Creating connection to Azure Storage Account using SAS Key

# COMMAND ----------

containerName = dbutils.widgets.get("containerName")
storageAccountName = dbutils.widgets.get("storageAccountName")
sas = dbutils.secrets.get(scope="AzureCredentials", key="sas")
config = "fs.azure.sas." + containerName+ "." + storageAccountName + ".blob.core.windows.net"
configs = {config: sas}

# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting Azure container to Databricks DBFS

# COMMAND ----------

azureMntLocName = dbutils.widgets.get("azureMntLocName")
azureMntLoc = f"/mnt/{azureMntLocName}"
dbutils.fs.mount(
  source = f"wasbs://{containerName}@{storageAccountName}.blob.core.windows.net/",
  mount_point = azureMntLoc,
  extra_configs = configs)

azureMntLoc
