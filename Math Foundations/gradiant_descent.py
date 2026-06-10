class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        minimizer = init

        for _ in range(iterations):
            derivative = 2 * minimizer
            minimizer = minimizer - learning_rate * derivative

        return round(minimizer, 5)


if __name__ == '__main__':
    # 自动测试输入输出
    tests = [
        (10, 0.1, 5),
        (20, 0.05, -3),
        (15, 0.01, 2.5),
    ]
    solution = Solution()
    for iterations, learning_rate, init in tests:
        result = solution.get_minimizer(iterations, learning_rate, init)
        print(f'iterations={iterations}, learning_rate={learning_rate}, init={init} -> {result}')