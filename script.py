from pyspark.sql import SparkSession, Row

def get_product_category_pairs(products, categories, product_categories):
    product_category = products.join(product_categories, products.id == product_categories.product_id, how="left_outer")\
                               .join(categories, product_categories.category_id == categories.id, how="left_outer")\
                               .select(products.name, categories.category)
    return product_category
    
spark = SparkSession.builder.getOrCreate()
products = spark.createDataFrame(
    [Row(id=1, name='product_ab_1'), 
     Row(id=2, name='product_ac_2'), 
     Row(id=3, name='product_null_3')])
categories = spark.createDataFrame([Row(id=1, category='A'), 
                                    Row(id=2, category='B'), 
                                    Row(id=3, category='C')])
product_categories = spark.createDataFrame([Row(product_id=1, category_id=1), 
                                            Row(product_id=1, category_id=2), 
                                            Row(product_id=2, category_id=1), 
                                            Row(product_id=2, category_id=3)])
get_product_category_pairs(products, categories, product_categories).show()