from django.db import models


# Create your models here.
class WTTX_SERVICE_LOGS(models.Model):
    DESCRIPTION = models.CharField(max_length=1000)
    total = models.IntegerField()
    # ID = models.IntegerField()
    # REQUESTDATETIME = models.DateTimeField()
    # APPNAME = models.CharField(max_length=1000)
    # LDAPUSER = models.CharField(max_length=1000)
    # DWELLINGUNITNUM = models.CharField(max_length=1000)
    # TOKENKEY = models.CharField(max_length=1000)
    # TRANSACTIONID = models.CharField(max_length=1000)
    # LON = models.IntegerField()
    # LAT = models.IntegerField()
    # SERVICETYPE = models.IntegerField()
    # SERVICEID = models.IntegerField()
    # OLDSERVICEID = models.IntegerField()
    # RESULTCODE = models.IntegerField()
    # SPEED = models.CharField(max_length=1000)
    # TASKSTATUS = models.IntegerField()
    # CINFO = models.CharField(max_length=1000)
    # SENSIVITY = models.IntegerField()
    # CLEARADDRESS = models.CharField(max_length=1000)
    # BMSADDRESS = models.CharField(max_length=1000)
    # GRID_RESULT = models.CharField(max_length=1000)
    # KAPASITIF_RESULT = models.CharField(max_length=1000)

    class Meta:
        db_table = "WTTX_SERVICE_LOGS"
