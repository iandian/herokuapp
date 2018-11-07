# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class NideshopAd(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    ad_position_id = models.SmallIntegerField()
    media_type = models.IntegerField()
    name = models.CharField(max_length=60)
    link = models.CharField(max_length=255)
    image_url = models.TextField()
    content = models.CharField(max_length=255)
    end_time = models.IntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_ad'


class NideshopAdPosition(models.Model):
    name = models.CharField(max_length=60)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_ad_position'


class NideshopAddress(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    country_id = models.SmallIntegerField()
    province_id = models.SmallIntegerField()
    city_id = models.SmallIntegerField()
    district_id = models.SmallIntegerField()
    address = models.CharField(max_length=120)
    mobile = models.CharField(max_length=60)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_address'


class NideshopAdmin(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    password_salt = models.CharField(max_length=255)
    last_login_ip = models.CharField(max_length=60)
    last_login_time = models.IntegerField()
    add_time = models.IntegerField()
    update_time = models.IntegerField()
    avatar = models.CharField(max_length=255)
    admin_role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_admin'


class NideshopAttribute(models.Model):
    attribute_category_id = models.IntegerField()
    name = models.CharField(max_length=60)
    input_type = models.IntegerField()
    values = models.TextField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_attribute'


class NideshopAttributeCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_attribute_category'


class NideshopBrand(models.Model):
    name = models.CharField(max_length=255)
    list_pic_url = models.CharField(max_length=255)
    simple_desc = models.CharField(max_length=255)
    pic_url = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    is_show = models.IntegerField()
    floor_price = models.DecimalField(max_digits=10, decimal_places=2)
    app_list_pic_url = models.CharField(max_length=255)
    is_new = models.IntegerField()
    new_pic_url = models.CharField(max_length=255)
    new_sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_brand'


class NideshopCart(models.Model):
    user_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    goods_id = models.IntegerField()
    goods_sn = models.CharField(max_length=60)
    product_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.SmallIntegerField()
    goods_specifition_name_value = models.TextField()
    goods_specifition_ids = models.CharField(max_length=60)
    checked = models.IntegerField()
    list_pic_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_cart'


class NideshopCategory(models.Model):
    name = models.CharField(max_length=90)
    keywords = models.CharField(max_length=255)
    front_desc = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField()
    show_index = models.IntegerField()
    is_show = models.IntegerField()
    banner_url = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    wap_banner_url = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    type = models.IntegerField()
    front_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_category'


class NideshopChannel(models.Model):
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_channel'


class NideshopCollect(models.Model):
    user_id = models.IntegerField()
    value_id = models.IntegerField()
    add_time = models.IntegerField()
    is_attention = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_collect'


class NideshopComment(models.Model):
    type_id = models.IntegerField()
    value_id = models.IntegerField()
    content = models.CharField(max_length=6550)
    add_time = models.BigIntegerField()
    status = models.IntegerField()
    user_id = models.IntegerField()
    new_content = models.CharField(max_length=6550)

    class Meta:
        managed = False
        db_table = 'nideshop_comment'


class NideshopCommentPicture(models.Model):
    comment_id = models.IntegerField()
    pic_url = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_comment_picture'


class NideshopCoupon(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    type_money = models.DecimalField(max_digits=10, decimal_places=2)
    send_type = models.IntegerField()
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    send_start_date = models.IntegerField()
    send_end_date = models.IntegerField()
    use_start_date = models.IntegerField()
    use_end_date = models.IntegerField()
    min_goods_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'nideshop_coupon'


class NideshopFeedback(models.Model):
    msg_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=60)
    user_email = models.CharField(max_length=60)
    msg_title = models.CharField(max_length=200)
    msg_type = models.IntegerField()
    msg_status = models.IntegerField()
    msg_content = models.TextField()
    msg_time = models.IntegerField()
    message_img = models.CharField(max_length=255)
    order_id = models.IntegerField()
    msg_area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_feedback'


class NideshopFootprint(models.Model):
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_footprint'


class NideshopGoods(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    goods_sn = models.CharField(max_length=60)
    name = models.CharField(max_length=120)
    brand_id = models.IntegerField()
    goods_number = models.IntegerField()
    keywords = models.CharField(max_length=255)
    goods_brief = models.CharField(max_length=255)
    goods_desc = models.TextField(blank=True, null=True)
    is_on_sale = models.IntegerField()
    add_time = models.IntegerField()
    sort_order = models.SmallIntegerField()
    is_delete = models.IntegerField()
    attribute_category = models.IntegerField()
    counter_price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.IntegerField()
    goods_unit = models.CharField(max_length=45)
    primary_pic_url = models.CharField(max_length=255)
    list_pic_url = models.CharField(max_length=255)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_volume = models.IntegerField()
    primary_product_id = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_desc = models.CharField(max_length=255)
    promotion_tag = models.CharField(max_length=45)
    app_exclusive_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_app_exclusive = models.IntegerField()
    is_limited = models.IntegerField()
    is_hot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_goods'


class NideshopGoodsAttribute(models.Model):
    goods_id = models.IntegerField()
    attribute_id = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'nideshop_goods_attribute'


class NideshopGoodsGallery(models.Model):
    goods_id = models.IntegerField()
    img_url = models.CharField(max_length=255)
    img_desc = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_goods_gallery'


class NideshopGoodsIssue(models.Model):
    goods_id = models.TextField(blank=True, null=True)
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nideshop_goods_issue'


class NideshopGoodsSpecification(models.Model):
    goods_id = models.IntegerField()
    specification_id = models.IntegerField()
    value = models.CharField(max_length=50)
    pic_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_goods_specification'


class NideshopKeywords(models.Model):
    keyword = models.CharField(max_length=90)
    is_hot = models.IntegerField()
    is_default = models.IntegerField()
    is_show = models.IntegerField()
    sort_order = models.IntegerField()
    scheme_url = models.CharField(db_column='scheme _url', max_length=255)  # Field renamed to remove unsuitable characters.
    id = models.AutoField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_keywords'
        unique_together = (('keyword', 'id'),)


class NideshopOrder(models.Model):
    order_sn = models.CharField(unique=True, max_length=20)
    user_id = models.IntegerField()
    order_status = models.IntegerField()
    shipping_status = models.IntegerField()
    pay_status = models.IntegerField()
    consignee = models.CharField(max_length=60)
    country = models.SmallIntegerField()
    province = models.SmallIntegerField()
    city = models.SmallIntegerField()
    district = models.SmallIntegerField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=60)
    postscript = models.CharField(max_length=255)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pay_name = models.CharField(max_length=120)
    pay_id = models.IntegerField()
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.IntegerField()
    integral_money = models.DecimalField(max_digits=10, decimal_places=2)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    confirm_time = models.IntegerField()
    pay_time = models.IntegerField()
    freight_price = models.IntegerField()
    coupon_id = models.IntegerField()
    parent_id = models.IntegerField()
    coupon_price = models.DecimalField(max_digits=10, decimal_places=2)
    callback_status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nideshop_order'


class NideshopOrderExpress(models.Model):
    order_id = models.IntegerField()
    shipper_id = models.IntegerField()
    shipper_name = models.CharField(max_length=120)
    shipper_code = models.CharField(max_length=60)
    logistic_code = models.CharField(max_length=20)
    traces = models.CharField(max_length=2000)
    is_finish = models.IntegerField()
    request_count = models.IntegerField(blank=True, null=True)
    request_time = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_order_express'


class NideshopOrderGoods(models.Model):
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_sn = models.CharField(max_length=60)
    product_id = models.IntegerField()
    number = models.SmallIntegerField()
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_specifition_name_value = models.TextField()
    is_real = models.IntegerField()
    goods_specifition_ids = models.CharField(max_length=255)
    list_pic_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_order_goods'


class NideshopProduct(models.Model):
    goods_id = models.IntegerField()
    goods_specification_ids = models.CharField(max_length=50)
    goods_sn = models.CharField(max_length=60)
    goods_number = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'nideshop_product'


class NideshopRegion(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    parent_id = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    type = models.IntegerField()
    agency_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_region'


class NideshopRelatedGoods(models.Model):
    goods_id = models.IntegerField()
    related_goods_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_related_goods'


class NideshopSearchHistory(models.Model):
    keyword = models.CharField(max_length=50)
    from_field = models.CharField(db_column='from', max_length=45)  # Field renamed because it was a Python reserved word.
    add_time = models.IntegerField()
    user_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nideshop_search_history'


class NideshopShipper(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_shipper'


class NideshopSpecification(models.Model):
    name = models.CharField(max_length=60)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_specification'


class NideshopTopic(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    avatar = models.CharField(max_length=255)
    item_pic_url = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    topic_category_id = models.IntegerField()
    price_info = models.DecimalField(max_digits=10, decimal_places=2)
    read_count = models.CharField(max_length=255)
    scene_pic_url = models.CharField(max_length=255)
    topic_template_id = models.IntegerField()
    topic_tag_id = models.IntegerField()
    sort_order = models.IntegerField()
    is_show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_topic'


class NideshopTopicCategory(models.Model):
    title = models.CharField(max_length=255)
    pic_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_topic_category'


class NideshopUser(models.Model):
    username = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=32)
    gender = models.IntegerField()
    birthday = models.IntegerField()
    register_time = models.IntegerField()
    last_login_time = models.IntegerField()
    last_login_ip = models.CharField(max_length=15)
    user_level_id = models.IntegerField()
    nickname = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    register_ip = models.CharField(max_length=45)
    avatar = models.CharField(max_length=255)
    weixin_openid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nideshop_user'


class NideshopUserCoupon(models.Model):
    coupon_id = models.IntegerField()
    coupon_number = models.CharField(max_length=20)
    user_id = models.IntegerField()
    used_time = models.IntegerField()
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nideshop_user_coupon'


class NideshopUserLevel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nideshop_user_level'
