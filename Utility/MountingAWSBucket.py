# Databricks notebook source
# MAGIC %md
# MAGIC ##Creating connection to AWS Account using Access Key

# COMMAND ----------

access_key = ""
secret_key = ""
encoded_secret_key = secret_key.replace("/","%2F")


# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting AWS S3 Bucket to Databricks DBFS

# COMMAND ----------

aws_bucket_name = ""
mount_name = ""
awsMntLoc = f"/mnt/{mount_name}"

dbutils.fs.mount(f"s3a://{access_key}:{encoded_secret_key}@{aws_bucket_name}", awsMntLoc)
awsMntLoc
