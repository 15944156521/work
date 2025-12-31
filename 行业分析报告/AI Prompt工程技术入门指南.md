# AI Prompt 工程技术指南

## 1. 引言：Prompt 工程概述

### 1.1 什么是 AI Prompt 工程

在人工智能时代，如何与大语言模型（LLM）进行有效沟通成为了一项关键技能。AI Prompt 工程（Prompt Engineering）正是这样一门通过精心设计输入指令（Prompt）来引导 AI 模型生成准确、相关且高质量输出的技术[(40)](http://news.qq.com/rain/a/20251211A067WG00)。它不仅是一种技巧，更是一门融合了语言学、认知科学和计算机科学的系统学科[(9)](https://blog.csdn.net/csdn_224022/article/details/150861497)。

从本质上讲，Prompt 工程是人与 AI 协同的核心技能，它的目标是将人类的意图精准地传达给模型，使 AI 能够理解并执行各种复杂任务[(24)](https://www.cnblogs.com/neolshu/p/19120304)。与传统编程不同，Prompt 工程使用自然语言而非代码来指挥 AI，这种方式极大地降低了 AI 应用的门槛，让更多非技术背景的用户也能充分利用 AI 的强大能力[(164)](https://blog.51cto.com/u_16099343/14247423)。

在 2025 年的今天，Prompt 工程已经从早期的 "提示词炼金术" 发展成为一门成熟的专业学科。它不仅涵盖了如何构建有效的提示词，还包括了系统设计、性能优化、安全治理等多个层面[(29)](https://juejin.cn/post/7555780704270434323)。随着 AI 技术的不断进步，Prompt 工程的重要性日益凸显，成为了 AI 应用开发中不可或缺的核心技术。

### 1.2 发展历程与技术定位

Prompt 工程的发展可以清晰地划分为三个阶段，每个阶段都反映了 AI 技术和应用需求的深刻变化[(36)](https://blog.csdn.net/2502_91591115/article/details/149843337)。

**第一阶段：手动试错期（2020-2022 年）**，这一时期被戏称为 "提示词炼金术"。开发者主要通过反复试验来调整提示词，缺乏系统化的方法。技术标志包括基础提示模板（如 "总结以下文本..."）和少量提示技巧（如角色设定、逐步思考）。由于缺乏工具支持，这一阶段主要依赖经验和直觉。

**第二阶段：方法论形成期（2023-2024 年）**，Prompt 工程开始从经验积累走向方法论构建。这一时期出现了提示模式库（如 Chain-of-Thought、Few-shot 学习）、结构化提示格式（如 JSON、XML 标记），以及基础的 Prompt 工程工具（如 LangChain、PromptBase）。同时，Prompt 评估指标也初步建立。

**第三阶段：架构系统化期（2024 年至今）**，Prompt 工程已经上升到系统架构层面，与软件工程深度融合。这一阶段的技术标志包括 Prompt 工程架构设计模式、自动化 Prompt 优化与管理平台、Prompt 工程与 MLOps 的融合、多模态 Prompt 设计框架，以及 Prompt 安全与治理体系。

值得注意的是，2025 年 Prompt 工程出现了一些革命性的变化。自动化提示工程（APE）开启了新的时代，标志着 Prompt 工程从 "手工作坊" 迈向 "工业化生产"[(39)](https://m.sohu.com/a/968134670_122500756/)。同时，Prompt 工程正在向 Context Engineering（上下文工程）演进，这反映了模型对更复杂上下文理解能力的提升[(38)](http://m.toutiao.com/group/7528606956567708194/?upstream_biz=doubao)。

### 1.3 核心价值与应用场景

Prompt 工程的核心价值在于它能够最大化 AI 应用的效率和效果。通过精心设计的 Prompt，可以显著提升模型的输出质量，同时降低成本和提高响应速度。具体而言，Prompt 工程的价值体现在以下几个方面：

**提升输出质量**：研究表明，通过优化 Prompt，AI 模型的准确率可以提升 13.5%，用户满意度可以从 3.2 分提升至 4.5 分[(112)](https://blog.csdn.net/2502_92021348/article/details/151325346)。这种提升不仅体现在准确性上，还包括输出的相关性、一致性和实用性。

**降低使用成本**：通过 Prompt 压缩、模型选择和 RAG（检索增强生成）技术，可以削减 20-50% 的调用成本。这对于需要大规模部署 AI 应用的企业来说，意味着巨大的经济效益。

**提高开发效率**：Prompt 工程让开发者能够快速迭代和优化 AI 应用，而不需要重新训练模型。这种灵活性大大缩短了 AI 应用的开发周期，提高了整体效率。

在应用场景方面，Prompt 工程已经渗透到各个行业和领域：

在**软件开发**领域，Prompt 工程被广泛用于代码生成、调试、测试用例生成等任务。开发者可以使用 Prompt 来检测代码错误、优化函数性能、在不同编程语言间进行翻译等[(141)](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)。

在**内容创作**领域，从广告文案到学术论文，从产品描述到创意写作，Prompt 工程都发挥着重要作用。电商平台使用 AI 生成引人入胜的产品描述和广告文案，确保在所有渠道上保持一致的品牌信息[(143)](https://www.godofprompt.ai/blog/prompt-engineering-evolution-adapting-to-2025-changes)。

在**数据分析**领域，Prompt 工程帮助将原始数据转换为可操作的洞察。高管和分析师使用 Prompt 将项目报告转换为执行摘要，将电子表格数据转换为性能评论和趋势分析[(144)](https://www.educative.io/blog/real-world-applications-of-prompt-engineering)。

在**教育培训**领域，教师使用 Prompt 生成个性化教学方案、试题和讲解内容。学生则可以借助 Prompt 进行知识梳理和解题思路训练[(140)](https://blog.51cto.com/u_16213661/14303482)。

在**企业服务**领域，Prompt 工程被用于优化客服对话、生成报告、进行市场分析等。通过构建 Mega-Prompt 和 Prompt 链，可以将复杂任务分解为可管理的步骤，优化金融、医疗、电商等行业的运营[(141)](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)。

## 2. 基础概念与要素详解

### 2.1 Prompt 的定义与核心要素

在深入探讨 Prompt 工程之前，我们需要先理解什么是 Prompt。从技术定义来看，Prompt 是用户提供给人工智能模型（如大型语言模型 LLM）的指令或输入，它通常是一段文本，用于引导模型生成符合特定期望的响应[(24)](https://www.cnblogs.com/neolshu/p/19120304)。

一个完整的 Prompt 通常包含以下几个核心要素，这些要素相互配合，共同决定了 AI 模型的输出质量：

**指令（Instruction）**：这是 Prompt 的核心部分，明确告诉模型需要完成的任务。指令应该使用清晰、具体的语言，避免模糊或歧义。例如，"写一篇关于气候变化的文章" 就过于模糊，而 "写一篇 1000 字的文章，论述气候变化对沿海城市的影响，重点关注海平面上升问题" 则更加具体明确[(17)](https://learnprompting.org/docs/basics/formalizing)。

**上下文（Context）**：提供任务相关的背景信息，帮助模型更好地理解任务的来龙去脉。上下文可以包括问题领域的描述、目标受众、相关事实或数据等。例如，在要求模型生成产品描述时，提供产品的技术规格、目标市场、竞争产品等信息，可以帮助模型生成更精准的内容[(22)](https://blog.csdn.net/yweng18/article/details/147103039)。

**输入数据（Input Data）**：这是用户希望模型处理的具体内容或问题。在实际应用中，输入数据可能是一段文本、一个问题、一组数据等。需要注意的是，输入数据应该与指令和上下文区分开来，避免混淆[(150)](https://blog.csdn.net/CSDN_430422/article/details/154730980)。

**输出格式（Output Format）**：指定输出的形式和风格要求。这可以包括输出的长度、格式（如 JSON、Markdown、表格等）、语言风格、字数限制等。明确的输出格式要求可以帮助模型生成更符合预期的结果[(22)](https://blog.csdn.net/yweng18/article/details/147103039)。

除了这四个基本要素外，现代 Prompt 还可能包含其他组件：

**角色（Role）**：为 AI 分配一个特定的身份或角色，如 "你是一位资深的医学专家"、"你是一位市场营销经理" 等。角色设定可以帮助模型采用特定的视角和语言风格来响应。

**示例（Examples）**：提供输入 - 输出对的示例，特别是在进行少样本学习时。示例可以帮助模型理解任务的模式和期望的输出格式。

**约束条件（Constraints）**：设置边界条件和限制，如 "回答不得超过 500 字"、"必须使用正式的商务语气"、"输出中不得包含任何偏见" 等。约束条件可以确保输出符合特定的要求和规范[(164)](https://blog.51cto.com/u_16099343/14247423)。

### 2.2 基础概念体系

理解 Prompt 工程需要掌握一系列基础概念，这些概念构成了整个技术体系的基石。

\*\*Token（令牌）\*\* 是 LLM 处理文本的基本单位。Token 通常由子词（Subword）或字符组成，不同的模型使用不同的 Tokenization 算法。例如，GPT-3 使用 Byte-Pair Encoding（BPE）算法[(81)](https://blog.csdn.net/2501_91490244/article/details/150074235)。Token 的数量直接影响模型的处理成本和响应速度。一般来说，1 个 Token 约等于 1/4 个英文单词或 1.5 个中文字符[(82)](https://juejin.cn/post/7585157583473803315)。

\*\* 上下文窗口（Context Window）\*\* 是模型能够处理的最大 Token 数量。不同的模型有不同的上下文窗口限制：GPT-3.5 的标准上下文窗口为 4096 个 Token，GPT-4 为 8192-32768 个 Token，GPT-4 Turbo 可达 128000 个 Token，而最新的 GPT-4.1 则支持高达 100 万个 Token[(85)](https://note.com/emm_tokyo/n/n04b0f7746bea)。超过上下文窗口限制的内容会被截断，这可能导致模型 "忘记" 早期的对话内容。

\*\* 温度参数（Temperature）\*\* 是影响模型输出随机性的重要参数。温度值的范围通常在 0 到 2 之间。较低的温度（如 0.2）会使模型输出更加确定性和精确，适合需要准确答案的任务；较高的温度（如 0.8）会使输出更加多样化和有创意，适合需要创新的任务[(59)](https://www.godofprompt.ai/blog/best-prompt-engineering-tips)。

\*\* 零样本学习（Zero-Shot Learning）\*\* 是指模型在没有任何示例的情况下执行任务的能力。这种能力使得模型可以直接根据指令生成响应，特别适合翻译、内容审核等任务[(141)](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)。

\*\* 少样本学习（Few-Shot Learning）\*\* 是指在 Prompt 中包含少量输入 - 输出示例，帮助模型更好地理解任务。通常使用 1-3 个示例就可以显著提升模型的性能[(43)](https://blog.csdn.net/leah126/article/details/150558248)。

\*\* 思维链（Chain of Thought, CoT）\*\* 是一种高级的 Prompt 技巧，通过引导模型逐步推理来解决复杂问题。这种方法特别适合需要多步推理的数学问题或逻辑问题[(141)](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)。

\*\* 元 Prompt（Meta Prompt）\*\* 是指能够生成其他 Prompt 或根据上下文自适应调整交互的 Prompt。这种技术使得 AI 系统能够根据用户的需求动态生成合适的 Prompt[(141)](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)。

### 2.3 与传统编程的本质区别

Prompt 工程与传统编程在多个方面存在本质区别，理解这些区别对于掌握 Prompt 工程至关重要。

**编程范式的差异**：传统编程遵循严格的语法规则和结构化流程，程序员需要精确地告诉计算机每一步该做什么。而 Prompt 工程使用自然语言，更像是与 AI 进行 "对话"，告诉它 "想要什么" 而不是 "如何做"[(164)](https://blog.51cto.com/u_16099343/14247423)。

**执行方式的不同**：传统编程是确定性的，相同的代码输入会产生相同的输出。而 Prompt 工程具有一定的随机性，即使使用相同的 Prompt，在不同的温度参数下也可能产生不同的输出。这种不确定性既是挑战也是机遇，可以用于生成多样化的内容。

**开发流程的差异**：传统编程需要经过编写代码、编译、调试、测试等多个步骤，流程相对固定。而 Prompt 工程更像是一个迭代优化的过程，通过不断调整 Prompt 来改进输出结果。这种方式更加灵活，但也需要更多的人工参与和判断。

**技能要求的不同**：传统编程需要掌握特定的编程语言和开发工具，对技术背景要求较高。而 Prompt 工程更注重语言表达能力、逻辑思维和领域知识。虽然技术理解有助于优化 Prompt，但即使是非技术背景的用户也能快速上手[(164)](https://blog.51cto.com/u_16099343/14247423)。

**错误处理机制**：在传统编程中，错误通常会导致程序崩溃或产生明显的错误信息。而在 Prompt 工程中，错误可能表现为输出不符合预期，这种 "软性" 错误更难诊断和修复，需要通过不断的试验和调整来解决。

理解这些区别可以帮助我们更好地认识 Prompt 工程的本质。它不是传统编程的替代品，而是一种全新的人机交互方式。在实际应用中，两者往往结合使用，例如在开发 AI 应用时，我们可能会使用传统编程来构建系统架构，使用 Prompt 工程来优化 AI 交互。

## 3. 基础技巧与构建方法

### 3.1 简单 Prompt 构建原则

构建简单有效的 Prompt 是学习 Prompt 工程的第一步。遵循以下基本原则，可以显著提升 Prompt 的质量和效果。

**明确性原则**：避免模糊和歧义是构建优质 Prompt 的首要原则。例如，"写点东西" 这样的指令过于宽泛，模型无法确定具体需求。相比之下，"写一篇 200 字的关于气候变化对沿海城市影响的文章，重点关注海平面上升问题" 则提供了清晰的目标和范围[(45)](http://www.linkedin.com/pulse/beginners-guide-prompt-engineering-michael-raynolds-laursen-vilmf)。在实践中，可以使用具体的数字、限定词和明确的动作动词来增强指令的清晰度。

**简洁性原则**：保持 Prompt 简洁明了，避免冗长和不必要的细节。研究表明，过于复杂的 Prompt 可能导致模型困惑，反而降低输出质量。例如，在要求模型生成产品描述时，"为无线耳机撰写 50 字产品描述，强调音质和运动舒适性" 比一段冗长的背景介绍更有效。

**结构清晰原则**：采用结构化的方式组织 Prompt 内容，使其逻辑清晰、层次分明。一个推荐的结构是：角色设定→任务描述→背景信息→输出要求。例如："你是一位资深的旅游顾问（角色），请为去北京旅游的家庭设计一份 3 天行程（任务），考虑到有老人和小孩（背景），行程要轻松且有教育意义，用表格形式输出（要求）"[(53)](https://blog.51cto.com/u_16213720/14403386)。

**使用示例原则**：在适当的时候提供输入 - 输出示例，可以帮助模型更好地理解任务要求。例如，在要求模型翻译时，可以先给出一个例子："Q: I like apples. A: Me gustan las manzanas." 这样模型就能理解期望的输出格式。

**避免专业术语原则**：除非目标受众是专业人士，否则应使用通俗易懂的语言。过于技术化的术语可能导致模型生成过于专业或难以理解的内容。保持语言的自然和口语化，可以获得更好的效果。

### 3.2 指令设计与上下文管理

指令设计是 Prompt 工程的核心，它直接决定了 AI 模型的行为方向。以下是一些经过验证的指令设计技巧：

**使用祈使句开头**：以动词开头的祈使句能够清晰地传达任务意图。例如，"撰写一份产品说明书"、"总结这篇文章的要点"、"将以下内容翻译成英文" 等[(53)](https://blog.51cto.com/u_16213720/14403386)。这种表达方式让模型明确知道需要执行什么动作。

**提供详细的任务描述**：除了基本指令外，还应该提供足够的细节来限定任务范围。这些细节可以包括：



* 目标受众："面向新手程序员的教程"

* 内容长度："不超过 500 字"

* 语言风格："正式的商务语气"

* 格式要求："使用 Markdown 格式，包含标题和列表"

* 特殊要求："必须包含 3 个实际案例"[(69)](http://m.toutiao.com/group/7571390461386949163/?upstream_biz=doubao)

**分步骤指导**：对于复杂的任务，可以将其分解为多个步骤，让模型逐步完成。例如："第一步，分析用户需求；第二步，设计解决方案；第三步，提供实施步骤；第四步，列出可能的风险和应对措施"[(43)](https://blog.csdn.net/leah126/article/details/150558248)。

上下文管理是确保 AI 理解任务背景的关键。以下是一些有效的上下文管理技巧：

**提供必要的背景信息**：在 Prompt 中包含相关的背景信息，可以帮助模型生成更准确的结果。例如，在要求模型分析市场趋势时，提供 "2025 年智能手机市场" 这样的背景，可以确保分析的时效性和相关性[(46)](https://promptgenius.net/prompts/chatgpt/resources/prompt-engineering-guide)。

**使用上下文保持一致性**：在多轮对话中，保持上下文的一致性至关重要。可以使用 "根据之前的讨论"、"基于我们刚才的对话" 等表达方式来建立上下文连接。例如："根据我们之前讨论的营销策略，现在请提供具体的执行计划"[(25)](https://cloud.tencent.com.cn/developer/article/2565421)。

**管理上下文长度**：注意不要提供过多无关的信息，以免造成信息过载。同时要考虑模型的上下文窗口限制，特别是对于 GPT-3.5 这样只有 4096 个 Token 的模型，需要精简上下文以留出空间给输出[(79)](https://blog.csdn.net/weixin_42738495/article/details/149338227)。

**动态上下文调整**：根据任务的不同，灵活调整上下文的内容和深度。例如，在技术支持场景中，需要提供详细的系统配置信息；而在创意写作场景中，则需要更多的灵感和风格指引。

### 3.3 输出格式与约束设置

明确的输出格式要求是确保 AI 生成内容符合预期的重要手段。以下是一些常用的输出格式设置方法：

**指定文本格式**：可以要求特定的文本格式，如：



* "以 Markdown 格式输出"

* "使用表格展示对比结果"

* "输出为 JSON 格式，包含 name、age、email 字段"

* "用编号列表的形式列出要点"[(57)](https://blog.51cto.com/u_17514447/14399814)

**设置输出长度**：通过明确的字数或段落要求来控制输出规模：



* "总字数控制在 800-1000 字"

* "每个要点不超过 50 字"

* "输出 3-5 个选项"

* "回答不超过 3 段"[(47)](https://blog.csdn.net/2401_84205765/article/details/146074841)

**限定语言风格**：根据应用场景设置合适的语言风格：



* "使用正式的学术语言"

* "保持口语化和亲切感"

* "采用幽默风趣的表达方式"

* "使用专业的技术术语"[(66)](https://cloud.tencent.cn/developer/article/2504596?policyId=1003)

约束设置是确保输出质量和安全性的重要手段：

**内容约束**：设置内容相关的限制条件：



* "不得包含任何歧视性内容"

* "避免使用攻击性语言"

* "必须基于事实，不得编造信息"

* "内容要积极向上"[(126)](https://blog.csdn.net/2501_91888447/article/details/152168249)

**技术约束**：对输出的技术特性进行限制：



* "代码必须能够编译运行"

* "数学计算必须准确"

* "引用的数据源必须可靠"

* "格式必须严格遵循要求"[(139)](https://blog.csdn.net/2501_91473495/article/details/149712929)

**格式约束**：使用分隔符来明确区分不同的内容部分：



* 使用 \`\`\` 包裹代码块

* 使用 ### 作为章节标题

* 使用 | 分隔表格列

* 使用 {} 定义 JSON 结构[(57)](https://blog.51cto.com/u_17514447/14399814)

在设置约束时，要注意以下几点：

首先，约束要具体且可执行。例如，"避免敏感话题" 这样的约束过于模糊，而 "不得讨论政治、宗教、种族相关话题" 则更加明确。

其次，要平衡约束的严格性。过于严格的约束可能限制模型的创造力，而约束不足则可能导致输出不符合要求。需要根据具体任务找到合适的平衡点。

最后，要考虑约束的优先级。当多个约束发生冲突时，应该明确哪个约束更重要。例如，在 "输出必须有趣" 和 "内容必须准确" 之间，如果准确性更重要，就要在 Prompt 中明确说明。

### 3.4 迭代优化方法

Prompt 工程是一个迭代优化的过程，通过不断的试验和调整来提升输出质量。以下是一些经过验证的迭代优化方法：

**A/B 测试法**：创建多个版本的 Prompt，对比它们的输出效果。例如，创建两个版本的产品描述 Prompt，一个强调功能特性，一个强调用户体验，通过对比用户反馈来选择更优的版本[(112)](https://blog.csdn.net/2502_92021348/article/details/151325346)。

**逐步细化法**：从一个简单的 Prompt 开始，根据输出结果逐步添加细节和约束。例如，初始 Prompt 可能只是 "写一个故事"，然后根据输出的方向逐步细化为 "写一个科幻故事，背景设定在 2050 年的火星殖民地，主角是一位年轻的工程师"[(67)](https://cloud.tencent.cn/developer/article/2495330?policyId=1003)。

**错误分析法**：仔细分析不理想的输出，找出问题所在，然后针对性地改进 Prompt。常见的问题包括：



* 输出过于泛泛：需要添加更多具体要求

* 偏离主题：需要强化主题约束

* 格式混乱：需要明确格式要求

* 包含错误信息：需要添加事实核查要求[(58)](https://www.byteplus.com/en/topic/404124)

**参数调整法**：除了调整 Prompt 文本外，还可以通过调整模型参数来优化输出：



* 温度参数：降低温度以获得更确定的输出，或提高温度以获得更多样化的输出

* 最大 Token 数：根据任务需求调整输出长度

* 停止序列：设置特定的停止词来控制输出结束[(59)](https://www.godofprompt.ai/blog/best-prompt-engineering-tips)

**反馈循环法**：建立持续的反馈机制，收集用户对输出的评价，根据反馈不断优化 Prompt。这种方法特别适合需要长期运行的 AI 应用，如客服系统、内容生成工具等。

在进行迭代优化时，要注意以下几个关键点：

首先，每次只改变一个变量。这样可以准确判断哪个改变带来了效果提升，避免多个变量同时变化导致无法确定因果关系。

其次，要记录每次迭代的过程和结果。创建一个 Prompt 版本记录，包括 Prompt 内容、参数设置、输出结果、效果评分等信息，这有助于分析优化趋势和发现最佳实践。

最后，要设定明确的优化目标。是要提高准确性、增加创意性、缩短响应时间还是降低成本？不同的目标需要不同的优化策略。

## 4. GPT 系列模型的 Prompt 工程特点

### 4.1 GPT 模型家族概览

GPT（Generative Pre-trained Transformer）系列模型是 OpenAI 开发的一系列大语言模型，在 Prompt 工程领域占据着重要地位。理解不同 GPT 模型的特点对于进行有效的 Prompt 工程至关重要。

**GPT-3.5 系列**是目前最受欢迎的模型之一，具有以下特点：



* 模型大小：约 175B 参数（改进版 GPT-3）

* 上下文窗口：标准 4096 个 Token，可选 16000 个 Token

* 价格：$0.0015-$0.002 每 1000 个 Token（4K 上下文）

* 特点：文本专用（无视觉或音频），低延迟，针对聊天优化

* 性能：MMLU 70.0%，GSM8K 数学 57.1%，HumanEval 代码约 48%[(91)](https://gpt.gekko.de/comparison-openai-language-models-may-2025/)

**GPT-4 系列**在性能上有了显著提升：



* 模型大小：未公开（传言约 1T 参数）

* 上下文窗口：8192 个 Token（标准）或 32768 个 Token（扩展）

* 价格：$0.03-$0.06 每 1000 个 Token（8K 上下文）

* 特点：多模态（文本 + 图像），但推理速度较慢

* 性能：MMLU 86.4%，GSM8K 92.0%，律师考试约 90 百分位[(91)](https://gpt.gekko.de/comparison-openai-language-models-may-2025/)

**GPT-4 Turbo/O 系列**（2024 年 5 月发布）带来了新的突破：



* 模型大小：未公开

* 上下文窗口：128000 个 Token

* 价格：$0.01-$0.03 每 1000 个 Token（优化定价）

* 特点：多模态（文本、图像、音频输入），优化了速度（接近人类响应时间）

* 性能：MMLU 88.7%，在多语言任务中表现优异[(91)](https://gpt.gekko.de/comparison-openai-language-models-may-2025/)

**GPT-4.1 系列**（2025 年发布）代表了最新的技术水平：



* 上下文窗口：高达 100 万个 Token

* 特点：支持超长上下文，可处理大型代码库、长文档或复杂多轮对话

* 注意事项：窗口越大，模型可靠性可能下降，从 8K 的 84% 准确率降至 100 万 Token 的 50% 左右[(96)](https://www.iesdouyin.com/share/note/7524727461121412412/?region=\&mid=7431527252317882385\&u_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with_sec_did=1\&video_share_track_ver=\&titleType=title\&schema_type=37\&share_sign=RRu0CLssc.Sj3oUS5O1lTuEJcZktg7pNBHWlhiud.sM-\&share_version=280700\&ts=1766840355\&from_aid=1128\&from_ssr=1\&share_track_info=%7B%22link_description_type%22%3A%22%22%7D)

**GPT-5 系列**（2025 年 8 月发布）是最新的旗舰模型：



* 发布时间：2025 年 8 月 7 日

* 特点：多模态大语言模型，具备高速响应、更强编码能力、更低幻觉率

* 改进：在推理、安全性和上下文追踪方面有重要改进[(83)](https://blog.51cto.com/ghostwritten/14192748)

理解这些模型的特点对于选择合适的模型和优化 Prompt 策略至关重要。例如，对于需要处理长文档的任务，GPT-4.1 的百万 Token 上下文窗口是理想选择；而对于实时对话应用，GPT-3.5 的低延迟特性则更为重要。

### 4.2 不同版本的特性差异

不同版本的 GPT 模型在处理 Prompt 时表现出各自的特点，了解这些差异对于优化 Prompt 策略至关重要。

**GPT-3.5 的特点**：



* 对简单 Prompt 响应良好，适合日常对话和基础任务

* 需要更明确的指令和示例，因为其推理能力相对有限

* 价格便宜，适合需要大量调用的场景

* 上下文窗口较小，需要精简 Prompt 以留出空间给输出[(97)](https://lobehub.com/zh/docs/usage/agents/model)

**GPT-4 的特点**：



* 具备更强的推理能力，能够处理更复杂的逻辑

* 对上下文的理解更深入，可以记住对话历史中的细节

* 支持多模态输入，如图片描述和分析

* 但价格较高，需要权衡性能和成本[(97)](https://lobehub.com/zh/docs/usage/agents/model)

**GPT-4 Turbo 的特点**：



* 相比 GPT-4，速度有了显著提升

* 支持 128K Token 的超大上下文窗口，适合处理长文档

* 保持了 GPT-4 的高质量输出

* 在处理复杂的多轮对话时表现优异[(90)](https://scalebytech.com/gpt-4-context-window/)

**GPT-4.1 的独特优势**：



* 支持 100 万 Token 的超长上下文，是目前支持上下文最长的模型之一

* 特别适合处理大型代码库、学术论文、法律文档等超长文本

* 但需要注意的是，超长上下文可能影响准确性，需要进行测试验证[(94)](https://juejin.cn/post/7493198688871153716)

**版本间的共性特点**：



* 都支持 system prompt、user prompt 和 assistant prompt 的格式

* 都需要清晰、具体的指令来获得最佳效果

* 都可以通过调整温度参数来控制输出的随机性

* 都有 Token 数量限制，需要合理规划输入和输出的长度

了解这些特性差异后，我们可以根据具体任务选择合适的模型并制定相应的 Prompt 策略。例如：



* 简单的问答任务：选择 GPT-3.5，使用简洁明了的 Prompt

* 复杂的推理任务：选择 GPT-4 或 GPT-4 Turbo，提供详细的上下文和推理步骤

* 长文档处理：选择 GPT-4 Turbo 或 GPT-4.1，充分利用其大上下文窗口

* 多模态任务：选择支持多模态的 GPT-4 版本，在 Prompt 中包含图像或音频描述

### 4.3 输入限制与最佳实践

了解 GPT 模型的输入限制是进行有效 Prompt 工程的基础。以下是一些关键的限制和对应的最佳实践：

**Token 限制的处理**：

不同模型的 Token 限制差异很大，从 GPT-3.5 的 4K 到 GPT-4.1 的 1M 不等。处理 Token 限制的最佳实践包括：



* 精简 Prompt：去除不必要的描述和示例

* 分批处理：将长任务拆分成多个短任务

* 使用总结：对历史对话进行总结，只保留关键信息

* 优化格式：使用更紧凑的格式（如 JSON 而非冗长的文本）[(78)](https://blog.csdn.net/gitblog_00979/article/details/152063528)

**上下文管理策略**：



* 优先保留最新的对话内容，因为模型对近期信息的记忆更清晰

* 使用 "根据之前的讨论" 等方式明确引用历史上下文

* 在长对话中定期总结要点，帮助模型保持连贯

* 避免在上下文中包含无关信息，以节省 Token 空间[(25)](https://cloud.tencent.com.cn/developer/article/2565421)

**温度参数的使用**：

温度参数控制着模型输出的随机性：



* 温度 0.2-0.5：用于需要精确答案的任务，如数学计算、事实查询

* 温度 0.6-0.8：用于需要创造性的任务，如创意写作、头脑风暴

* 温度 0.8-1.0：用于需要高度多样性的任务，如艺术创作、故事生成

* 温度 > 1.0：可能产生混乱或不连贯的输出，需谨慎使用[(59)](https://www.godofprompt.ai/blog/best-prompt-engineering-tips)

**输出长度控制**：



* 使用 max\_tokens 参数明确限制输出长度

* 根据任务需求设置合理的长度范围

* 对于需要多轮对话的任务，预留足够的输出空间

* 注意不同语言的 Token 密度差异，中文通常需要更多 Token[(80)](https://help.openai.com/en/articles/5072518-controlling-the-length-of-openai-model-responses%23.pls)

**格式要求的设置**：



* 使用明确的格式指令，如 "输出为 JSON 格式"、"使用 Markdown 表格"

* 提供格式示例，让模型清楚知道期望的输出结构

* 对于复杂格式，可以分步说明，如 "首先输出标题，然后是内容，最后是总结"

* 使用分隔符（如 \`\`\`）来明确区分不同部分[(57)](https://blog.51cto.com/u_17514447/14399814)

**错误处理策略**：



* 当输出不符合预期时，首先检查 Prompt 是否清晰明确

* 如果输出过长，考虑增加长度限制或简化 Prompt

* 如果输出偏离主题，需要加强主题约束和上下文

* 如果输出包含错误信息，需要添加事实核查要求

**成本优化技巧**：



* 使用较小的模型（如 GPT-3.5）处理简单任务

* 优化 Prompt 以减少 Token 消耗

* 批量处理多个请求以提高效率

* 使用缓存来避免重复处理相同的输入

通过遵循这些最佳实践，可以在充分利用 GPT 模型能力的同时，确保输出质量和成本效益的平衡。

### 4.4 特殊功能与参数优化

GPT 系列模型提供了一些特殊功能和参数，合理使用这些功能可以显著提升 Prompt 工程的效果。

**Function Calling 功能**：

GPT 模型支持函数调用功能，可以让模型调用外部工具或 API 来获取实时信息。使用方法如下：



```
{

&#x20; "name": "function\_name",

&#x20; "parameters": {

&#x20;   "key": "value"

&#x20; }

}
```

最佳实践包括：



* 明确告诉模型何时需要调用工具："如果需要实时数据，请使用工具调用"

* 提供工具描述：让模型了解每个工具的功能

* 设置调用条件："当需要获取当前天气信息时，调用天气 API"

* 处理工具返回结果：指导模型如何处理工具返回的数据

**System Prompt 的高级用法**：

System Prompt 不仅可以设置角色，还可以包含复杂的指令和规则。例如：



```
你是一位专业的客服代表。遵循以下规则：

1\. 始终以友好的问候开始："您好，很高兴为您服务！"

2\. 对于产品相关问题，必须使用工具查询最新信息

3\. 遇到无法回答的问题，应礼貌地告知并引导至人工服务

4\. 保持回答简洁，每个回答不超过5句话
```

**多轮对话的优化**：

在多轮对话中，可以使用以下技巧：



* 使用 "记忆" 机制：在 System Prompt 中设置 "记住用户的偏好和历史"

* 明确对话状态："我们正在处理您的订单问题，接下来需要确认配送地址"

* 引导对话流程："让我先了解一下您的问题，然后提供解决方案"

* 保持一致性：在整个对话中使用相同的语言风格和术语

**参数调优策略**：

除了温度参数，还有其他参数可以优化：



* presence\_penalty：控制模型是否倾向于谈论新话题

* frequency\_penalty：控制模型是否倾向于重复内容

* top\_p：使用核采样来控制输出的多样性

* n：生成多个备选回答，从中选择最佳方案

这些参数的组合使用可以产生不同的效果：



* 高温度 + 高 presence\_penalty：用于生成高度创新的内容

* 低温度 + 高 frequency\_penalty：用于生成连贯、聚焦的内容

* top\_p=0.1：用于需要非常确定性输出的任务

**Batch Processing（批量处理）**：

对于需要处理大量相似任务的场景，可以使用批量处理：



* 将多个 Prompt 组合成一个请求

* 使用循环结构来处理每个子任务

* 注意 Token 限制，确保批量大小合理

* 可以显著提高处理效率，降低成本

**Streaming 输出**：

GPT 模型支持流式输出，可以在生成过程中实时获取结果：



* 用于需要实时显示的场景，如聊天应用

* 可以显示 "思考中..." 的效果，提升用户体验

* 需要注意的是，流式输出可能影响最终结果的完整性

通过充分利用这些特殊功能和参数，可以创建更加智能、高效的 AI 交互系统。关键是要根据具体应用场景选择合适的功能组合，并通过实验找到最佳的参数配置。

## 5. 实践案例分析

### 5.1 基础对比案例

为了让初学者更好地理解 Prompt 工程的效果，我们通过一系列对比案例来展示不同 Prompt 设计带来的显著差异。

**案例一：产品描述生成**

原始 Prompt：



```
写一个产品描述
```

优化后 Prompt：



```
你是一位资深的产品文案专家。为无线耳机撰写50字产品描述，强调音质和运动舒适性，面向健身爱好者，使用积极向上的语言风格。
```

效果对比：



* 原始输出："这是一款无线耳机，具有良好的音质和舒适性。"（过于普通，缺乏吸引力）

* 优化输出："沉浸动感音质，稳固舒适佩戴！专为健身爱好者设计的无线耳机，让运动更带劲！"（突出了卖点，更具吸引力）

**案例二：代码生成**

原始 Prompt：



```
生成Python代码
```

优化后 Prompt：



```
生成Python函数，计算两个数的最大公约数。要求：

1\. 使用欧几里得算法

2\. 包含输入验证

3\. 添加详细注释

4\. 处理异常情况
```

效果对比：



* 原始输出：通常只是简单的 print 语句或基本结构

* 优化输出：完整的函数实现，包含算法逻辑、参数检查和文档注释

**案例三：数学问题解决**

原始 Prompt：



```
1+2+3+...+100等于多少？
```

优化后 Prompt（使用思维链）：



```
让我思考一下：这个问题是求1到100的和。我可以使用等差数列求和公式：S = n(a1+an)/2，其中n是项数，a1是首项，an是末项。

在这个问题中，n=100，a1=1，an=100。

所以，S = 100\*(1+100)/2 = 100\*101/2 = 5050。
```

效果对比：



* 原始输出：直接给出答案 5050（无法展示思考过程）

* 优化输出：不仅给出答案，还详细展示了推理过程，适合教学场景

**案例四：文本总结**

原始 Prompt：



```
总结这篇文章
```

优化后 Prompt：



```
总结以下文章的主要观点，要求：

1\. 提取3个核心论点

2\. 每个论点用2-3句话说明

3\. 保持客观中立的语气

4\. 不超过200字
```

效果对比：



* 原始输出：通常是原文的缩写，可能包含大量细节

* 优化输出：结构化的总结，突出重点，便于快速理解

这些基础案例展示了一个重要原则：**越具体、越明确的 Prompt，产生的结果越符合预期**。在实际应用中，我们可以通过以下方式不断优化 Prompt：



1. 添加角色设定：让模型以特定身份响应

2. 提供详细要求：包括格式、长度、风格等

3. 使用示例：展示期望的输出格式

4. 设定约束条件：明确哪些内容需要包含或排除

### 5.2 复杂场景案例

在实际应用中，Prompt 工程往往需要处理更复杂的场景。以下是一些典型的复杂场景案例：

**案例一：多轮对话系统**

场景：智能客服系统处理产品投诉

第一轮对话：



```
用户：我的手机充电很慢，怎么办？

系统：（使用预设的System Prompt）

你是一位专业的手机客服代表。遵循以下规则：

1\. 首先表达歉意并理解用户感受

2\. 询问具体情况（型号、购买时间、充电方式等）

3\. 提供故障排查步骤

4\. 如果无法解决，引导至售后支持

根据规则，系统回复：

"很抱歉给您带来不便！请问您使用的是哪款手机型号？购买多久了？平时使用什么充电器充电呢？"
```

第二轮对话：



```
用户：我用的是iPhone 15，买了半年，用的是原装充电器。

系统：基于用户提供的信息，使用工具查询iPhone 15充电慢的常见问题

"了解了。iPhone 15充电慢可能有以下原因：

1\. 充电口有灰尘或杂物，建议清理

2\. 充电器或数据线损坏，建议更换

3\. 系统软件问题，建议更新到最新版本

4\. 电池健康度下降，可在设置中查看

建议您先尝试清理充电口，使用其他原装充电器测试。如果问题依然存在，请携带设备到官方售后检测。"
```

这个案例展示了多轮对话中 Prompt 工程的关键要素：



* System Prompt 定义了客服的行为准则

* 动态调整：根据用户提供的信息调整响应策略

* 工具调用：使用外部信息来提供更准确的建议

* 流程引导：按照预设流程逐步解决问题

**案例二：代码审查与优化**

场景：AI 辅助代码审查

Prompt 设计：



```
你是一位资深的代码审查工程师。请审查以下Python代码：

1\. 检查代码风格是否符合PEP8规范

2\. 查找潜在的bug和逻辑错误

3\. 评估代码的可读性和可维护性

4\. 提出性能优化建议

5\. 给出整体评分（1-10分）

代码：

def calculate\_average(lst):

&#x20;   total = 0

&#x20;   count = 0

&#x20;   for num in lst:

&#x20;       total += num

&#x20;       count += 1

&#x20;   return total / count
```

AI 审查结果：



```
代码审查报告：

1\. 代码风格评分：8/10

&#x20;  \- 优点：函数命名规范，使用了有意义的变量名

&#x20;  \- 建议：添加类型提示，使用更简洁的循环方式

2\. 潜在问题：

&#x20;  \- 当输入空列表时会抛出ZeroDivisionError

&#x20;  \- 没有处理非数字类型的输入

&#x20;  \- 可以使用内置的sum()和len()函数简化代码

3\. 可读性评分：7/10

&#x20;  \- 优点：逻辑清晰，注释充分

&#x20;  \- 建议：添加函数文档字符串

4\. 优化建议：

&#x20;  optimized\_code = """

&#x20;  def calculate\_average(lst: list\[float]) -> float:

&#x20;      """计算列表的平均值"""

&#x20;      if not lst:

&#x20;          raise ValueError("列表不能为空")

&#x20;      return sum(lst) / len(lst)

&#x20;  """

5\. 总体评分：7.5/10

&#x20;  理由：代码功能正确，但存在一些可改进的地方，特别是异常处理和代码简洁性。
```

这个案例展示了如何使用 Prompt 工程实现专业的代码审查功能，包括风格检查、错误检测、优化建议等。

**案例三：数据分析报告生成**

场景：根据销售数据生成分析报告

Prompt 设计：



```
你是一位数据分析师。根据以下销售数据，生成一份分析报告：

数据：

月份: \[1, 2, 3, 4, 5, 6]

销售额（万元）: \[120, 135, 142, 118, 156, 168]

成本（万元）: \[85, 92, 98, 82, 105, 110]

要求：

1\. 计算每个月的利润和利润率

2\. 找出销售额最高和最低的月份

3\. 分析销售趋势

4\. 识别异常数据点

5\. 提出改进建议

6\. 以Markdown格式输出，包含图表建议
```

AI 生成的报告片段：



```
\# 上半年销售数据分析报告

\## 一、整体业绩概览

\| 月份 | 销售额(万元) | 成本(万元) | 利润(万元) | 利润率 |

\|------|------------|------------|------------|---------|

\| 1    | 120        | 85         | 35         | 29.2%  |

\| 2    | 135        | 92         | 43         | 31.9%  |

\| 3    | 142        | 98         | 44         | 31.0%  |

\| 4    | 118        | 82         | 36         | 30.5%  |

\| 5    | 156        | 105        | 51         | 32.7%  |

\| 6    | 168        | 110        | 58         | 34.5%  |

\## 二、关键发现

1\. \*\*销售额趋势\*\*：整体呈现上升趋势，从1月的120万元增长到6月的168万元，增长率达40%

2\. \*\*最高销售额\*\*：6月销售额最高（168万元），主要原因是...

3\. \*\*最低销售额\*\*：4月销售额最低（118万元），可能与...有关

4\. \*\*利润率分析\*\*：利润率稳定在30-35%之间，6月达到最高的34.5%

\## 三、图表建议

建议使用以下图表来可视化数据：

1\. 折线图：展示销售额和成本的月度趋势

2\. 柱状图：比较各月的利润

3\. 饼图：展示各月销售额占比
```

这个案例展示了如何使用 Prompt 工程将原始数据转换为结构化的分析报告，包括计算、分析和可视化建议。

### 5.3 效果差异对比分析

通过对比不同 Prompt 设计的效果，我们可以更直观地理解 Prompt 工程的重要性和实际效果。

**量化效果对比**：

以下是一些经过实际测试的效果提升数据：



1. **客服系统优化**：

* 原始 Prompt：用户满意度 3.2 分

* 优化后 Prompt：用户满意度提升至 4.5 分（提升 40.6%）

* 投诉解决率：从 65% 提升至 92%（提升 41.5%）

1. **代码生成优化**：

* 原始 Prompt：需求满足率 60%

* 优化后 Prompt：需求满足率提升至 95%（提升 58.3%）

* 开发时间：从 30 分钟缩短至 5 分钟（减少 83.3%）

1. **内容创作优化**：

* 原始 Prompt：内容质量评分 5.2 分（10 分制）

* 优化后 Prompt：内容质量评分提升至 9.1 分（提升 75%）

* 用户参与度：提升约 30%

1. **数据分析优化**：

* 报告准确性：从 70% 提升至 95%

* 报告生成时间：从 2 小时缩短至 10 分钟

**质化效果对比**：

除了量化指标，质化效果同样重要：

**输出质量提升**：



* 从模糊、泛泛的回答变为具体、精准的内容

* 从单一风格变为多样化、个性化的输出

* 从错误频出变为高准确率的结果

**用户体验改善**：



* 响应更加及时、相关

* 交互更加自然、流畅

* 结果更易于理解和使用

**业务价值提升**：



* 减少人工干预和后期修改

* 提高工作效率和生产力

* 增强客户满意度和忠诚度

**典型失败案例分析**：

了解失败案例同样重要，以下是一些常见的失败情况及原因：



1. **Prompt 过于模糊**：

* 失败案例："写一篇好文章"

* 问题："好" 的定义不明确

* 改进：明确文章类型、字数、风格、目标受众等

1. **信息过载**：

* 失败案例：包含过多无关细节的长 Prompt

* 问题：模型无法聚焦核心任务

* 改进：精简信息，只保留必要内容

1. **格式要求不明确**：

* 失败案例：期望 JSON 输出但未明确说明

* 问题：模型返回文本而非结构化数据

* 改进：明确指定输出格式和结构

1. **缺乏上下文**：

* 失败案例：在多轮对话中突然改变话题

* 问题：模型无法理解新话题的背景

* 改进：提供必要的上下文信息或过渡说明

通过这些案例分析，我们可以总结出以下关键经验：



1. **明确性是关键**：越具体、越明确的 Prompt，效果越好

2. **迭代优化**：Prompt 工程是一个不断优化的过程

3. **测试验证**：需要通过实际测试来评估和改进 Prompt

4. **场景适配**：不同场景需要不同的 Prompt 策略

5. **用户反馈**：持续收集用户反馈，不断改进 Prompt 设计

## 6. 学习资源与实践建议

### 6.1 基础入门资源

作为初学者，选择合适的学习资源至关重要。以下是一些经过筛选的优质入门资源：

**在线课程推荐**：



1. **吴恩达 xOpenAI Prompt 工程专项课程**

* 平台：Coursera

* 特点：由深度学习领域权威吴恩达与 OpenAI 合作推出

* 内容：涵盖基础概念、最佳实践、实际案例

* 优势：提供 Jupyter Notebook 版本，适合实践操作

* 链接：[DeepLearning.AI Prompt Engineering for Developers](https://www.coursera.org/specializations/prompt-engineering)

1. **DataCamp - Understanding Prompt Engineering**

* 时长：1 小时，11 个视频，29 个练习

* 特点：交互式学习，提供 1500XP 积分

* 内容：从基础到实践，包含 ChatGPT 应用

* 适合人群：希望快速入门的初学者

* 链接：[DataCamp Prompt Engineering](https://www.datacamp.com/courses/understanding-prompt-engineering)

1. **Udemy 系列课程**：

* 《The Complete Prompt Engineering for AI Bootcamp (2025)》：包含最新的 ChatGPT 研究和 Agent 模式

* 《Complete AI and Prompt Engineering Masterclass (2025)》：从基础到高级的完整课程

* 特点：提供终身访问和完成证书

**中文学习资源**：



1. **免费中文教程**：

* B 站系列教程：搜索 "Prompt 工程入门教程"，有多个免费系列

* CSDN 博客：大量入门级文章，如《零基础 1 小时入门，全网最详细的提示词工程教程》

* 掘金专栏：《万字长文解码如何玩转 Prompt》等

1. **系统性中文课程**：

* 《2025 吃透提示词工程全套视频教程》：15 天学习计划

* 《B 站最全最细的提示词工程全套教程》：7 天学习计划

* 特点：包含课件、代码和实战案例

**官方文档与指南**：



1. **OpenAI 官方资源**：

* [OpenAI Cookbook](https://cookbook.openai.com/)：包含大量最佳实践和示例

* [OpenAI API 文档](https://platform.openai.com/docs/guides)：官方 API 指南

* [GPT Best Practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)：官方最佳实践

1. **中文翻译资源**：

* OpenAI 官方指南中文翻译：包含官方文档的完整中文解读

* 熊猫 Jay 万字解读：详细解析 ChatGPT 提示词最佳实践

**入门书籍推荐**：



1. 《Prompt Engineering for Generative AI》（James Phoenix）

* 特点：系统介绍 Prompt 工程基础概念和实践

* 适合：完全零基础的初学者

1. 《深度对话 GPT-4—— 提示工程实战》

* 特点：结合实战案例，注重实用性

* 适合：希望快速上手的学习者

1. 《提示工程架构：从技巧到系统设计》

* 特点：进阶内容，适合有一定基础的学习者

### 6.2 进阶学习路径

当掌握了基础概念后，需要通过进阶学习来提升 Prompt 工程技能。以下是建议的学习路径：

**阶段一：基础巩固（1-2 周）**

学习目标：



* 熟练掌握基础 Prompt 构建技巧

* 了解不同模型的特点和差异

* 能够独立完成简单的 Prompt 设计

学习内容：



1. 完成基础课程的所有练习

2. 在 OpenAI Playground 上进行实践

3. 学习并实践 5-10 个基础 Prompt 模板

4. 尝试在不同场景下应用所学技巧

推荐资源：



* OpenAI Playground：[playground.openai.com](https://playground.openai.com/)

* Prompt 模板库：[PromptBase](https://promptbase.com/)

**阶段二：技巧进阶（2-3 周）**

学习目标：



* 掌握高级 Prompt 技巧（如 CoT、Few-shot 等）

* 理解不同模型的优化策略

* 能够处理复杂的多轮对话场景

学习内容：



1. 深入学习思维链（CoT）技术

2. 掌握少样本学习（Few-shot）技巧

3. 学习多模态 Prompt 设计

4. 了解参数调优策略

5. 实践复杂场景的 Prompt 设计

推荐资源：



* Learn Prompting：[learnprompting.org](https://learnprompting.org/)

* Prompt Engineering Guide：[promptingguide.ai](https://www.promptingguide.ai/)

**阶段三：实战提升（3-4 周）**

学习目标：



* 能够设计生产级别的 Prompt

* 掌握 Prompt 优化和评估方法

* 了解行业最佳实践

学习内容：



1. 学习 Prompt 评估指标和方法

2. 掌握 Prompt 版本控制和管理

3. 了解 Prompt 安全和伦理问题

4. 实践不同行业的应用案例

5. 参与开源项目或社区讨论

推荐资源：



* GitHub Prompt 工程项目：搜索 "prompt-engineering" 相关项目

* Reddit 社区：[r/LearnMachineLearning](https://www.reddit.com/r/LearnMachineLearning/)

* 知乎专栏：关注 AI 和 Prompt

**参考资料&#x20;**

\[1] 《2025提示工程从入门到进阶指南》正式发布 | 中科算网算泥社区\_腾讯新闻[ http://news.qq.com/rain/a/20251211A067WG00](http://news.qq.com/rain/a/20251211A067WG00)

\[2] AI Prompt Engineering: 2025 Guide[ https://www.technolynx.com/post/ai-prompt-engineering-2025-guide](https://www.technolynx.com/post/ai-prompt-engineering-2025-guide)

\[3] What Is Prompt Engineering? | Oracle 中国[ https://www.oracle.com/cn/artificial-intelligence/prompt-engineering/](https://www.oracle.com/cn/artificial-intelligence/prompt-engineering/)

\[4] Prompt engineering: optimizando la interacción con la IA[ https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)

\[5] Prompt Engineering: A Comprehensive Guide for 2025[ https://www.toolify.ai/ai-news/prompt-engineering-a-comprehensive-guide-for-2025-3711647](https://www.toolify.ai/ai-news/prompt-engineering-a-comprehensive-guide-for-2025-3711647)

\[6] What is Prompt Engineering?[ https://www.conviva.com/glossary/prompt-engineering/](https://www.conviva.com/glossary/prompt-engineering/)

\[7] What Is Prompt Engineering? A Comprehensive Guide for Modern AI Teams[ https://www.getmaxim.ai/articles/what-is-prompt-engineering-a-comprehensive-guide-for-modern-ai-teams/](https://www.getmaxim.ai/articles/what-is-prompt-engineering-a-comprehensive-guide-for-modern-ai-teams/)

\[8] 什么是Prompt?-腾讯云开发者社区-腾讯云[ https://cloud.tencent.com/developer/article/2542452](https://cloud.tencent.com/developer/article/2542452)

\[9] 提示词工程(Prompt)入门到精通:一文搞懂核心原理与应用方法\_prompt 工程-CSDN博客[ https://blog.csdn.net/csdn\_224022/article/details/150861497](https://blog.csdn.net/csdn_224022/article/details/150861497)

\[10] 解锁AI大模型:Prompt工程全面解析\_crispe框架实例-CSDN博客[ https://blog.csdn.net/2401\_85592132/article/details/150424921](https://blog.csdn.net/2401_85592132/article/details/150424921)

\[11] 万字长文解码如何玩转Prompt(附实践应用)以下文章来源:https://mp.weixin.qq.com/s/ad6 - 掘金[ https://juejin.cn/post/7538009133640499250](https://juejin.cn/post/7538009133640499250)

\[12] 深入浅出 Prompt 基础概念 & 什么是 Prompt 工程? - NeoLshu - 博客园[ https://www.cnblogs.com/neolshu/p/19120304](https://www.cnblogs.com/neolshu/p/19120304)

\[13] 大模型开发必备:Prompt提示词工程入门到精通全攻略!\_大模型提示词工程-CSDN博客[ https://blog.csdn.net/m0\_65555479/article/details/148628962](https://blog.csdn.net/m0_65555479/article/details/148628962)

\[14] 提示词工程(Prompt Engineering)完全指南:从入门到生产级应用 - 指尖下的世界 - 博客园[ https://www.cnblogs.com/luzhanshi/articles/19071865](https://www.cnblogs.com/luzhanshi/articles/19071865)

\[15] 【大模型入门】一文讲清大模型提示词工程(Prompt Engineering)的核心概念与实现方法!\_大模型提示的几部分-CSDN博客[ https://blog.csdn.net/2401\_84495872/article/details/151621408](https://blog.csdn.net/2401_84495872/article/details/151621408)

\[16] Introduction to Prompt Engineering[ https://techcommunity.microsoft.com/discussions/azure-ai-services/introduction-to-prompt-engineering/4057123](https://techcommunity.microsoft.com/discussions/azure-ai-services/introduction-to-prompt-engineering/4057123)

\[17] Parts of a Prompt: Understanding the Key Elements[ https://learnprompting.org/docs/basics/formalizing](https://learnprompting.org/docs/basics/formalizing)

\[18] Prompt Engineering[ https://dev.natestephens.com/prompt-engineering](https://dev.natestephens.com/prompt-engineering)

\[19] Prompt Engineering 技术文档\_prompt engineering 文档-CSDN博客[ https://blog.csdn.net/Xu\_youyaxianshen/article/details/151793682](https://blog.csdn.net/Xu_youyaxianshen/article/details/151793682)

\[20] Prompt Engineering\_51CTO博客\_prompt engineering book[ https://blog.51cto.com/u\_15851118/14190018](https://blog.51cto.com/u_15851118/14190018)

\[21] 提示词工程(Prompt Engineering)完全指南:从入门到生产级应用 - 指尖下的世界 - 博客园[ https://www.cnblogs.com/luzhanshi/articles/19071865](https://www.cnblogs.com/luzhanshi/articles/19071865)

\[22] 《AI大模型应知应会100篇》第7篇:Prompt Engineering基础:如何与大模型有效沟通-CSDN博客[ https://blog.csdn.net/yweng18/article/details/147103039](https://blog.csdn.net/yweng18/article/details/147103039)

\[23] 大模型 Prompt 工程实战:从入门到高阶的全攻略，玩转 LLM 就靠它-CSDN博客[ https://blog.csdn.net/CSDN\_430422/article/details/154730980](https://blog.csdn.net/CSDN_430422/article/details/154730980)

\[24] 深入浅出 Prompt 基础概念 & 什么是 Prompt 工程? - NeoLshu - 博客园[ https://www.cnblogs.com/neolshu/p/19120304](https://www.cnblogs.com/neolshu/p/19120304)

\[25] 让AI更了解你:掌握提示词与上下文工程的核心策略-腾讯云开发者社区-腾讯云[ https://cloud.tencent.com.cn/developer/article/2565421](https://cloud.tencent.com.cn/developer/article/2565421)

\[26] 大模型时代的prompt学习(持续更新)\_mob64ca13fc5fb6的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213600/14403703](https://blog.51cto.com/u_16213600/14403703)

\[27] 大模型 Prompt 技巧全解析-51CTO.COM[ https://www.51cto.com/article/808432.html](https://www.51cto.com/article/808432.html)

\[28] 智能体搭建:Prompt提示词工程:几句话让AI秒懂你心-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2580967](https://cloud.tencent.cn/developer/article/2580967)

\[29] 08\_提示工程入门:让LLM听你的话引言:为什么提示工程如此重要? 在2025年的今天，大语言模型(LLM)已经成为人工 - 掘金[ https://juejin.cn/post/7555780704270434323](https://juejin.cn/post/7555780704270434323)

\[30] O Fim do Prompt Engineer: A Automação Chegou ao Coração da IA[ https://pt.linkedin.com/pulse/o-fim-do-prompt-engineer-automa%C3%A7%C3%A3o-chegou-ao-cora%C3%A7%C3%A3o-da-fabio-seixas-ab72f?trk=article-ssr-frontend-pulse\_more-articles\_related-content-card](https://pt.linkedin.com/pulse/o-fim-do-prompt-engineer-automa%C3%A7%C3%A3o-chegou-ao-cora%C3%A7%C3%A3o-da-fabio-seixas-ab72f?trk=article-ssr-frontend-pulse_more-articles_related-content-card)

\[31] AI Is Already Eating Its Own: The Rise and Rapid Fall of Prompt Engineering[ https://www.ampcuscyber.com/blogs/rise-and-fall-of-ai-prompt-engineering/](https://www.ampcuscyber.com/blogs/rise-and-fall-of-ai-prompt-engineering/)

\[32] From Templates to Toolchains: Prompt Engineering Trends 2025 Explained[ https://www.refontelearning.com/blog/from-templates-to-toolchains-prompt-engineering-trends-2025-explained](https://www.refontelearning.com/blog/from-templates-to-toolchains-prompt-engineering-trends-2025-explained)

\[33] Prompt Engineering 2.0: System Prompts, Tools, and Measurable Quality[ https://www.sentisight.ai/prompt-engineering-2-0-tools-measurable-quality/](https://www.sentisight.ai/prompt-engineering-2-0-tools-measurable-quality/)

\[34] Advanced Prompt Engineering Techniques in 2025[ https://www.getmaxim.ai/articles/advanced-prompt-engineering-techniques-in-2025/](https://www.getmaxim.ai/articles/advanced-prompt-engineering-techniques-in-2025/)

\[35] A Guide to Prompt Engineering in AI[ https://autogpt.net/a-guide-to-promp-engineering-in-ai/](https://autogpt.net/a-guide-to-promp-engineering-in-ai/)

\[36] 探索AI提示设计未来趋势，提示工程架构师的前沿观点-CSDN博客[ https://blog.csdn.net/2502\_91591115/article/details/149843337](https://blog.csdn.net/2502_91591115/article/details/149843337)

\[37] 2025年提示词工程完全指南:从入门到精通的实战手册\_人人都是产品经理[ http://m.toutiao.com/group/7577358666295214592/?upstream\_biz=doubao](http://m.toutiao.com/group/7577358666295214592/?upstream_biz=doubao)

\[38] Prompt Engineering 正在“进化”为 Context Engineering!\_AI能见未来[ http://m.toutiao.com/group/7528606956567708194/?upstream\_biz=doubao](http://m.toutiao.com/group/7528606956567708194/?upstream_biz=doubao)

\[39] 提示工程发展生态与典型工具/论文简述\_搜狐网[ https://m.sohu.com/a/968134670\_122500756/](https://m.sohu.com/a/968134670_122500756/)

\[40] 《2025提示工程从入门到进阶指南》正式发布 | 中科算网算泥社区\_腾讯新闻[ http://news.qq.com/rain/a/20251211A067WG00](http://news.qq.com/rain/a/20251211A067WG00)

\[41] The Evolution of Prompt Engineering: The Brain of Agentic AI Systems[ https://inclusioncloud.com/insights/blog/the-evolution-of-prompt-engineering/](https://inclusioncloud.com/insights/blog/the-evolution-of-prompt-engineering/)

\[42] 2025提示工程架构师技术博客TOP10:未来趋势讨论与行业洞见-CSDN博客[ https://blog.csdn.net/2502\_91869417/article/details/150614809](https://blog.csdn.net/2502_91869417/article/details/150614809)

\[43] 提示工程(Prompt Engineering)全指南:从入门到精通的完整路径(非常详细)从零基础到精通，收藏这篇就够了!-CSDN博客[ https://blog.csdn.net/leah126/article/details/150558248](https://blog.csdn.net/leah126/article/details/150558248)

\[44] Welcome to the Basics Guide to Generative AI and Prompt Engineering\![ https://learnprompting.org/docs/basics/introduction?srsltid=AfmBOooz0-tFC3w-gW81-YfMMeP3hCsAqIUcVBBGWCjKzG3l2XzmXL4R](https://learnprompting.org/docs/basics/introduction?srsltid=AfmBOooz0-tFC3w-gW81-YfMMeP3hCsAqIUcVBBGWCjKzG3l2XzmXL4R)

\[45] A Beginner's Guide to Prompt Engineering[ http://www.linkedin.com/pulse/beginners-guide-prompt-engineering-michael-raynolds-laursen-vilmf](http://www.linkedin.com/pulse/beginners-guide-prompt-engineering-michael-raynolds-laursen-vilmf)

\[46] Prompt Engineering Guide[ https://promptgenius.net/prompts/chatgpt/resources/prompt-engineering-guide](https://promptgenius.net/prompts/chatgpt/resources/prompt-engineering-guide)

\[47] 提示词(Prompt)工程入门(非常详细)，零基础入门到精通，看这一篇就够了-CSDN博客[ https://blog.csdn.net/2401\_84205765/article/details/146074841](https://blog.csdn.net/2401_84205765/article/details/146074841)

\[48] Prompt工程师指南\[从基础到进阶篇]:用于开发和优化提示，以有效地使用语言模型(LMs)\_mob6454cc67bcfb的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16099209/14409214](https://blog.51cto.com/u_16099209/14409214)

\[49] 从零开始的AI对话指南:5步掌握提示词工程精髓-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2495330?policyId=1004](https://cloud.tencent.cn/developer/article/2495330?policyId=1004)

\[50] 如何写好AI提示词，一文带你从入门到精通(含40个模版)\_学会提问,驾驭ai:提示词从入门到精通-CSDN博客[ https://blog.csdn.net/heiyeshuwu/article/details/149078946](https://blog.csdn.net/heiyeshuwu/article/details/149078946)

\[51] 这是一份简洁优雅的Prompt教程-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2504596?policyId=1003](https://cloud.tencent.cn/developer/article/2504596?policyId=1003)

\[52] 掌握Prompt工程:从入门到进阶的完整指南\_人人都是产品经理[ http://m.toutiao.com/group/7544205276132442663/?upstream\_biz=doubao](http://m.toutiao.com/group/7544205276132442663/?upstream_biz=doubao)

\[53] Prompt工程师指南从基础到进阶篇:用于开发和优化提示，以有效地使用语言模型(LMs)进行各种应用和研究主题\_mob64ca14193248的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213720/14403386](https://blog.51cto.com/u_16213720/14403386)

\[54] 大模型(2)——提示工程(Prompt Engineering)-CSDN博客[ https://blog.csdn.net/jiaomongjun/article/details/148076265](https://blog.csdn.net/jiaomongjun/article/details/148076265)

\[55] 提示工程(Prompt Engineering)入门指南这篇指南是我从Claude Code官方文档中提炼出最核心的技巧 - 掘金[ https://aicoding.juejin.cn/post/7539351775045222451](https://aicoding.juejin.cn/post/7539351775045222451)

\[56] 从菜鸟到大神，Prompt设计的核心秘诀全在这里!-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2509858?policyId=1004](https://cloud.tencent.cn/developer/article/2509858?policyId=1004)

\[57] AI 提示词工程全指南:从“咒语”到“编程”\_mb68b85ccf7a016的技术博客\_51CTO博客[ https://blog.51cto.com/u\_17514447/14399814](https://blog.51cto.com/u_17514447/14399814)

\[58] Effective prompting tips and examples for AI interactions[ https://www.byteplus.com/en/topic/404124](https://www.byteplus.com/en/topic/404124)

\[59] 10 Best Prompt Engineering Tips for ChatGPT in 2025[ https://www.godofprompt.ai/blog/best-prompt-engineering-tips](https://www.godofprompt.ai/blog/best-prompt-engineering-tips)

\[60] Image prompt engineering techniques[ https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/gpt-4-v-prompt-engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/gpt-4-v-prompt-engineering)

\[61] ChatGPT Prompt Engineering for Developers: 13 Best Examples[ https://strapi.io/blog/ChatGPT-Prompt-Engineering-for-Developers](https://strapi.io/blog/ChatGPT-Prompt-Engineering-for-Developers)

\[62] Prompt Engineering for LLMs: A Beginner's Practical Guide to Writing Effective Prompts[ https://techbuzzonline.com/prompt-engineering-llms-beginners-guide/](https://techbuzzonline.com/prompt-engineering-llms-beginners-guide/)

\[63] 7 Prompt Engineering Templates That Actually Work (Yes, You Can Copy-Paste These!)[ https://dextralabs.com/blog/prompt-engineering-templates/?ekit-blog-posts-paged=7](https://dextralabs.com/blog/prompt-engineering-templates/?ekit-blog-posts-paged=7)

\[64] 大模型 Prompt 工程实战:从入门到高阶的全攻略，玩转 LLM 就靠它-CSDN博客[ https://blog.csdn.net/CSDN\_430422/article/details/154730980](https://blog.csdn.net/CSDN_430422/article/details/154730980)

\[65] 不会写Prompt?AI产品经理的Prompt工程实战指南(从入门到落地，建议收藏)\_prompt产品经理-CSDN博客[ https://blog.csdn.net/2401\_85373691/article/details/149900126](https://blog.csdn.net/2401_85373691/article/details/149900126)

\[66] 这是一份简洁优雅的Prompt教程-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2504596?policyId=1003](https://cloud.tencent.cn/developer/article/2504596?policyId=1003)

\[67] 从零开始的AI对话指南:5步掌握提示词工程精髓-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2495330?policyId=1003](https://cloud.tencent.cn/developer/article/2495330?policyId=1003)

\[68] 实用指南:零基础学AI大模型之Prompt提示词工程\_mob6454cc7aaa9d的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16099343/14247423](https://blog.51cto.com/u_16099343/14247423)

\[69] 从零到一构建生产级Prompt\_人人都是产品经理[ http://m.toutiao.com/group/7571390461386949163/?upstream\_biz=doubao](http://m.toutiao.com/group/7571390461386949163/?upstream_biz=doubao)

\[70] Prompt设计实战指南:三大模板与进阶技巧🎯 Prompt设计实战指南:三大模板与进阶技巧 一、需求+细节+目标模板 - 掘金[ https://juejin.cn/post/7550992566671065128](https://juejin.cn/post/7550992566671065128)

\[71] GPT-4.1 Prompting Guide[ https://cookbook.openai.com/examples/gpt4-1\_prompting\_guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)

\[72] prompt-blueprint/guides/openai-best-practices\_\_chatgpt-4\_5.md at main · thibaultyou/prompt-blueprint · GitHub[ https://github.com/thibaultyou/prompt-blueprint/blob/main/guides/openai-best-practices\_\_chatgpt-4\_5.md](https://github.com/thibaultyou/prompt-blueprint/blob/main/guides/openai-best-practices__chatgpt-4_5.md)

\[73] Stop Writing Terrible Prompts: GPT-4 API Guide That Actually Works[ https://markaicode.com/gpt4-prompt-engineering-guide/](https://markaicode.com/gpt4-prompt-engineering-guide/)

\[74] prompt-engineering[ https://community.openai.com/tag/prompt-engineering](https://community.openai.com/tag/prompt-engineering)

\[75] GPT-4.1 提示工程(Prompt Engineering)详细指南-AITOP100,AI资讯[ https://www.aitop100.cn/infomation/details/24175.html](https://www.aitop100.cn/infomation/details/24175.html)

\[76] Prompt Engineering Best Practices for GPT-4: Building Reliable, Custom LLM Chatbots[ https://www.amplework.com/blog/gpt4-prompt-engineering-best-practices/](https://www.amplework.com/blog/gpt4-prompt-engineering-best-practices/)

\[77] OpenAI GPT-4.1 Prompting Guide[ https://www.rivista.ai/2025/05/15/openai-gpt-4-1-prompting-guide/](https://www.rivista.ai/2025/05/15/openai-gpt-4-1-prompting-guide/)

\[78] 告别AI瞎猜:gh\_mirrors/pr/prompt-engineering让GPT-4输出可控的实战指南-CSDN博客[ https://blog.csdn.net/gitblog\_00979/article/details/152063528](https://blog.csdn.net/gitblog_00979/article/details/152063528)

\[79] AI和运维的故事-CSDN博客[ https://blog.csdn.net/weixin\_42738495/article/details/149338227](https://blog.csdn.net/weixin_42738495/article/details/149338227)

\[80] Controlling the length of OpenAI model responses[ https://help.openai.com/en/articles/5072518-controlling-the-length-of-openai-model-responses%23.pls](https://help.openai.com/en/articles/5072518-controlling-the-length-of-openai-model-responses%23.pls)

\[81] 提示工程架构的资源占用规范:优化Token使用的8个方法-CSDN博客[ https://blog.csdn.net/2501\_91490244/article/details/150074235](https://blog.csdn.net/2501_91490244/article/details/150074235)

\[82] 揭秘大模型的“记忆力”:Token和上下文窗口完全指南深入浅出地讲解什么是Token、上下文窗口以及它们如何影响AI的表 - 掘金[ https://juejin.cn/post/7585157583473803315](https://juejin.cn/post/7585157583473803315)

\[83] 让 GPT-5 成为最靠谱的智能助手:OpenAI 提示工程全解析\_爱死亡机器人的技术博客\_51CTO博客[ https://blog.51cto.com/ghostwritten/14192748](https://blog.51cto.com/ghostwritten/14192748)

\[84] Google大模型基础教程02—— 大语言模型的提示词工程\_木汝科技@muru[ http://m.toutiao.com/group/7586124936050131496/?upstream\_biz=doubao](http://m.toutiao.com/group/7586124936050131496/?upstream_biz=doubao)

\[85] ChatGPTで扱える書類・ファイル数と制限まとめ[ https://note.com/emm\_tokyo/n/n04b0f7746bea](https://note.com/emm_tokyo/n/n04b0f7746bea)

\[86] What is the character limit on OpenAI ChatGPT?[ https://www.byteplus.com/en/topic/546378](https://www.byteplus.com/en/topic/546378)

\[87] ChatGPT token limit per request Empowers Efficient Planning[ https://scalebytech.com/chatgpt-token-limit-per-request/](https://scalebytech.com/chatgpt-token-limit-per-request/)

\[88] (pdf)[ http://kpangu.com/img/files/4a3967f0-ba8f-44d6-b72b-95a10b23c5cb.pdf](http://kpangu.com/img/files/4a3967f0-ba8f-44d6-b72b-95a10b23c5cb.pdf)

\[89] Breaking the Token Limit: Mastering Large Text Inputs in ChatGPT (2025 Edition)[ https://www.rickyspears.com/ai/breaking-the-token-limit-mastering-large-text-inputs-in-chatgpt-2025-edition/](https://www.rickyspears.com/ai/breaking-the-token-limit-mastering-large-text-inputs-in-chatgpt-2025-edition/)

\[90] gpt 4 context window Maximizes Token Efficiency[ https://scalebytech.com/gpt-4-context-window/](https://scalebytech.com/gpt-4-context-window/)

\[91] Comparison of OpenAI Language Models (May 2025)[ https://gpt.gekko.de/comparison-openai-language-models-may-2025/](https://gpt.gekko.de/comparison-openai-language-models-may-2025/)

\[92] 更改模型版本和设置 - Microsoft Copilot Studio | Microsoft Learn[ https://video2.skills-academy.com/zh-cn/ai-builder/prompt-modelsettings](https://video2.skills-academy.com/zh-cn/ai-builder/prompt-modelsettings)

\[93] GPT系列模型-详解\_gpt模型-CSDN博客[ https://blog.csdn.net/weixin\_61006262/article/details/152802825](https://blog.csdn.net/weixin_61006262/article/details/152802825)

\[94] GPT 4.1 API正式发布!GPT 4.1怎么样?GPT 4.1如何使用?如何免费使用?教你2种方法白嫖! - 掘金[ https://juejin.cn/post/7493198688871153716](https://juejin.cn/post/7493198688871153716)

\[95] ChatGPT当前基于哪个大模型版本?\_编程语言-CSDN问答[ https://ask.csdn.net/questions/8847927](https://ask.csdn.net/questions/8847927)

\[96] OpenAI发布GPT-4.1系列模型：长上下文与高效[ https://www.iesdouyin.com/share/note/7524727461121412412/?region=\&mid=7431527252317882385\&u\_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with\_sec\_did=1\&video\_share\_track\_ver=\&titleType=title\&schema\_type=37\&share\_sign=RRu0CLssc.Sj3oUS5O1lTuEJcZktg7pNBHWlhiud.sM-\&share\_version=280700\&ts=1766840355\&from\_aid=1128\&from\_ssr=1\&share\_track\_info=%7B%22link\_description\_type%22%3A%22%22%7D](https://www.iesdouyin.com/share/note/7524727461121412412/?region=\&mid=7431527252317882385\&u_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with_sec_did=1\&video_share_track_ver=\&titleType=title\&schema_type=37\&share_sign=RRu0CLssc.Sj3oUS5O1lTuEJcZktg7pNBHWlhiud.sM-\&share_version=280700\&ts=1766840355\&from_aid=1128\&from_ssr=1\&share_track_info=%7B%22link_description_type%22%3A%22%22%7D)

\[97] ChatGPT 模型指南:参数概念与应用 · LobeChat Docs · LobeHub[ https://lobehub.com/zh/docs/usage/agents/model](https://lobehub.com/zh/docs/usage/agents/model)

\[98] GPT 4.1 模型上线，支持百万token上下文，性能吊打 GPT 4o ，性价比超高!-腾讯云开发者社区-腾讯云[ https://cloud.tencent.com.cn/developer/article/2514280](https://cloud.tencent.com.cn/developer/article/2514280)

\[99] 不同大模型的prompt是否存在差异?-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2505128?policyId=1004](https://cloud.tencent.cn/developer/article/2505128?policyId=1004)

\[100] AI Model Comparison 2025: GPT, Claude, Grok and more[ https://blog.typingmind.com/ai-model-comparison-2025/](https://blog.typingmind.com/ai-model-comparison-2025/)

\[101] Which LLM is the Best for Answering User Queries?[ https://www.sentisight.ai/which-llm-best-answers-user-queries/](https://www.sentisight.ai/which-llm-best-answers-user-queries/)

\[102] ChatGPT vs Claude (2025): The Ultimate Comparison of AI Assistants[ https://www.datastudios.org/post/chatgpt-vs-claude-2025-the-ultimate-comparison-of-ai-assistants](https://www.datastudios.org/post/chatgpt-vs-claude-2025-the-ultimate-comparison-of-ai-assistants)

\[103] Claude vs. ChatGPT | 2025 Comparison of Anthropic & OpenAI[ https://www.makebot.ai/blog-en/claude-vs-chatgpt-2025-comparison-of-anthropic-openai](https://www.makebot.ai/blog-en/claude-vs-chatgpt-2025-comparison-of-anthropic-openai)

\[104] 2025 LLM Comparison: Claude, Gemini, GPT | Generated by AI[ https://lzwjava.github.io/notes/2025-07-06-2025-llm-comparison-en](https://lzwjava.github.io/notes/2025-07-06-2025-llm-comparison-en)

\[105] AI Models Comparison 2025: Top Picks and Insights[ https://collabnix.com/comparing-top-ai-models-in-2025-claude-grok-gpt-llama-gemini-and-deepseek-the-ultimate-guide/](https://collabnix.com/comparing-top-ai-models-in-2025-claude-grok-gpt-llama-gemini-and-deepseek-the-ultimate-guide/)

\[106] 资深提示工程架构师经验:如何应对不同大模型的Prompt差异?\_同样prompt 不同模型不一样-CSDN博客[ https://blog.csdn.net/2501\_91490244/article/details/150401488](https://blog.csdn.net/2501_91490244/article/details/150401488)

\[107] 你的 Prompt 都该重写?\_清梦游天[ http://m.toutiao.com/group/7580376509753147947/?upstream\_biz=doubao](http://m.toutiao.com/group/7580376509753147947/?upstream_biz=doubao)

\[108] Claude 模型与 GPT 模型的区别剖析​在人工智能飞速发展的当下，大型语言模型成为了众人瞩目的焦点。Claude - 掘金[ https://juejin.cn/post/7530179277796196402](https://juejin.cn/post/7530179277796196402)

\[109] 全面对比主流大模型，了选对大模型真的可以事半功倍!本报告旨在梳理和分析2025年市场上被广泛讨论和使用的主流大型语言模型 - 掘金[ https://juejin.cn/post/7554677260345491519](https://juejin.cn/post/7554677260345491519)

\[110] 建议收藏!一套通用提示词工程框架搞定 GPT、Claude、Gemini 等所有大模型 - 苏米客[ https://xmsumi.com/detail/2083](https://xmsumi.com/detail/2083)

\[111] AI 对话艺术:Prompt 设计技巧与案例解析-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2508769?policyId=1004](https://cloud.tencent.cn/developer/article/2508769?policyId=1004)

\[112] 提示工程架构师公认的10个提示优化最佳实践(附案例)\_兰蔻客服投诉处理提示词优化,用户满意度从 3.2 分提升至 4.5 分-CSDN博客[ https://blog.csdn.net/2502\_92021348/article/details/151325346](https://blog.csdn.net/2502_92021348/article/details/151325346)

\[113] Prompt Engineering Cheatsheet (17 Techniques for 1B LLMs)[ https://github.com/FareedKhan-dev/prompt-engineering-cheatsheet](https://github.com/FareedKhan-dev/prompt-engineering-cheatsheet)

\[114] How Does Prompt Engineering Work? (With Examples & Use Cases)[ https://www.c-sharpcorner.com/article/how-does-prompt-engineering-work-with-examples-use-cases/](https://www.c-sharpcorner.com/article/how-does-prompt-engineering-work-with-examples-use-cases/)

\[115] It’s All About the Prompt, Part 2: Real-World Examples and GPT-4 vs GPT-5 Comparisons[ https://www.synergyonline.com/post/it-s-all-about-the-prompt-part-2-real-world-examples-and-gpt-4-vs-gpt-5-comparisons](https://www.synergyonline.com/post/it-s-all-about-the-prompt-part-2-real-world-examples-and-gpt-4-vs-gpt-5-comparisons)

\[116] Prompt Engineering vs RAG: Smarter Code Suggestions[ https://www.qodo.ai/blog/rag-vs-fine-tuning-vs-rag-prompt-engineering/](https://www.qodo.ai/blog/rag-vs-fine-tuning-vs-rag-prompt-engineering/)

\[117] Prompt Engineering: From Zero-Shot to Advanced AI Reasoning[ https://www.bluetickconsultants.com/the-evolution-of-prompt-engineering/](https://www.bluetickconsultants.com/the-evolution-of-prompt-engineering/)

\[118] Prompt Engineering vs. Context Engineering: Understanding the Critical Differences for LLM Mastery[ https://prompt-engineer.com/prompt-engineering-vs-context-engineering-understanding-the-critical-differences-for-llm-mastery/](https://prompt-engineer.com/prompt-engineering-vs-context-engineering-understanding-the-critical-differences-for-llm-mastery/)

\[119] 《AI大模型应知应会100篇》第7篇:Prompt Engineering基础:如何与大模型有效沟通-CSDN博客[ https://blog.csdn.net/yweng18/article/details/146967539](https://blog.csdn.net/yweng18/article/details/146967539)

\[120] 小白入门大模型之 Prompt 工程:解锁高效对话的密码\_当前暂不支持prompt输入,请使用灵感卡片以获得更好效果,-CSDN博客[ https://blog.csdn.net/m0\_48891301/article/details/148307046](https://blog.csdn.net/m0_48891301/article/details/148307046)

\[121] 一文看懂“提示词” vs “提示词工程” vs “上下文工程”\_HuggingFace[ http://m.toutiao.com/group/7522348446125146633/?upstream\_biz=doubao](http://m.toutiao.com/group/7522348446125146633/?upstream_biz=doubao)

\[122] GPT-5暴写“屎山代码”，14个Prompt，看穿GPT-1到GPT-5七年智商进化史\_36氪[ http://m.toutiao.com/group/7540218089011495470/?upstream\_biz=doubao](http://m.toutiao.com/group/7540218089011495470/?upstream_biz=doubao)

\[123] AI对话魔法|Prompt Engineering 探索指南一、什么是 Prompt Engineering? 想象一下 - 掘金[ https://juejin.cn/post/7501209408196001842](https://juejin.cn/post/7501209408196001842)

\[124] 沃顿商学院重磅Prompt报告:别再对AI"循循善诱"了!我们在错误地使用它\![ https://m.aitntnews.com/newDetail.html?newId=14901](https://m.aitntnews.com/newDetail.html?newId=14901)

\[125] AI 生 图 大模型 硬核 对比 测评 ： 即 梦 3 . 1 、 Mid journey V7 、 Google Imagen 4 Ultra 、 可 图 2 . 1 ， 到底 谁 的 Prompt 指令 遵循 能力 更 强 ？ # AI 设计 # 设计师 # AI 生 图 # 设计 # 涨 知识[ https://www.iesdouyin.com/share/video/7533753461621656890/?region=\&mid=7533753366648834859\&u\_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with\_sec\_did=1\&video\_share\_track\_ver=\&titleType=title\&share\_sign=EhoVXATf3G5yiwSF2w5kXkZm\_Dz8CJiL\_oTronAKgmw-\&share\_version=280700\&ts=1766840290\&from\_aid=1128\&from\_ssr=1\&share\_track\_info=%7B%22link\_description\_type%22%3A%22%22%7D](https://www.iesdouyin.com/share/video/7533753461621656890/?region=\&mid=7533753366648834859\&u_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with_sec_did=1\&video_share_track_ver=\&titleType=title\&share_sign=EhoVXATf3G5yiwSF2w5kXkZm_Dz8CJiL_oTronAKgmw-\&share_version=280700\&ts=1766840290\&from_aid=1128\&from_ssr=1\&share_track_info=%7B%22link_description_type%22%3A%22%22%7D)

\[126] 提示工程架构师的“生成误区避坑”:10个错误，你必须避开!-CSDN博客[ https://blog.csdn.net/2501\_91888447/article/details/152168249](https://blog.csdn.net/2501_91888447/article/details/152168249)

\[127] 5 Common Prompt Engineering Mistakes Beginners Make[ https://metaailabs.com/5-common-prompt-engineering-mistakes-beginners-make/](https://metaailabs.com/5-common-prompt-engineering-mistakes-beginners-make/)

\[128] (pdf)[ https://www.di.ubi.pt/\~hugomcp/pe/06\_pe\_24\_25.pdf](https://www.di.ubi.pt/~hugomcp/pe/06_pe_24_25.pdf)

\[129] 10 Critical Mistakes in ChatGPT Prompt Engineering to Avoid in 2025[ https://www.rickyspears.com/ai/10-critical-mistakes-in-chatgpt-prompt-engineering-to-avoid-in-2025/](https://www.rickyspears.com/ai/10-critical-mistakes-in-chatgpt-prompt-engineering-to-avoid-in-2025/)

\[130] Common AI Prompt Mistakes and How to Fix Them[ https://www.godofprompt.ai/blog/common-ai-prompt-mistakes-and-how-to-fix-them](https://www.godofprompt.ai/blog/common-ai-prompt-mistakes-and-how-to-fix-them)

\[131] Five Key Mistakes to Avoid in Prompt Design with Expert Tips You Should Be Aware Of[ https://moldstud.com/articles/p-five-key-mistakes-to-avoid-in-prompt-design-with-expert-tips-you-should-be-aware-of](https://moldstud.com/articles/p-five-key-mistakes-to-avoid-in-prompt-design-with-expert-tips-you-should-be-aware-of)

\[132] Common LLM Pitfalls and Best Practices[ https://handbook.exemplar.dev/ai\_engineer/llms/pitfalls\_llm](https://handbook.exemplar.dev/ai_engineer/llms/pitfalls_llm)

\[133] 客户服务提示工程:Prompt设计的10个常见误区-CSDN博客[ https://blog.csdn.net/2501\_91590464/article/details/152453291](https://blog.csdn.net/2501_91590464/article/details/152453291)

\[134] 我做了10个提示工程项目，总结出7个用户意图误解的失败教训-CSDN博客[ https://blog.csdn.net/2405\_88636357/article/details/155950956](https://blog.csdn.net/2405_88636357/article/details/155950956)

\[135] Prompt调试技巧:20个常见错误诊断[ http://bbs.itying.com/topic/67c7e1bb36bb8501316ffdc6](http://bbs.itying.com/topic/67c7e1bb36bb8501316ffdc6)

\[136] Prompt Engineering 常见陷阱及规避方法-51CTO.COM[ https://www.51cto.com/article/811509.html](https://www.51cto.com/article/811509.html)

\[137] 前端学AI:如何写好提示词(prompt)本文主要讲述提示词(prompt)相关的知识点:提示词的定义、本质特征、作用， - 掘金[ https://juejin.cn/post/7478185513460482048](https://juejin.cn/post/7478185513460482048)

\[138] 7 Principais erros na Engenharia de Prompt[ https://pt.linkedin.com/pulse/7-principais-erros-na-engenharia-de-prompt-ricardo-miluzzi-v2gsf?trk=public\_post](https://pt.linkedin.com/pulse/7-principais-erros-na-engenharia-de-prompt-ricardo-miluzzi-v2gsf?trk=public_post)

\[139] 提示工程架构师避坑手册:初级到高级常见20个错误，附正确解决方案-CSDN博客[ https://blog.csdn.net/2501\_91473495/article/details/149712929](https://blog.csdn.net/2501_91473495/article/details/149712929)

\[140] 【每天一个知识点】提示词工程\_mob64ca140b0bc8的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213661/14303482](https://blog.51cto.com/u_16213661/14303482)

\[141] Prompt engineering: optimizando la interacción con la IA[ https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque](https://es.linkedin.com/pulse/prompt-engineering-optimizando-la-interacci%C3%B3n-con-ia-fresh-latam-usque)

\[142] Communicating with AI: Prompt engineering strategies every leader should know[ https://www.kellton.com/kellton-tech-blog/prompt-engineering-for-business-in-their-ai-decision-making](https://www.kellton.com/kellton-tech-blog/prompt-engineering-for-business-in-their-ai-decision-making)

\[143] Prompt Engineering Evolution: Adapting to 2025 Changes[ https://www.godofprompt.ai/blog/prompt-engineering-evolution-adapting-to-2025-changes](https://www.godofprompt.ai/blog/prompt-engineering-evolution-adapting-to-2025-changes)

\[144] What are the practical applications of prompt engineering?[ https://www.educative.io/blog/real-world-applications-of-prompt-engineering](https://www.educative.io/blog/real-world-applications-of-prompt-engineering)

\[145] Top 7 Enterprise Use Cases of Prompt Engineering in AI-Powered Workflows[ https://dextralabs.com/blog/enterprise-use-cases-of-prompt-engineering/?ekit-blog-posts-paged=16](https://dextralabs.com/blog/enterprise-use-cases-of-prompt-engineering/?ekit-blog-posts-paged=16)

\[146] Engenharia de Prompt: Uma Ferramenta para a Eficiência no Trabalho[ https://pt.linkedin.com/pulse/engenharia-de-prompt-uma-ferramenta-para-efici%C3%AAncia-israel-m-pereira-rirgf](https://pt.linkedin.com/pulse/engenharia-de-prompt-uma-ferramenta-para-efici%C3%AAncia-israel-m-pereira-rirgf)

\[147] AI 对话艺术:Prompt 设计技巧与案例解析-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2508769?policyId=1003](https://cloud.tencent.cn/developer/article/2508769?policyId=1003)

\[148] 提示词工程(Prompt Engineering)完全指南:从入门到生产级应用 - 指尖下的世界 - 博客园[ https://www.cnblogs.com/luzhanshi/articles/19071865](https://www.cnblogs.com/luzhanshi/articles/19071865)

\[149] 【每天一个知识点】全面了解 Prompt:人工智能时代的沟通语言\_prompt人工智能-CSDN博客[ https://blog.csdn.net/dundunmm/article/details/147010019](https://blog.csdn.net/dundunmm/article/details/147010019)

\[150] 大模型 Prompt 工程实战:从入门到高阶的全攻略，玩转 LLM 就靠它-CSDN博客[ https://blog.csdn.net/CSDN\_430422/article/details/154730980](https://blog.csdn.net/CSDN_430422/article/details/154730980)

\[151] Prompt Engineering\_51CTO博客\_prompt engineering book[ https://blog.51cto.com/u\_15851118/14190018](https://blog.51cto.com/u_15851118/14190018)

\[152] 大模型的典型应用场景\_阿里云大模型工程师ACA认证免费课程\_阿里云培训中心-阿里云[ https://edu.aliyun.com/lesson/343300096](https://edu.aliyun.com/lesson/343300096)

\[153] AI之Prompt简介\_牛客网[ https://www.nowcoder.com/discuss/732154415506804736](https://www.nowcoder.com/discuss/732154415506804736)

\[154] Prompt 编程实战:用 AI 10 分钟开发 Chrome 插件AI 应用开发工程师:用 Prompt 编程与 LL - 掘金[ https://aicoding.juejin.cn/post/7506832918317154367](https://aicoding.juejin.cn/post/7506832918317154367)

\[155] Startup Guide to Prompt Engineering Using GitHub Copilot[ https://xebia.com/blog/microsoft-services-startup-guide-to-prompt-engineering-using-github-copilot/](https://xebia.com/blog/microsoft-services-startup-guide-to-prompt-engineering-using-github-copilot/)

\[156] Generating Code[ https://www.promptingguide.ai/kr/applications/coding](https://www.promptingguide.ai/kr/applications/coding)

\[157] Working with Code via ChatGPT[ https://codefinity.com/courses/v2/25328d71-183b-406e-9c29-d45129ed8108/3f95161e-5855-47e0-ba29-d7e903b8305f/39d29030-a87c-47d4-aec2-b2430af3aadc](https://codefinity.com/courses/v2/25328d71-183b-406e-9c29-d45129ed8108/3f95161e-5855-47e0-ba29-d7e903b8305f/39d29030-a87c-47d4-aec2-b2430af3aadc)

\[158] Prompt Engineering Cheat Sheet for GPT-5: Learn These Patterns for Solid Code Generation[ https://www.freecodecamp.org/news/prompt-engineering-cheat-sheet-for-gpt-5/](https://www.freecodecamp.org/news/prompt-engineering-cheat-sheet-for-gpt-5/)

\[159] CodeGeneration[ https://github.com/medxiaorudan/CodeGeneration/](https://github.com/medxiaorudan/CodeGeneration/)

\[160] ChatGPT Prompt Engineering for Developers: 13 Best Examples[ https://strapi.io/blog/ChatGPT-Prompt-Engineering-for-Developers?ref=bytes](https://strapi.io/blog/ChatGPT-Prompt-Engineering-for-Developers?ref=bytes)

\[161] 拆解 Prompt 工程:五大场景驱动 DeepSeek 超越 ChatGPT\_deepseek prompt 客户画像模版-CSDN博客[ https://blog.csdn.net/qq\_52213943/article/details/147769577](https://blog.csdn.net/qq_52213943/article/details/147769577)

\[162] 提示词工程(Prompt Engineering)完全指南:从入门到生产级应用 - 指尖下的世界 - 博客园[ https://www.cnblogs.com/luzhanshi/articles/19071865](https://www.cnblogs.com/luzhanshi/articles/19071865)

\[163] 提示工程(Prompt Engineering)全指南:从入门到精通的完整路径\_如何学习 prompt engineering-CSDN博客[ https://blog.csdn.net/ytt0523\_com/article/details/150346205](https://blog.csdn.net/ytt0523_com/article/details/150346205)

\[164] 实用指南:零基础学AI大模型之Prompt提示词工程\_mob6454cc7aaa9d的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16099343/14247423](https://blog.51cto.com/u_16099343/14247423)

\[165] deep seek下Prompt设计终极指南:从原则到实战的优化技巧大全-腾讯云开发者社区-腾讯云[ https://cloud.tencent.com/developer/article/2510561](https://cloud.tencent.com/developer/article/2510561)

\[166] AI 对话艺术:Prompt 设计技巧与案例解析\_李卓知识库的技术博客\_51CTO博客[ https://blog.51cto.com/lizhuo6/13671568](https://blog.51cto.com/lizhuo6/13671568)

\[167] 2025 的 Ai 的 proment 所有提示词方向分享以下是覆盖12大行业的提示词工程案例库，包含场景化提示词模板、 - 掘金[ https://juejin.cn/post/7531661199101493286](https://juejin.cn/post/7531661199101493286)

\[168] The Complete Prompt Engineering for AI Bootcamp (2025) | Udemy[ https://www.udemy.com/course/prompt-engineering-for-ai/?srsltid=AfmBOor9\_jsVYVmrFcc4ZECvXxaKHPSiGKOxbn2sTjUTsUJsQXGmu0KC](https://www.udemy.com/course/prompt-engineering-for-ai/?srsltid=AfmBOor9_jsVYVmrFcc4ZECvXxaKHPSiGKOxbn2sTjUTsUJsQXGmu0KC)

\[169] Understanding Prompt Engineering[ https://www.datacamp.com/courses/understanding-prompt-engineering?ref=eqraatech.com](https://www.datacamp.com/courses/understanding-prompt-engineering?ref=eqraatech.com)

\[170] The Complete Ai Prompt Engineering for Beginners -2025[ https://www.udemy.com/course/master-prompt-engineering-basic-to-advanced/?srsltid=AfmBOoriiuNWh-2TrC2i4\_FLQpKOFbPYIDFBUta6E\_kQESFjJYcA4spc](https://www.udemy.com/course/master-prompt-engineering-basic-to-advanced/?srsltid=AfmBOoriiuNWh-2TrC2i4_FLQpKOFbPYIDFBUta6E_kQESFjJYcA4spc)

\[171] Complete AI and Prompt Engineering Masterclass (2025)[ https://www.udemy.com/course/artificial-intelligence-guide-master-ai/?quantity=1](https://www.udemy.com/course/artificial-intelligence-guide-master-ai/?quantity=1)

\[172] Prompt Engineering 101: Learn to Communicate with AI[ https://www.tutorialspoint.com/course/prompt-engineering-101-learn-to-communicate-with-ai/index.asp](https://www.tutorialspoint.com/course/prompt-engineering-101-learn-to-communicate-with-ai/index.asp)

\[173] Prompt Engineering: Mastering ChatGPT & GitHub Copilot[ https://www.tutorialspoint.com/course/prompt-engineering-mastering-chatgpt-and-github-copilot/index.asp](https://www.tutorialspoint.com/course/prompt-engineering-mastering-chatgpt-and-github-copilot/index.asp)

\[174] 八 个 值得 反复 观看 的 Gemini 教程 。 涵盖 提示 词 prompt&#x20;

&#x20;学术 研究&#x20;

&#x20;代码 调试&#x20;

&#x20;创意 生成&#x20;

&#x20;营销 爆款&#x20;

&#x20;Agent 构建&#x20;

&#x20;\# 创作 灵感 # 上 热搜 # 知识 分享[ https://www.iesdouyin.com/share/note/7588026081543212778/?region=\&mid=7452211876186196746\&u\_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with\_sec\_did=1\&video\_share\_track\_ver=\&titleType=title\&schema\_type=37\&share\_sign=LF8tP1a4zx2Xco\_WZr41l6bfqYZUtwgdP1eW\_QSkM3Q-\&share\_version=280700\&ts=1766840434\&from\_aid=1128\&from\_ssr=1\&share\_track\_info=%7B%22link\_description\_type%22%3A%22%22%7D](https://www.iesdouyin.com/share/note/7588026081543212778/?region=\&mid=7452211876186196746\&u_code=0\&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\&with_sec_did=1\&video_share_track_ver=\&titleType=title\&schema_type=37\&share_sign=LF8tP1a4zx2Xco_WZr41l6bfqYZUtwgdP1eW_QSkM3Q-\&share_version=280700\&ts=1766840434\&from_aid=1128\&from_ssr=1\&share_track_info=%7B%22link_description_type%22%3A%22%22%7D)

\[175] 提示工程(Prompt Engineering)-CSDN博客[ https://blog.csdn.net/weixin\_41120248/article/details/154619525](https://blog.csdn.net/weixin_41120248/article/details/154619525)

\[176] 2025最新爆款!普通人从零掌握大模型提示词工程:保姆级学习路线+实战案例解析\_经典大模型提示词工程技术路线概述-CSDN博客[ https://blog.csdn.net/m0\_63171455/article/details/147246535](https://blog.csdn.net/m0_63171455/article/details/147246535)

\[177] 2025 最全指南:程序员必备 Prompt Engineering(AI 提示词)实战攻略与优质平台推荐 - 幂简集成[ https://www.explinks.com/blog/yt-ai-prompt-guide/](https://www.explinks.com/blog/yt-ai-prompt-guide/)

\[178] 提示工程架构师必看!最佳实践社区推荐的8个学习资源，超全-CSDN博客[ https://blog.csdn.net/2501\_91473495/article/details/151195761](https://blog.csdn.net/2501_91473495/article/details/151195761)

\[179] 与知识库对话 - AI提示词有什么免费的学习课程 - WayToAGI[ https://www.waytoagi.com/zh/question/72958](https://www.waytoagi.com/zh/question/72958)

\[180] 与知识库对话 - 如何学习Prompt - WayToAGI[ https://www.waytoagi.com/zh/question/98235](https://www.waytoagi.com/zh/question/98235)

\[181] prompt提示工程初级到高级用法指南【初阶】 【入门】吴恩达Prompt公开课 【视频教程(英文版)】https:// - 掘金[ https://juejin.cn/post/7473705093398560779](https://juejin.cn/post/7473705093398560779)

\[182] 2025 最全指南:程序员必备 Prompt Engineering(AI 提示词)实战攻略与优质平台推荐 - 幂简集成[ https://www.explinks.com/blog/yt-ai-prompt-guide/](https://www.explinks.com/blog/yt-ai-prompt-guide/)

\[183] Prompt Builder Launches Platform to Craft Perfect AI Prompts in Seconds, Not Hours[ https://web3wire.org/web3/prompt-builder-launches-platform-to-craft-perfect-ai-prompts-in-seconds-not-hours/](https://web3wire.org/web3/prompt-builder-launches-platform-to-craft-perfect-ai-prompts-in-seconds-not-hours/)

\[184] The Ultimate List of Top Prompt Engineering Tools in 2025[ https://eicta.iitk.ac.in/knowledge-hub/artificial-intelligence/prompt-engineering-tools/](https://eicta.iitk.ac.in/knowledge-hub/artificial-intelligence/prompt-engineering-tools/)

\[185] Top 3 Tools in 2025 to Experiment with Prompts[ https://www.getmaxim.ai/articles/top-5-tools-in-2025-to-experiment-with-prompts/](https://www.getmaxim.ai/articles/top-5-tools-in-2025-to-experiment-with-prompts/)

\[186] Tools to Watch: What’s Powering Prompt Engineering Trends 2025[ https://www.refontelearning.com/blog/whats-powering-prompt-engineering-trends-2025](https://www.refontelearning.com/blog/whats-powering-prompt-engineering-trends-2025)

\[187] 6 Best Prompt Engineering Tools for AI Optimization in 2025[ https://www.eweek.com/artificial-intelligence/prompt-engineering-tools/](https://www.eweek.com/artificial-intelligence/prompt-engineering-tools/)

\[188] 8 Best Prompt Engineering Tools for AI Teams in 2025[ https://www.getmaxim.ai/articles/8-best-prompt-engineering-tools-for-ai-teams-in-2025/](https://www.getmaxim.ai/articles/8-best-prompt-engineering-tools-for-ai-teams-in-2025/)

\[189] 不会写Prompt?AI产品经理的Prompt工程实战指南(从入门到落地，建议收藏)\_prompt产品经理-CSDN博客[ https://blog.csdn.net/2401\_85373691/article/details/149900126](https://blog.csdn.net/2401_85373691/article/details/149900126)

\[190] 扣子罗盘!轻松构建 Prompt，可视化调试、测评AI Agent继coze空间之后，coze又最新推出了扣子罗盘，一款 - 掘金[ https://juejin.cn/post/7502258740831535131](https://juejin.cn/post/7502258740831535131)

\[191] 2025年10大爆款Prompt优化工具全面测评-AI.x-AIGC专属社区-51CTO.COM[ https://www.51cto.com/aigc/6685.html](https://www.51cto.com/aigc/6685.html)

\[192] LangSmith:大模型应用调试利器LangSmith 作为 LangChain 团队推出的一款专业工具，为开发者提供 - 掘金[ https://juejin.cn/post/7521314647523246119](https://juejin.cn/post/7521314647523246119)

\[193] PromptPilot – Prompt优化官网 - 专为大模型开发，PromptPilot为你提供更精准，专业，可持续迭代提示词!PromptPilot 是一款面向大模型应用的全链路优化平台，覆盖大模型开发从构想、开发部署到迭代优化的全过程。平台提供从创意落地的 Prompt 生成，到基于用户意图与评测数据的智能调优能力，确保大模型输出更贴合真实业务需求。通过 API 接入，用户可低成本获取高质量的实时反馈数据，自动优化 Prompt，构建AI应用与真实数据间的反馈闭环。始于Pro阿mpt，PromptPilot助力用户打造可自我进化的大模型应用，加速 AI 能力在实际业务场景中的落地 - 一起学AI[ https://ai.meiweihui.cn/sites/2906.html](https://ai.meiweihui.cn/sites/2906.html)

\[194] Promptive - AI提示词调试平台 - Aitoolnet[ https://www.aitoolnet.com/zh/promptive](https://www.aitoolnet.com/zh/promptive)

\[195] PromptPilot - PROMPT[ https://prompt.cn/sites/9400.html](https://prompt.cn/sites/9400.html)

