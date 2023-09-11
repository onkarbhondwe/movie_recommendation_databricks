# Databricks notebook source
adlsAccountName = "fmmovierecstorage"
adlsContainerName = "validated"
adlsFolderName = "Data"
mountPoint = "/mnt/Files/Validated"
sas_key = dbutils.secrets.get(scope="movie_recomendation-scope", key="sas-token")

configs={
"fs.azure.sas." + adlsContainerName+ "." + adlsAccountName + ".blob.core.windows.net": sas_key
         }

source="wasbs://"+adlsContainerName+"@"+adlsAccountName+".blob.core.windows.net/"+adlsFolderName

if not any (mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
    print(dbutils.fs.mount(
        source=source,
        mount_point=mountPoint,
        extra_configs=configs))
    


# COMMAND ----------

## Undeploy mountPoint
# mountPoint = "/mnt/Files/Validated"
# dbutils.fs.unmount(mountPoint)

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/mnt/Files/Validated/

# COMMAND ----------


