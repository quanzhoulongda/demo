# BMI指数计算器

def calculate_bmi(weight, height):
    """根据体重(kg)和身高(m)计算BMI指数"""
    if height <= 0 or weight <= 0:
        raise ValueError("身高和体重必须为正数")
    return weight / (height ** 2)


def classify_bmi(bmi):
    """根据BMI指数进行分类"""
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif 24 <= bmi < 28:
        return "超重"
    else:
        return "肥胖"


def main():
    print("=== BMI指数计算器 ===")
    try:
        weight = float(input("请输入您的体重(kg): "))
        height = float(input("请输入您的身高(m): "))
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"您的BMI指数为: {bmi:.2f}")
        print(f"您的体型分类为: {category}")
    except ValueError as e:
        print(f"输入错误: {e}")


if __name__ == "__main__":
    main()
