# ai-ui-testing-lab

SDET AI UI 测试框架实战 Lab —— 系统对比主流 UI 测试框架及其 AI 辅助能力。

## 当前进度

| 项目 | 状态 | 测试通过 |
|------|:----:|:--------:|
| web-playwright | ✅ 完成 | 3/3 |
| web-selenium | ✅ 完成 | 3/3 |
| app-appium | ⏳ 待实现 | - |
| web-midscene | ⏳ 待实现 | - |
| web-cypress | ⚪ 备选 | - |
| web-wdio | ⚪ 备选 | - |

## 框架对比速览

| 维度 | Playwright | Selenium | Appium | Midscene.js |
|------|:----------:|:--------:|:------:|:-----------:|
| AI 能力 | ⭐⭐⭐⭐⭐ MCP | ⭐⭐ Healenium | ⭐ | ⭐⭐⭐⭐ 纯视觉 |
| 使用率 | 3864万/周 | 206万/周 | 92万/周 | 新兴 |
| 开源 | ✅ Apache 2.0 | ✅ Apache 2.0 | ✅ Apache 2.0 | ✅ MIT |
| 语言 | Python/JS | 全语言 | Python/JS | JS |
| 平台 | Web | Web | 移动端 | Web/移动/桌面 |

## 快速开始

```bash
# 克隆
git clone https://github.com/xiaotrong/ai-ui-testing-lab.git
cd ai-ui-testing-lab

# Playwright
cd projects/web-playwright && pip install -r requirements.txt
python -m playwright install chromium
pytest tests/ -v

# Selenium
cd projects/web-selenium && pip install -r requirements.txt
pytest tests/ -v
```

## 项目结构

```
├── AGENTS.md            # AI 规则手册
├── projects/
│   ├── web-playwright/  # Playwright + MCP AI Agent
│   ├── web-selenium/    # Selenium + Healenium 自愈
│   ├── app-appium/      # Appium 移动端
│   └── web-midscene/    # Midscene.js 纯视觉 AI
├── shared/              # Python 公共工具
└── docs/                # 架构文档 & 对比报告
```
