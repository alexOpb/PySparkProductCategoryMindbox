from pyspark.sql import SparkSession, Row

def get_product_category_pairs(products, categories):
    return products.join(categories, on="id", how="left_outer").select("name", "category")
    
spark = SparkSession.builder.getOrCreate()
products = spark.createDataFrame(
    [Row(id=1, name='product_ab_1'), 
     Row(id=2, name='product_ac_2'), 
     Row(id=3, name='product_null_3')])
categories = spark.createDataFrame(
    [Row(id=1, category='A'), 
     Row(id=1, category='B'), 
     Row(id=2, category='A'), 
     Row(id=2, category='C')])

get_product_category_pairs(products, categories).show()