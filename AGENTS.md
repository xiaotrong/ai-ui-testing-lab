# ai-ui-testing-lab — AI Rules

## 项目定位
SDET 实战 Lab：对比主流 UI 测试框架的 AI 辅助能力。
测试目标：**用户自己的项目（后续指定）**，当前占位 Demo 为 SauceDemo。

## 目录结构速查

```
projects/
├── web-playwright/    # [Python] Playwright + MCP AI Agent
├── web-selenium/      # [Python] Selenium + Healenium 自愈
├── app-appium/        # [Python] Appium 移动端（待实现）
├── web-midscene/      # [JS] Midscene.js 纯视觉 AI（待实现）
├── web-cypress/       # [JS] 备选：Cypress + Studio AI
└── web-wdio/          # [JS] 备选：WebdriverIO + Percy
shared/                # Python 公共工具库
docs/                  # 对比报告 & 架构文档
```

## 框架优先级

| 优先级 | 框架 | 语言 | 理由 |
|:------:|------|:----:|------|
| 🔴 ① | Playwright + MCP | Python | 使用率第一（npm 3864万/周），AI Agent 最强 |
| 🔴 ② | Selenium + Healenium | Python | 企业标配，唯一开源自愈方案 |
| 🔴 ③ | Appium | Python | 移动端唯一选择 |
| 🔴 ④ | Midscene.js | JS | 字节开源，纯视觉 AI，跨平台 |
| ⚪ 备选 | Cypress / WebdriverIO | JS | 核心做完后再看 |

## 如何运行

```bash
# Playwright（用本地 Chrome）
cd projects/web-playwright
pip install -r requirements.txt
python -m playwright install chromium  # 首次需下载浏览器
pytest tests/ -v

# Selenium（自动管理 ChromeDriver）
cd projects/web-selenium
pip install -r requirements.txt
pytest tests/ -v
```

## 关键约定

1. **Demo 网站可替换** — 当前用 SauceDemo 占位，后续统一换为用户真实项目
2. **Python 为主，JS 为辅** — web-playwright/selenium/appium 用 Python，midscene/cypress/wdio 用 JS
3. **Page Object 模式** — 所有框架统一用 pages/ 目录做页面对象封装
4. **测试结构** — conftest.py 放 fixture，tests/ 放用例，每个框架 3+ 个基础用例起步
5. **不要提交** — __pycache__、reports/、.venv/、.env（已在 .gitignore）
6. **AGENTS.md 控制在 100 行以内** — 详细文档放 docs/

## 深入文档

- 架构设计 → [docs/architecture.md](./docs/architecture.md)（待创建）
- 框架对比报告 → [docs/framework-comparison.md](./docs/framework-comparison.md)（待创建）
