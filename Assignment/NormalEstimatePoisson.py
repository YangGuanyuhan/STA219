import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

# 设置不同的 λ 值
lambdas = [1, 5, 10, 20]

# 绘制图形
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.ravel()

# 对每个 λ 值进行绘图
for i, lam in enumerate(lambdas):
    # 泊松分布
    x_vals = np.arange(0, int(lam + 5), 1)
    poisson_vals = poisson.pmf(x_vals, lam)

    # 正态分布逼近
    mean = lam
    std_dev = np.sqrt(lam)
    normal_vals = norm.pdf(x_vals, mean, std_dev)

    # 绘制泊松分布和正态分布
    axes[i].stem(x_vals, poisson_vals, label='Poisson', basefmt=" ")
    axes[i].plot(x_vals, normal_vals, label='Normal Approximation', color='red')

    # 设置图标题和标签
    axes[i].set_title(f'Poisson Distribution (λ={lam}) vs Normal Approximation')
    axes[i].legend()

# 显示图形
plt.tight_layout()
plt.show()
