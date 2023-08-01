from django.db import models

# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    Vendor = models.CharField(max_length=225, blank=True, null=True)
    BuyerName = models.CharField(max_length=225)
    Address = models.CharField(max_length=225)
    def __str__(self):
        return self.BuyerName

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    Vendor = models.CharField(max_length=225, blank=True, null=True)
    BuyerName = models.CharField(max_length=225)
    StyleCode = models.CharField(max_length=225,unique=True)
    ItemName = models.CharField(max_length=225,blank=True,null=True)
    barcode = models.CharField(max_length=225, blank=True,null=True)
    def __str__(self):
        return self.StyleCode

class ProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    ProductionLine = models.CharField(max_length=255)
    daily_target = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.ProductionLine

class OrderQty(models.Model):
    buyer = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255)
    item = models.CharField(max_length=255, blank=True, null=True)
    order_qty = models.PositiveIntegerField(default=0)
    cmp = models.FloatField()
    cmp_amount = models.FloatField()
    making_charge = models.PositiveIntegerField(default=0)
    import_export_charge = models.PositiveIntegerField(default=0)
    box_charge = models.PositiveIntegerField(default=0)
    poly_bag = models.PositiveIntegerField(default=0)
    sewing_thread = models.PositiveIntegerField(default=0)
    cmp_condition = models.FloatField()
    date = models.DateField()
    serial_number = models.CharField(max_length=255)
    md_charge = models.CharField(max_length=255,blank=True,null=True)
    delivery = models.DateField(blank=True,null=True)
    fabricETA = models.DateField(blank=True,null=True)
    accETA = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.style

class ProductionInput(models.Model):
    line = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    input_qty = models.PositiveIntegerField(default=0)
    daily_target = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line




    
class DailyProductionOuput(models.Model):
    line = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    input_qty = models.PositiveIntegerField(default=0)
    cmp_amount = models.FloatField(default=0.0)
    daily_target = models.PositiveIntegerField(default=0)
    wok_hr = models.PositiveIntegerField(default=10)

    shift_1 = models.PositiveIntegerField(default=0)
    shift_2 = models.PositiveIntegerField(default=0)
    shift_3 = models.PositiveIntegerField(default=0)
    shift_4 = models.PositiveIntegerField(default=0)
    shift_5 = models.PositiveIntegerField(default=0)
    shift_6 = models.PositiveIntegerField(default=0)
    shift_7 = models.PositiveIntegerField(default=0)
    shift_8 = models.PositiveIntegerField(default=0)
    shift_9 = models.PositiveIntegerField(default=0)
    shift_10 = models.PositiveIntegerField(default=0)
    shift_11 = models.PositiveIntegerField(default=0)
    shift_12 = models.PositiveIntegerField(default=0)    
    total_output_qty = models.PositiveIntegerField(default=0)

    menpower = models.PositiveIntegerField(default=1)
    cmp_pr_menpower = models.FloatField(default=0.0)
    acc_total_cmp = models.FloatField(default=0.0)
    
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DailyProductionLineMenPower(models.Model):
    line = models.CharField(max_length=225)
    num_operator = models.PositiveIntegerField(default=0)
    num_helper = models.PositiveIntegerField(default=0)
    
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WareHouse(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.warehouse_name

class FabricInventory(models.Model):
    supplier_name = models.CharField(max_length=200)
    buyer_name = models.CharField(max_length=200)
    po_style_no = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    chall_invoice_no = models.CharField(max_length=200, blank=True, null=True)
    fabric_construction = models.CharField(max_length=200, blank=True, null=True)
    fabric_width = models.CharField(max_length=200, blank=True, null=True)
    fabric_composition = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    receive_qty = models.PositiveIntegerField(default=0)
    warehouse = models.CharField(max_length=200)
    receive_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.po_style_no

class AccInventoy(models.Model):
    supplier_name = models.CharField(max_length=200)
    buyer_name = models.CharField(max_length=200)
    po_style_no = models.CharField(max_length=200)
    receive_qty = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=200, blank=True, null=True)
    sewing_finishing = models.CharField(max_length=200, blank=True, null=True)
    warehouse = models.ForeignKey(WareHouse, on_delete=models.CASCADE, null=True)
    receive_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.po_style_no

class AccImage(models.Model):
    accinv = models.ForeignKey(
        AccInventoy, on_delete=models.CASCADE, null=True
    )
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.accinv.po_style_no


class AccVariant(models.Model):
    accinv = models.ForeignKey(
        AccInventoy, on_delete=models.CASCADE
        )
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    request_qty = models.IntegerField(default=0)
    request_by = models.CharField(max_length=100, blank=True, null=True)
    request_date = models.DateField(blank=True,null=True)
    request_status = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.accinv.po_style_no

class Wh(models.Model):
    test = models.CharField(max_length=100)


class AccessoriesRequestToWh(models.Model):
    style_po_id = models.CharField(max_length=100)
    style_po = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    request_qty = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    request_by = models.CharField(max_length=100, blank=True, null=True)
    request_line = models.CharField(max_length=100, blank=True, null=True)
    accept_by = models.CharField(max_length=100, blank=True, null=True)
    request_status = models.CharField(max_length=100)
    request_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WarehouseToProductionHistory(models.Model):
    style_po_id = models.CharField(max_length=100)
    style_po = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    handover_quantity = models.PositiveIntegerField(default=0)
    request_qty = models.IntegerField(default=0)
    request_by = models.CharField(max_length=100)
    request_line = models.CharField(max_length=100)
    handover_by = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    remark = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FabricInventoy(models.Model):
    supplier_name = models.CharField(max_length=200,blank=True, null=True)
    buyer_name = models.CharField(max_length=200,blank=True, null=True)
    po_style_no = models.CharField(max_length=200,blank=True, null=True)
    receive_qty = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(WareHouse, on_delete=models.CASCADE, null=True)
    receive_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.po_style_no


class FabricImage(models.Model):
    accinv = models.ForeignKey(
        FabricInventoy, on_delete=models.CASCADE, null=True
    )
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.accinv.po_style_no
    

class FabricComposition(models.Model):
    accinv = models.ForeignKey(
        FabricInventoy, on_delete=models.CASCADE, null=True
    )
    fabric_construction = models.CharField(max_length=200, blank=True, null=True)
    fabric_width = models.CharField(max_length=200, blank=True, null=True)
    fabric_composition = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    receive_qty = models.PositiveIntegerField(default=0)
    remark = models.CharField(max_length=200, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fabric_composition

class FabricRequesttoWH(models.Model):
    pass