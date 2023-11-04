import numpy as np 

def softmax(x):
    # 计算指数函数
    exp_values = np.exp(x - np.max(x))
    # exp_values = np.exp(x)
    # 计算每个元素的概率
    probabilities = exp_values / np.sum(exp_values, axis=0)
    return probabilities

def l2_norm(x):
    norm = np.linalg.norm(x)
    return x / norm

def min_max_norm(x):
    min_value = min(x)
    max_value = max(x)
    # return (x - min_value) / (max_value - min_value)
    norm = (x - min_value) / (max_value - min_value)
    return norm/sum(norm)

def z_score_norm(x):
    mean = np.mean(x)  # 计算均值
    std = np.std(x)  # 计算标准差
    normalized_data = (x - mean) / std  # 归一化计算
    return normalized_data

def de_count(each_cost, total_pay, norm_type="l2_norm"):
    """
    计算每个人应付的钱.
    差距较小用 l2_norm
    差距较大用 z_score_norm
    无法免除最后一人的支出，若需免除，输入直接去除该人即可。

    Args:
        each_cost (list): 每个人赢钱数额.
        total_pay (int): 需要分摊的饮料钱.
    """
    each_cost = np.array(each_cost)
    if norm_type == "min_max_norm":
        cost_rate = min_max_norm(each_cost)
    elif norm_type == "z_score_norm":
        cost_rate = z_score_norm(each_cost)
    elif norm_type == "l2_norm":
        cost_rate = l2_norm(each_cost)
    print("cost_rate:{}".format([round(x,2) for x in cost_rate]))
    cost_rate = softmax(cost_rate)
    final_cost = total_pay * cost_rate
    print("should_pay:{}".format([round(x,2) for x in final_cost]))
    print("final_record:{}".format([round(x,2) for x in (each_cost - final_cost)]))
    return final_cost

# 1
# gold_cost: [30, 25, 20, 15, 10]
# predict_cost: [33.94, 23.21, 21.11, 10.95, 10.79]
# each_cost = [42.2, 16.6, 10.2, -34, -35]
# total_pay = 100
# final_cost = de_count(each_cost, total_pay, "l2_norm")

# 2
# gold_cost: [80, 30, 15, 12, 9, 6, 3]
# predict_cost: [93.94, 15.74, 7.78, 7.48, 5.97, 4.62, 4.16]
# each_cost = [157.5, 37.4, -10, -12.6, -27.8, -45, -52]
# total_pay = 139.7
# final_cost = de_count(each_cost, total_pay, "z_score_norm")

# 3
# gold_cost: [56, 46, 36, 26, 16]
# predict_cost: [65.4, 46.32, 25.63, 23.0, 20.75]
# each_cost = [63.5, 30, -27.5, -38, -48]
# total_pay = 181.1
# final_cost = de_count(each_cost, total_pay, "l2_norm")

# 4
# gold_cost: [80, 30, 7, 4.1, 0]
# predict_cost: [71.4, 24.94, 11.02, 10.17, 3.57]
each_cost = [121.8, 40.3, -23, -29.2, -110.4]
total_pay = 121.1
final_cost = de_count(each_cost, total_pay, "z_score_norm")

