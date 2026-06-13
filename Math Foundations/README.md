# Gradiant Descent

梯度下降法（Gradient Descent）是一种优化算法，用于寻找函数的局部最小值。它通过迭代地调整参数来最小化目标函数。

例如对于一个函数 f(x)，我们可以计算其导数 f'(x)，然后按照以下方式更新参数 x：

```python
x = x - learning_rate * f'(x)
```

