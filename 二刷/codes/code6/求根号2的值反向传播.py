def gradient_descent_sqrt2(initial_guess=2.0, learning_rate=0.001, epsilon=1e-7, max_epochs=10000):
    """
    使用梯度下降法计算根号2
    :param initial_guess: 初始猜测值
    :param learning_rate: 学习率
    :param epsilon: 停止迭代的精度阈值
    :param max_epochs: 最大迭代次数
    """
    x = initial_guess
    
    for i in range(max_epochs):
        # 1. 计算损失函数的梯度: 4x(x^2 - 2)
        gradient = 4 * x * (x**2 - 2)
        
        # 2. 更新 x
        x_new = x - learning_rate * gradient
        
        # 3. 计算当前的损失值 (x^2 - 2)^2，用于观察
        loss = (x_new**2 - 2)**2
        
        # 打印部分过程
        if i % 100 == 0:
            print(f"Epoch {i}: x = {x_new:.6f}, loss = {loss:.8f}")
            
        # 4. 检查收敛条件（如果变化极其微小则停止）
        if abs(x_new - x) < epsilon:
            print(f"\nConverged at Epoch {i}!")
            break
            
        x = x_new
        
    return x

# 执行
import math

# 注意：初始值不能为0，因为0处的梯度为0，无法移动
result = gradient_descent_sqrt2(initial_guess=2.0, learning_rate=0.01)

print("-" * 30)
print(f"计算结果: {result}")
print(f"真实值  : {math.sqrt(2)}")
print(f"误差    : {abs(result - math.sqrt(2))}")