import pandas as pd
import numpy as np

# DataFrame是个二维结构，这里首先构造一组时间序列，作为我们的下标
date = pd.date_range('20180101', periods=6)
print(date)

# 然后创建一个DataFrame结构,不指定index参数和columns。那么值将从0开始
df = pd.DataFrame(np.random.randn(6, 4))
print(df)
# 指定index，columns参数
df = pd.DataFrame(np.random.randn(6, 4), index=date, columns=list('ABCD'))
print(df)


# 除了向DataFrame 中传入二维数组，我们也可以使用字典传入数据
# 字典的每个key代表一列，其value可以是各种能够转化为Series的对象
# DataFrame 只要求每一列数据的格式相同
df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20181001'),
                    'C': pd.Series(1, index=list(range(4))),
                    'D': np.array([3] * 4, dtype=int),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'abc'})
print(df2)
# 查看各个列的数据类型
print(df2.dtypes)


# 查看数据 head 和 tail 方法可以分别查看前面几行和最后几行的数据（默认为5）
print(df.head())  # 默认查看前五行
print(df.tail())  # 默认查看后五行
print(df.head(3))  # 查看前3行

# 下标查看数据
print(df.index)

# 列标使用 columns 属性查看
print(df.columns)

# 使用 values 查看
print(df.values)