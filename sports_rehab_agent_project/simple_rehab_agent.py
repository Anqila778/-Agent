def simple_rehab_agent():
    print("========== 运动康复智能 Agent 简化版 ==========")

    exercise_type = input("运动类型：")
    intensity = input("运动强度（低/中/高）：")
    pain_area = input("不适部位：")

    try:
        pain_level = int(input("疼痛程度 0-10："))
    except ValueError:
        pain_level = 0

    duration = input("持续时间：")
    symptoms = input("其他症状：")

    high_risk_words = ["肿胀", "明显肿胀", "麻木", "刺痛", "活动受限", "胸痛", "呼吸困难", "头晕"]
    risk = "低风险"

    if pain_level >= 7:
        risk = "高风险"
    elif any(word in symptoms for word in high_risk_words):
        risk = "高风险"
    elif "3天" in duration or "三天" in duration or "超过3天" in duration:
        risk = "高风险"
    elif pain_level >= 4:
        risk = "中风险"

    print("\n========== 分析结果 ==========")
    print(f"运动类型：{exercise_type}")
    print(f"运动强度：{intensity}")
    print(f"不适部位：{pain_area}")
    print(f"疼痛程度：{pain_level}/10")
    print(f"持续时间：{duration}")
    print(f"其他症状：{symptoms}")
    print(f"风险等级：{risk}")

    print("\n========== 康复建议 ==========")

    if risk == "高风险":
        print("建议：请立即停止运动，避免继续负重或强行拉伸，并尽快就医。")
        print("原因：当前症状可能存在较高损伤风险，需要专业医生进一步判断。")
    elif risk == "中风险":
        print("建议：暂停高强度运动 24-48 小时。")
        print("可以进行轻柔拉伸、补水、保证睡眠，并观察症状变化。")
        print("如果疼痛加重、肿胀明显或持续超过 3 天，建议就医。")
    else:
        print("建议：当前更接近普通运动疲劳。")
        print("可以适当休息、补水、轻柔拉伸，并保证睡眠。")

    print("\n注意：本系统只能提供基础康复建议，不能替代医生诊断。")


if __name__ == "__main__":
    simple_rehab_agent()
