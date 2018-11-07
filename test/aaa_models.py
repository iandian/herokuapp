# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressCountry(models.Model):
    iso_3166_1_a2 = models.CharField(primary_key=True, max_length=2)
    iso_3166_1_a3 = models.CharField(max_length=3)
    iso_3166_1_numeric = models.CharField(max_length=3)
    printable_name = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    display_order = models.PositiveSmallIntegerField()
    is_shipping_country = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'address_country'


class AddressUseraddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    phone_number = models.CharField(max_length=128)
    notes = models.TextField()
    is_default_for_shipping = models.BooleanField()
    is_default_for_billing = models.BooleanField()
    hash = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    num_orders_as_billing_address = models.PositiveIntegerField()
    num_orders_as_shipping_address = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'address_useraddress'
        unique_together = (('user', 'hash'),)


class AnalyticsProductrecord(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num_views = models.PositiveIntegerField()
    num_basket_additions = models.PositiveIntegerField()
    num_purchases = models.PositiveIntegerField()
    score = models.FloatField()
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'analytics_productrecord'


class AnalyticsUserproductview(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date_created = models.DateTimeField()
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_userproductview'


class AnalyticsUserrecord(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num_product_views = models.PositiveIntegerField()
    num_basket_additions = models.PositiveIntegerField()
    num_orders = models.PositiveIntegerField()
    num_order_lines = models.PositiveIntegerField()
    num_order_items = models.PositiveIntegerField()
    total_spent = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    date_last_order = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'analytics_userrecord'


class AnalyticsUsersearch(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    query = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_usersearch'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BasketBasket(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    date_merged = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_basket'


class BasketBasketVouchers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING)
    voucher = models.ForeignKey('VoucherVoucher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'basket_basket_vouchers'
        unique_together = (('basket', 'voucher'),)


class BasketLine(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.PositiveIntegerField()
    price_currency = models.CharField(max_length=12)
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    price_incl_tax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    date_created = models.DateTimeField()
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING)
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING)
    line_reference = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'basket_line'
        unique_together = (('basket', 'line_reference'),)


class BasketLineattribute(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value = models.CharField(max_length=255)
    line = models.ForeignKey(BasketLine, models.DO_NOTHING)
    option = models.ForeignKey('CatalogueOption', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'basket_lineattribute'


class CatalogueAttributeoption(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    option = models.CharField(max_length=255)
    group = models.ForeignKey('CatalogueAttributeoptiongroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_attributeoption'
        unique_together = (('group', 'option'),)


class CatalogueAttributeoptiongroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'catalogue_attributeoptiongroup'


class CatalogueCategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'catalogue_category'


class CatalogueOption(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)
    type = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'catalogue_option'


class CatalogueProduct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    structure = models.CharField(max_length=10)
    upc = models.CharField(unique=True, max_length=64, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    is_discountable = models.BooleanField()
    product_class = models.ForeignKey('CatalogueProductclass', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_product'


class CatalogueProductProductOptions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_product_product_options'
        unique_together = (('product', 'option'),)


class CatalogueProductattribute(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    type = models.CharField(max_length=20)
    required = models.BooleanField()
    product_class = models.ForeignKey('CatalogueProductclass', models.DO_NOTHING, blank=True, null=True)
    option_group = models.ForeignKey(CatalogueAttributeoptiongroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_productattribute'


class CatalogueProductattributevalue(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value_text = models.TextField(blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    value_boolean = models.BooleanField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    value_richtext = models.TextField(blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_file = models.CharField(max_length=255, blank=True, null=True)
    value_image = models.CharField(max_length=255, blank=True, null=True)
    entity_object_id = models.PositiveIntegerField(blank=True, null=True)
    attribute = models.ForeignKey(CatalogueProductattribute, models.DO_NOTHING)
    entity_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    value_option = models.ForeignKey(CatalogueAttributeoption, models.DO_NOTHING, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_productattributevalue'
        unique_together = (('attribute', 'product'),)


class CatalogueProductattributevalueValueMultiOption(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    productattributevalue = models.ForeignKey(CatalogueProductattributevalue, models.DO_NOTHING)
    attributeoption = models.ForeignKey(CatalogueAttributeoption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productattributevalue_value_multi_option'
        unique_together = (('productattributevalue', 'attributeoption'),)


class CatalogueProductcategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    category = models.ForeignKey(CatalogueCategory, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productcategory'
        unique_together = (('product', 'category'),)


class CatalogueProductclass(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    requires_shipping = models.BooleanField()
    track_stock = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'catalogue_productclass'


class CatalogueProductclassOptions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    productclass = models.ForeignKey(CatalogueProductclass, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productclass_options'
        unique_together = (('productclass', 'option'),)


class CatalogueProductimage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    original = models.CharField(max_length=255)
    caption = models.CharField(max_length=200)
    display_order = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productimage'


class CatalogueProductrecommendation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ranking = models.PositiveSmallIntegerField()
    primary = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    recommendation = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productrecommendation'
        unique_together = (('primary', 'recommendation'),)


class CustomerCommunicationeventtype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    email_subject_template = models.CharField(max_length=255, blank=True, null=True)
    email_body_template = models.TextField(blank=True, null=True)
    email_body_html_template = models.TextField(blank=True, null=True)
    sms_template = models.CharField(max_length=170, blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'customer_communicationeventtype'


class CustomerEmail(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    subject = models.TextField()
    body_text = models.TextField()
    body_html = models.TextField()
    date_sent = models.DateTimeField()
    email = models.CharField(max_length=254, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_email'


class CustomerNotification(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    subject = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=32)
    date_sent = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    recipient = models.ForeignKey(AuthUser, models.DO_NOTHING)
    sender = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_notification'


class CustomerProductalert(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=128)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    date_confirmed = models.DateTimeField(blank=True, null=True)
    date_cancelled = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'customer_productalert'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFlatpage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_flatpage'


class DjangoFlatpageSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    flatpage = models.ForeignKey(DjangoFlatpage, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'
        unique_together = (('flatpage', 'site'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class OfferBenefit(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=128)
    value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    max_affected_items = models.PositiveIntegerField(blank=True, null=True)
    range = models.ForeignKey('OfferRange', models.DO_NOTHING, blank=True, null=True)
    proxy_class = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_benefit'


class OfferCondition(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=128)
    value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    range = models.ForeignKey('OfferRange', models.DO_NOTHING, blank=True, null=True)
    proxy_class = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_condition'


class OfferConditionaloffer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    offer_type = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
    priority = models.IntegerField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    max_global_applications = models.PositiveIntegerField(blank=True, null=True)
    max_user_applications = models.PositiveIntegerField(blank=True, null=True)
    max_basket_applications = models.PositiveIntegerField(blank=True, null=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total_discount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    num_applications = models.PositiveIntegerField()
    num_orders = models.PositiveIntegerField()
    redirect_url = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    benefit = models.ForeignKey(OfferBenefit, models.DO_NOTHING)
    condition = models.ForeignKey(OfferCondition, models.DO_NOTHING)
    exclusive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'offer_conditionaloffer'


class OfferRange(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    is_public = models.BooleanField()
    includes_all_products = models.BooleanField()
    proxy_class = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'offer_range'


class OfferRangeClasses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    productclass = models.ForeignKey(CatalogueProductclass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_classes'
        unique_together = (('range', 'productclass'),)


class OfferRangeExcludedProducts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_excluded_products'
        unique_together = (('range', 'product'),)


class OfferRangeIncludedCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    category = models.ForeignKey(CatalogueCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_included_categories'
        unique_together = (('range', 'category'),)


class OfferRangeproduct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    display_order = models.IntegerField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_rangeproduct'
        unique_together = (('range', 'product'),)


class OfferRangeproductfileupload(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filepath = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    date_uploaded = models.DateTimeField()
    status = models.CharField(max_length=32)
    error_message = models.CharField(max_length=255)
    date_processed = models.DateTimeField(blank=True, null=True)
    num_new_skus = models.PositiveIntegerField(blank=True, null=True)
    num_unknown_skus = models.PositiveIntegerField(blank=True, null=True)
    num_duplicate_skus = models.PositiveIntegerField(blank=True, null=True)
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    uploaded_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_rangeproductfileupload'


class OrderBillingaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_billingaddress'


class OrderCommunicationevent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date_created = models.DateTimeField()
    event_type = models.ForeignKey(CustomerCommunicationeventtype, models.DO_NOTHING)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_communicationevent'


class OrderLine(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    partner_name = models.CharField(max_length=128)
    partner_sku = models.CharField(max_length=128)
    partner_line_reference = models.CharField(max_length=128)
    partner_line_notes = models.TextField()
    title = models.CharField(max_length=255)
    upc = models.CharField(max_length=128, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    line_price_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    line_price_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    line_price_before_discounts_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    line_price_before_discounts_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    unit_cost_price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    unit_price_incl_tax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    unit_price_excl_tax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    unit_retail_price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    status = models.CharField(max_length=255)
    est_dispatch_date = models.DateField(blank=True, null=True)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)
    partner = models.ForeignKey('PartnerPartner', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_line'


class OrderLineattribute(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=128)
    value = models.CharField(max_length=255)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_lineattribute'


class OrderLineprice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.PositiveIntegerField()
    price_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shipping_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shipping_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_lineprice'


class OrderOrder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    number = models.CharField(unique=True, max_length=128)
    currency = models.CharField(max_length=12)
    total_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shipping_incl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shipping_excl_tax = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    status = models.CharField(max_length=100)
    date_placed = models.DateTimeField()
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING, blank=True, null=True)
    billing_address = models.ForeignKey(OrderBillingaddress, models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey('OrderShippingaddress', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    guest_email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'order_order'


class OrderOrderdiscount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    category = models.CharField(max_length=64)
    offer_id = models.PositiveIntegerField(blank=True, null=True)
    offer_name = models.CharField(max_length=128)
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    voucher_code = models.CharField(max_length=128)
    frequency = models.PositiveIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    message = models.TextField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_orderdiscount'


class OrderOrdernote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    note_type = models.CharField(max_length=128)
    message = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_ordernote'


class OrderPaymentevent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    reference = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    event_type = models.ForeignKey('OrderPaymenteventtype', models.DO_NOTHING)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    shipping_event = models.ForeignKey('OrderShippingevent', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_paymentevent'


class OrderPaymenteventquantity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.PositiveIntegerField()
    event = models.ForeignKey(OrderPaymentevent, models.DO_NOTHING)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_paymenteventquantity'
        unique_together = (('event', 'line'),)


class OrderPaymenteventtype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=128)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'order_paymenteventtype'


class OrderShippingaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    phone_number = models.CharField(max_length=128)
    notes = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingaddress'


class OrderShippingevent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    notes = models.TextField()
    date_created = models.DateTimeField()
    event_type = models.ForeignKey('OrderShippingeventtype', models.DO_NOTHING)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingevent'


class OrderShippingeventquantity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.PositiveIntegerField()
    event = models.ForeignKey(OrderShippingevent, models.DO_NOTHING)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingeventquantity'
        unique_together = (('event', 'line'),)


class OrderShippingeventtype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'order_shippingeventtype'


class PartnerPartner(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'partner_partner'


class PartnerPartnerUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_partner_users'
        unique_together = (('partner', 'user'),)


class PartnerPartneraddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_partneraddress'


class PartnerStockalert(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    threshold = models.PositiveIntegerField()
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    date_closed = models.DateTimeField(blank=True, null=True)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_stockalert'


class PartnerStockrecord(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    partner_sku = models.CharField(max_length=128)
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    price_retail = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cost_price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    num_in_stock = models.PositiveIntegerField(blank=True, null=True)
    num_allocated = models.IntegerField(blank=True, null=True)
    low_stock_threshold = models.PositiveIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    price_currency = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'partner_stockrecord'
        unique_together = (('partner', 'partner_sku'),)


class PaymentBankcard(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    card_type = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=32)
    expiry_date = models.DateField()
    partner_reference = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_bankcard'


class PaymentSource(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    currency = models.CharField(max_length=12)
    amount_allocated = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    amount_debited = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    amount_refunded = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    label = models.CharField(max_length=128)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    source_type = models.ForeignKey('PaymentSourcetype', models.DO_NOTHING)
    reference = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'payment_source'


class PaymentSourcetype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'payment_sourcetype'


class PaymentTransaction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    txn_type = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    reference = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    source = models.ForeignKey(PaymentSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PromotionsAutomaticproductlist(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    description = models.TextField()
    link_url = models.CharField(max_length=200)
    link_text = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    method = models.CharField(max_length=128)
    num_products = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'promotions_automaticproductlist'


class PromotionsHandpickedproductlist(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    description = models.TextField()
    link_url = models.CharField(max_length=200)
    link_text = models.CharField(max_length=255)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions_handpickedproductlist'


class PromotionsImage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    link_url = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions_image'


class PromotionsKeywordpromotion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.PositiveIntegerField()
    position = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    keyword = models.CharField(max_length=200)
    filter = models.CharField(max_length=200)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_keywordpromotion'


class PromotionsMultiimage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions_multiimage'


class PromotionsMultiimageImages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    multiimage = models.ForeignKey(PromotionsMultiimage, models.DO_NOTHING)
    image = models.ForeignKey(PromotionsImage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_multiimage_images'
        unique_together = (('multiimage', 'image'),)


class PromotionsOrderedproduct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    display_order = models.PositiveIntegerField()
    list = models.ForeignKey(PromotionsHandpickedproductlist, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_orderedproduct'
        unique_together = (('list', 'product'),)


class PromotionsOrderedproductlist(models.Model):
    handpickedproductlist_ptr = models.ForeignKey(PromotionsHandpickedproductlist, models.DO_NOTHING, primary_key=True)
    display_order = models.PositiveIntegerField()
    tabbed_block = models.ForeignKey('PromotionsTabbedblock', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_orderedproductlist'


class PromotionsPagepromotion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.PositiveIntegerField()
    position = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    page_url = models.CharField(max_length=128)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_pagepromotion'


class PromotionsRawhtml(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    display_type = models.CharField(max_length=128)
    body = models.TextField()
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions_rawhtml'


class PromotionsSingleproduct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateTimeField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotions_singleproduct'


class PromotionsTabbedblock(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promotions_tabbedblock'


class ReviewsProductreview(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    score = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    homepage = models.CharField(max_length=200)
    status = models.SmallIntegerField()
    total_votes = models.IntegerField()
    delta_votes = models.IntegerField()
    date_created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews_productreview'
        unique_together = (('product', 'user'),)


class ReviewsVote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    delta = models.SmallIntegerField()
    date_created = models.DateTimeField()
    review = models.ForeignKey(ReviewsProductreview, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_vote'
        unique_together = (('user', 'review'),)


class ShippingOrderanditemcharges(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    price_per_order = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    price_per_item = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    free_shipping_threshold = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'shipping_orderanditemcharges'


class ShippingOrderanditemchargesCountries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    orderanditemcharges = models.ForeignKey(ShippingOrderanditemcharges, models.DO_NOTHING)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_orderanditemcharges_countries'
        unique_together = (('orderanditemcharges', 'country'),)


class ShippingWeightband(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    upper_limit = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    charge = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    method = models.ForeignKey('ShippingWeightbased', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_weightband'


class ShippingWeightbased(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    default_weight = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'shipping_weightbased'


class ShippingWeightbasedCountries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    weightbased = models.ForeignKey(ShippingWeightbased, models.DO_NOTHING)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_weightbased_countries'
        unique_together = (('weightbased', 'country'),)


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'


class VoucherVoucher(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)
    usage = models.CharField(max_length=128)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    num_basket_additions = models.PositiveIntegerField()
    num_orders = models.PositiveIntegerField()
    total_discount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    date_created = models.DateTimeField()
    voucher_set = models.ForeignKey('VoucherVoucherset', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_voucher'


class VoucherVoucherOffers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    voucher = models.ForeignKey(VoucherVoucher, models.DO_NOTHING)
    conditionaloffer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voucher_voucher_offers'
        unique_together = (('voucher', 'conditionaloffer'),)


class VoucherVoucherapplication(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey(VoucherVoucher, models.DO_NOTHING)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher_voucherapplication'


class VoucherVoucherset(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    code_length = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    offer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING, unique=True, blank=True, null=True)
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'voucher_voucherset'


class WishlistsLine(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)
    wishlist = models.ForeignKey('WishlistsWishlist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlists_line'
        unique_together = (('wishlist', 'product'),)


class WishlistsWishlist(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=6)
    visibility = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlists_wishlist'
