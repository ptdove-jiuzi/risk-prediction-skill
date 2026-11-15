# First-use User Context

## Purpose

Ask for a small amount of user context before the first substantive risk analysis so that time, location, device conditions, physical load, and health factors are not guessed. Gather the context in one compact message, use it only for the current conversation, and proceed when the user skips optional items.

## Privacy notice

Show this notice before the questions, in the selected language.

Chinese:

> 以下信息仅用于本次对话中的情景分析，不会上传到 GitHub、写入 Skill、发送给第三方，也不会用于统计或推广。你可以跳过任何非必要项目；城市只需填写市级，不需要详细地址。

English:

> This information is used only for scenario analysis in the current conversation. It is not uploaded to GitHub, written into the Skill, sent to third parties, or used for analytics or promotion. You may skip any optional item; provide only a city-level location, never a detailed address.

Do not proceed as if the user consented to data collection. The notice explains purpose and boundaries; it is not a request for sensitive data beyond the task.

## Ask once

After language selection and before the first substantive event analysis, ask once in the selected language. Do not interrupt installation help, greetings, or requests that do not need analysis.

Chinese compact form:

```text
为了更贴合你的情况，请一次性回复以下信息（均可跳过）：
1. 所在城市（仅市级）
2. 正在使用的 Agent 软件及版本
3. 是否允许读取当前日期、时间和时区；若不允许，请直接提供
4. 是否允许读取当前系统环境；若不允许，请提供设备类型和操作系统
5. 年龄
6. 身高和体重
7. 健康状况（仅填写与活动相关的疾病、过敏、用药或行动限制）
```

English compact form:

```text
To make the analysis more relevant, reply once with the following (all optional):
1. City (city level only)
2. Agent application and version
3. May I read the current date, time, and timezone? If not, provide them.
4. May I read the current system environment? If not, provide device type and operating system.
5. Age
6. Height and weight
7. Health factors relevant to the activity (conditions, allergies, medication, or mobility limits only)
```

Do not ask for a street address, precise coordinates, ID number, phone number, workplace, account credentials, or unrelated medical history.

## Capability handling

Use the user's Agent answer to explain what can be checked automatically.

| Need | If the Agent supports it | If it does not |
|---|---|---|
| Real-time date/time | Read the current date, time, and timezone with an available tool or system command; state the observed value and timezone. | Ask the user for the current date, time, and timezone; do not guess. |
| System environment | Read basic OS, device class, runtime, and relevant constraints. Never expose hostname, username, serial number, MAC address, IP address, or other identifiers. | Ask for device type and operating system only. |
| City context | Use it for local weather, daylight, transport, emergency, or jurisdiction context when reliable tools are available. | State that local conditions could not be verified and use conditional scenarios. |
| Age, height, weight | Use only the values the user supplied. Adjust physical-load, recovery, and age-related considerations when relevant. | Do not infer them from writing style, avatar, voice, or other personal data. |
| Health status | Apply only user-stated conditions that materially affect the scenario. Avoid diagnosis and preserve dignity. | Do not assume a condition from age, weight, or appearance. |

If the user names an Agent whose capabilities are unknown, say so and ask permission to attempt the relevant read. Do not claim a capability merely because the application is popular. If a tool call fails, ask the user rather than inventing the current time or environment.

## Using the context

- Use the exact date/time and timezone when evaluating opening hours, transport, weather, tides, deadlines, or daylight.
- Use city-level location for local conditions and jurisdiction, not for identifying the user.
- Use age, height, weight, and health only when they change the risk mechanism, such as physical exertion, heat, fatigue, mobility, medication, or recovery.
- Do not calculate BMI, diagnose, or give treatment instructions unless explicitly requested; even then, frame it as general information.
- If the user skips everything, continue with explicit assumptions and lower confidence. Never block the analysis.
- Do not repeat the full profile before every table. Mention only the relevant factor, such as “given the stated knee injury”.
- If context changes during the conversation, ask only for the changed item.

## Privacy boundaries

- Keep the profile transient in the current conversation. Do not write it into `SKILL.md`, `README`, `language.json`, repository files, memory files, logs, generated JSON, HTML metadata, URLs, query strings, examples, screenshots, or commits.
- Do not upload any user profile to a remote service. A web search for city-level weather should include only the city, not age, health, device, or precise location.
- Do not place health details in the generated HTML. Reflect relevant limitations in scenario wording without embedding the user's full profile.
- If the user asks to remember the profile locally, explain the tradeoff, obtain explicit permission, and save only to a user-chosen local path outside the repository. Never commit it.
- If the user asks to delete the context, stop using it immediately and do not repeat it.
- Do not include user information in feedback, public posts, issues, or Git commits.

## Response after intake

Briefly confirm what was received without repeating sensitive details:

- Chinese: “已收到。信息只用于本次分析；未提供的项目我会按假设处理。”
- English: “Received. I will use this only for the current analysis and treat missing items as assumptions.”

Then continue with the risk response and the central disclaimer.
