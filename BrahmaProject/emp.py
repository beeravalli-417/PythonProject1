#print ("hello world")


a = 87
b = 5
sum_result = a + b
print("Addition:", sum_result)  # Output: 15
x = 25
y = 9
difference = x - y
print("Subtraction:", difference)  # Output: 12
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("CSVReader").getOrCreate()
df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)

# list1 = []
# list2 = list()
# list3 = [1, 1, 2,"python",True, 2.0,[1,2,3]]
# #print(list3)
# print(type(list))
# print = range (1,100)
# print(a)
# a = list (range(1,100))
# print(a)
# a = range (1,101,2)
# for x in a:
#     print(x)
#a = list(range (100))
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
],
print (matrix(0)(2))
#list = [1,12,"python",True, 2.0,[1,2,3]]


print(len(list3))


