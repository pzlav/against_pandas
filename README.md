## Evolving Data Analytics Speed: Pandas Versus Today Libraries

![Pandas](./img/pandas.png)

Over the years, Pandas has become a key component of the Python data ecosystem, often used in conjunction with libraries like Matplotlib for plotting, Scikit-learn for machine learning, and others. Pandas is widely used in various fields for data analysis, financial modeling, data cleaning, and preprocessing, both in academic research and industry applications. 
So why anyone want choose different package instead pandas?
1.	While Pandas offers reasonable performance for most use cases, it is not always the fastest tool for every scenario.
2.	Parallel processing in Pandas is not natively supported in the core library, which is primarily designed for single-threaded operations.
3.	Pandas can be memory-intensive, especially when dealing with very large datasets. It often requires more memory than the size of the data being processed.
4.	Pandas syntax can be initially challenging to understand and remember, particularly for more complex operations.

So whats alternatives can be chosen for pandas in 2023. It depends from a lot of factors like size of the data, requirements for speed and you environment. In this I’ll try to test several libraries on very common use case of transforming data from CSV file.

 ---
![Polars](./img/polars.png)
Polars is a highly performant library for manipulating structured data is written in Rust and fully utilises the power of parallel processing. Polars have lazy execution mode that significantly speed up computation and utilize Apache Arrow engine.


![DuckDB](./img/duckdb.png)
DuckDB is a relational DBMS that supports SQL. DuckDB contains a columnar-vectorized query execution engine, written on C++, where queries are still interpreted, but a large batch of values (a “vector”) are processed in one operation. Vectorized query execution leads to far better performance in OLAP queries.

![Pandas 2.0](./img/pandas20.png)
In 2.0 release, the big change is related to the introduction of the Apache Arrow server side for pandas data. PyArrow takes care of the previous memory limitations of version 1.X and allows for faster and more memory-efficient data operations, especially for large datasets.

![ChDB](./img/chdb.png)
Chdb is an embedded Clickhouse engine through MemoryView. In a simple words you can use power of fast vector database in you python script with out the need of deploying Clickhouse.

![Datafusion](./img/datafusion.png)
DataFusion, is written in Rust Python library that binds to Apache Arrow in-memory query engine DataFusion. Execute queries using SQL or DataFrames against CSV, Parquet, and JSON data sources

---
My computer setup: Intel Xeon Icelake, 32 Gb RAM, Ubuntu 20.04
I want speed up transformation of large dataset (10-100 Gb) don’t go out from my python file.
Lets try to compare this libraries with simple task of processing data on CSV file with filtering and aggregations. I will test it on 3 CSV files different size but the same structure.

I got following results:
![Time to perform task with CSV file](./img/table1.png)

Results show that you can get significant speed up with modern libraries.

Should admit It’s not professional benchmark also all packages are actively developing so results may change significantly. 
All source scripts and datasets can be found here https://github.com/pzlav/against_pandas


Conclusion:

1 As Pandas is still a king for simple data analysis task you have a lot of alternatives for more complex tasks that can significantly speed up your work.
2 Classic trio of classic ML: Pandas, NumPy, Sci-kit today is not the only choice for data analysis.
3 If dont like pandas syntax there a lot of alternatives with SQL like syntax.
4 Modern libraries offer versatile set of tools. You should choose libraries according to your task.
5 The most painless transition from pandas to other libraries is Pandas 2.0 with Apache Arrow engine and Polars.

