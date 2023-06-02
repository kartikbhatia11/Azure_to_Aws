# Databricks notebook source
# MAGIC %md
# MAGIC ##Refreshes Mount to Latest version

# COMMAND ----------

dbutils.fs.refreshMounts()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Creating connection to AWS Account using Access Key

# COMMAND ----------

access_key = dbutils.widgets.get("access_key")
secret_key = dbutils.widgets.get("secret_key")
encoded_secret_key = secret_key.replace("/","%2F")


# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting AWS S3 Bucket to Databricks DBFS

# COMMAND ----------

aws_bucket_name = dbutils.widgets.get("aws_bucket_name")
awsMntLoc = f"/mnt/{dbutils.widgets.get('mount_name')}"

dbutils.fs.mount(f"s3a://{access_key}:{encoded_secret_key}@{aws_bucket_name}", awsMntLoc)
awsMntLoc