import os
from openai import OpenAI


class SportsRehabAgent:
    """
    运动康复智能 Agent
    功能：
    1. 收集用户运动后的身体状态
    2. 基于规则判断风险等级
    3. 调用大语言模型生成个性化康复建议
    4. 对高风险情况进行就医提醒
    """

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "未检测到 OPENAI_API_KEY。请先在终端设置环境变量：\n"
                "macOS/Linux: export OPENAI_API_KEY='你的API_KEY'\n"
                "Windows PowerShell: setx OPENAI_API_KEY '你的API_KEY'"
            )

        self.client = OpenAI(api_key=api_key)

        self.system_prompt = """
你是一名专业、谨慎、负责任的运动康复智能 Agent。
你的任务是根据用户运动后的身体情况，给出基础康复建议和风险提醒。

你必须遵守以下规则：
1. 你不能进行医学诊断，不能替代医生。
2. 如果用户出现剧烈疼痛、明显肿胀、活动受限、麻木、刺痛、头晕、胸痛、呼吸困难、疼痛持续超过3天等情况，必须优先建议用户及时就医。
3. 不要随意推荐处方药。
4. 可以给出基础建议，例如休息、拉伸、冷热敷、补水、营养补充、降低运动强度等。
5. 回答要结构清晰，适合普通用户理解。
6. 输出内容应包含：
   - 状态判断
   - 风险等级
   - 恢复建议
   - 注意事项
   - 是否建议就医
"""

    def collect_user_info(self):
        print("========== 运动康复智能 Agent ==========")
        print("你好，我会根据你运动后的身体情况，给出基础康复建议。")
        print("请依次回答下面几个问题。\n")

        info = {}
        info["exercise_type"] = input("1. 你进行了什么运动？例如跑步、篮球、健身、足球等：")
        info["exercise_intensity"] = input("2. 运动强度如何？低 / 中 / 高：")
        info["pain_area"] = input("3. 是否有不适部位？例如膝盖、小腿、肩膀、腰部；没有可填“无”：")
        info["pain_level"] = input("4. 疼痛程度 0-10 分是多少？0 表示不痛，10 表示非常痛：")
        info["duration"] = input("5. 不适持续了多久？例如 1小时、1天、3天以上：")
        info["symptoms"] = input("6. 是否有肿胀、麻木、刺痛、活动受限、头晕、胸痛、呼吸困难等情况？没有可填“无”：")

        return info

    def assess_risk(self, info):
        high_risk_keywords = [
            "剧烈", "严重", "肿胀", "明显肿胀", "麻木", "刺痛",
            "活动受限", "不能走", "无法活动", "头晕", "胸痛",
            "呼吸困难", "骨折", "扭伤严重"
        ]

        medium_risk_keywords = [
            "疼", "酸痛", "拉伤", "不舒服", "僵硬", "轻微肿胀"
        ]

        symptoms_text = (
            info["pain_area"]
            + info["pain_level"]
            + info["duration"]
            + info["symptoms"]
        )

        try:
            pain_score = int(info["pain_level"])
        except ValueError:
            pain_score = 0

        if pain_score >= 7:
            return "高风险"

        for keyword in high_risk_keywords:
            if keyword in symptoms_text:
                return "高风险"

        if (
            "3天" in info["duration"]
            or "三天" in info["duration"]
            or "超过3天" in info["duration"]
            or "三天以上" in info["duration"]
        ):
            return "高风险"

        if pain_score >= 4:
            return "中风险"

        for keyword in medium_risk_keywords:
            if keyword in symptoms_text:
                return "中风险"

        return "低风险"

    def build_prompt(self, info, risk_level):
        return f"""
请根据以下用户信息，生成一份个性化运动康复建议。

用户运动信息：
- 运动类型：{info["exercise_type"]}
- 运动强度：{info["exercise_intensity"]}
- 不适部位：{info["pain_area"]}
- 疼痛程度：{info["pain_level"]}/10
- 持续时间：{info["duration"]}
- 其他症状：{info["symptoms"]}

系统初步风险判断：{risk_level}

请按照以下结构输出：
1. 状态判断
2. 风险等级说明
3. 个性化恢复建议
4. 拉伸或放松建议
5. 饮食与休息建议
6. 风险提醒
7. 是否建议就医

要求：
- 语言简洁、专业、适合普通用户理解。
- 如果风险等级是高风险，必须明确建议用户停止运动并及时就医。
- 不要给出处方药建议。
"""

    def generate_advice(self, prompt):
        response = self.client.responses.create(
            model="gpt-5.5",
            instructions=self.system_prompt,
            input=prompt
        )
        return response.output_text

    def run(self):
        info = self.collect_user_info()
        risk_level = self.assess_risk(info)
        prompt = self.build_prompt(info, risk_level)

        print("\n正在分析，请稍等...\n")

        try:
            advice = self.generate_advice(prompt)
            print("========== 康复建议结果 ==========\n")
            print(advice)
        except Exception as e:
            print("调用大语言模型失败。")
            print("错误信息：", e)
            print("\n请检查：")
            print("1. 是否已经安装 openai：pip install openai")
            print("2. 是否已经设置 OPENAI_API_KEY")
            print("3. 网络是否正常")
            print("4. API Key 是否有调用权限")


if __name__ == "__main__":
    agent = SportsRehabAgent()
    agent.run()
