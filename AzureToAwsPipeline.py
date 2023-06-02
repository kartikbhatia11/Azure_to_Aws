# Databricks notebook source
# MAGIC %md
# MAGIC ##Mounting Azure Blob Storage Container to Databricks DBFS

# COMMAND ----------



# COMMAND ----------

# MAGIC %run ./Utility/AzureStorageConfigurations $containerName="testcontainer" $storageAccountName="azureconnteststorage" $sas="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-06-29T18:59:16Z&st=2023-05-31T10:59:16Z&spr=https&sig=%2BGNv6awUheLDhKBE%2FyTX%2FQzn3OAbsWgyPipitBWMar8%3D" $azureMntLocName="AzureDemoContainer"

# COMMAND ----------

# MAGIC %md
# MAGIC ##Mounting AWS S3 Bucket to Databricks DBFS

# COMMAND ----------

# MAGIC %run ./Utility/AwsStorageConfigurations $access_key="AKIAQ6RW7SP5OGDC7MRY" $secret_key="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" $aws_bucket_name="kartikdemobucket" $mount_name="AWSDemoBucket"

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

medications_df.write.format("csv").save(awsMntLoc+"/medication_data")

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