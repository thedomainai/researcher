# -*- coding: utf-8 -*-
"""llm/ コーパスのトピック定義(fetch_llm.py が読み込む)。

方針(2026-10-01 決定):
  - 目的は LLM の専門家になること。優先順は 研究者 > 実装者 > 導入・評価を担う人。
  - 領域は 8 つ。エージェントは独立した大領域として扱う。
  - 直近 2024 年以降は recent_queries で重点的に取り、定番は landmarks で名指しする。
  - 複数トピックにまたがる文献は index.jsonl の topics に複数付く(ファイルは先頭トピックに 1 つ)。

構造は fetch_reference.py の TOPICS と同じ:
  label / definition / queries / recent_queries / cites_terms / landmarks[(タイトル, 役割)]
  役割: "" / "refs"(参考文献を辿る) / "cites"(引用元を辿る) / "refs,cites"
"""

TOPICS = {
    "foundations": {
        "label": "基盤: アーキテクチャ・事前学習・長文脈・推論高速化",
        "definition": (
            "含む: Transformer とその改良(Attention の効率化、位置エンコーディング、MoE、状態空間モデル)。"
            "大規模言語モデルの事前学習(スケーリング則、データの収集・品質・重複排除・配合、トークナイザ)。"
            "長文脈(文脈長の拡張、長文脈での性能劣化)。"
            "推論の高速化と配備(量子化、蒸留、投機的デコーディング、KV キャッシュ、サービング)。"
            "主要なオープン・クローズドモデルの技術報告。LLM 全般のサーベイ。\n"
            "除く: 言語モデルを使わない画像・音声・ロボットの深層学習。ハードウェア設計だけの論文。"
            "特定の下流タスクに言語モデルを当てはめただけの応用研究。"
        ),
        "queries": [
            '"large language model" AND (pretraining OR "pre-training" OR "scaling law" OR "scaling laws")',
            'transformer AND ("attention mechanism" OR "mixture of experts" OR "state space model" OR "positional encoding") AND "language model"',
            '"large language model" AND (quantization OR distillation OR "speculative decoding" OR "KV cache" OR "inference efficiency")',
            '"long context" AND "language model"',
        ],
        "recent_queries": [
            '"large language model" AND (architecture OR pretraining OR "scaling law" OR "mixture of experts")',
            '"long-context" AND ("language model" OR LLM)',
            '(LLM OR "language model") AND (quantization OR "speculative decoding" OR "KV cache" OR "inference serving")',
        ],
        "cites_terms": '("language model" OR "large language model" OR LLM OR transformer)',
        "landmarks": [
            ("Attention Is All You Need", "refs,cites"),
            ("A Survey of Large Language Models", "refs,cites"),
            ("BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", ""),
            ("Language Models are Few-Shot Learners", "refs,cites"),
            ("Language Models are Unsupervised Multitask Learners", ""),
            ("Scaling Laws for Neural Language Models", "cites"),
            ("Training Compute-Optimal Large Language Models", ""),
            ("Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", ""),
            ("PaLM: Scaling Language Modeling with Pathways", ""),
            ("GPT-4 Technical Report", ""),
            ("LLaMA: Open and Efficient Foundation Language Models", ""),
            ("Llama 2: Open Foundation and Fine-Tuned Chat Models", ""),
            ("The Llama 3 Herd of Models", ""),
            ("DeepSeek-V3 Technical Report", ""),
            ("Gemini: A Family of Highly Capable Multimodal Models", ""),
            ("RoFormer: Enhanced Transformer with Rotary Position Embedding", ""),
            ("FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", ""),
            ("Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity", ""),
            ("Mixtral of Experts", ""),
            ("Mamba: Linear-Time Sequence Modeling with Selective State Spaces", ""),
            ("Efficiently Modeling Long Sequences with Structured State Spaces", ""),
            ("Efficient Memory Management for Large Language Model Serving with PagedAttention", ""),
            ("Fast Inference from Transformers via Speculative Decoding", ""),
            ("LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale", ""),
            ("GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", ""),
            ("AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", ""),
            ("Distilling the Knowledge in a Neural Network", ""),
            ("Neural Machine Translation of Rare Words with Subword Units", ""),
            ("Lost in the Middle: How Language Models Use Long Contexts", ""),
            ("The Pile: An 800GB Dataset of Diverse Text for Language Modeling", ""),
            ("Deduplicating Training Data Makes Language Models Better", ""),
            ("Emergent Abilities of Large Language Models", ""),
        ],
    },
    "post_training": {
        "label": "学習後の調整: 指示チューニング・選好学習・推論モデル・効率的微調整",
        "definition": (
            "含む: 指示チューニング(SFT、合成データによる指示生成)。"
            "選好学習(RLHF、DPO とその派生、AI フィードバック、報酬モデル)。"
            "推論モデルの学習(検証可能な報酬による強化学習、過程報酬、テスト時計算量のスケーリング)。"
            "効率的な微調整(LoRA 系、アダプタ)、モデルマージ、継続学習・破滅的忘却。"
            "RLHF の限界・報酬ハッキングの手法面。\n"
            "除く: 言語モデルを使わない強化学習。ロボット制御のための報酬設計。"
            "安全性の評価や脱獄そのもの(safety_interp に属する)。"
        ),
        "queries": [
            '"reinforcement learning from human feedback" OR RLHF OR "preference optimization" OR "direct preference optimization"',
            '("instruction tuning" OR "instruction-tuning" OR "supervised fine-tuning") AND "language model"',
            '("parameter-efficient fine-tuning" OR LoRA OR "low-rank adaptation") AND ("language model" OR LLM)',
            '"reward model" AND ("language model" OR LLM)',
        ],
        "recent_queries": [
            '(RLHF OR DPO OR "preference optimization" OR "reward model") AND (LLM OR "language model")',
            '("reinforcement learning" AND ("verifiable rewards" OR "reasoning model" OR "test-time compute") AND (LLM OR "language model"))',
            '("post-training" OR "instruction tuning" OR "model merging" OR "continual learning") AND (LLM OR "language model")',
        ],
        "cites_terms": '("language model" OR LLM OR RLHF OR "human feedback" OR "instruction")',
        "landmarks": [
            ("Training language models to follow instructions with human feedback", "refs,cites"),
            ("Deep reinforcement learning from human preferences", ""),
            ("Fine-Tuning Language Models from Human Preferences", ""),
            ("Learning to summarize from human feedback", ""),
            ("Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback", ""),
            ("Constitutional AI: Harmlessness from AI Feedback", ""),
            ("Direct Preference Optimization: Your Language Model is Secretly a Reward Model", "cites"),
            ("KTO: Model Alignment as Prospect Theoretic Optimization", ""),
            ("Proximal Policy Optimization Algorithms", ""),
            ("Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback", "refs"),
            ("Finetuned Language Models Are Zero-Shot Learners", ""),
            ("Scaling Instruction-Finetuned Language Models", ""),
            ("Self-Instruct: Aligning Language Models with Self-Generated Instructions", ""),
            ("LIMA: Less Is More for Alignment", ""),
            ("Tulu 3: Pushing Frontiers in Open Language Model Post-Training", ""),
            ("LoRA: Low-Rank Adaptation of Large Language Models", "cites"),
            ("QLoRA: Efficient Finetuning of Quantized LLMs", ""),
            ("Parameter-Efficient Transfer Learning for NLP", ""),
            ("Let's Verify Step by Step", ""),
            ("DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", ""),
            ("DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", ""),
            ("Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters", ""),
            ("STaR: Bootstrapping Reasoning With Reasoning", ""),
            ("Editing Models with Task Arithmetic", ""),
            ("Overcoming catastrophic forgetting in neural networks", ""),
        ],
    },
    "elicitation": {
        "label": "能力の引き出し: プロンプト・文脈内学習・RAG・ツール・構造化出力・マルチモーダル",
        "definition": (
            "含む: プロンプト設計と推論の引き出し(思考の連鎖、自己一貫性、探索型の推論)。"
            "文脈内学習の実践面(デモの選び方、感度)。"
            "検索拡張生成(検索器、チャンク分割、再ランキング、グラウンディング、サーベイ)。"
            "ツール利用・関数呼び出し(単体の技術としての扱い)、構造化出力・制約付きデコーディング。"
            "マルチモーダル LLM(視覚・音声・動画の入力)。\n"
            "除く: 自律エージェントの設計全般(agents に属する)。文脈内学習の理論的説明(theory_cognition)。"
            "RAG を使わない単なる検索・推薦システムの研究。"
        ),
        "queries": [
            '("chain-of-thought" OR "chain of thought" OR "prompt engineering" OR "prompting") AND ("language model" OR LLM)',
            '("retrieval-augmented generation" OR RAG) AND ("language model" OR LLM)',
            '("tool use" OR "tool learning" OR "function calling") AND ("language model" OR LLM)',
            '("multimodal large language model" OR "vision-language model" OR "visual instruction tuning")',
        ],
        "recent_queries": [
            '("retrieval-augmented generation" OR RAG) AND (LLM OR "language model")',
            '("chain-of-thought" OR "reasoning" OR "prompting") AND (LLM OR "large language model") AND (technique OR method OR framework)',
            '("multimodal large language model" OR MLLM OR "vision-language model")',
            '("structured output" OR "constrained decoding" OR "function calling" OR "tool calling") AND (LLM OR "language model")',
        ],
        "cites_terms": '("language model" OR LLM OR prompting OR "retrieval-augmented")',
        "landmarks": [
            ("Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "refs,cites"),
            ("Large Language Models are Zero-Shot Reasoners", ""),
            ("Self-Consistency Improves Chain of Thought Reasoning in Language Models", ""),
            ("Tree of Thoughts: Deliberate Problem Solving with Large Language Models", ""),
            ("Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing", "refs"),
            ("The Power of Scale for Parameter-Efficient Prompt Tuning", ""),
            ("Making Pre-trained Language Models Better Few-shot Learners", ""),
            ("Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?", ""),
            ("A Survey on In-Context Learning", "refs"),
            ("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", "refs,cites"),
            ("Dense Passage Retrieval for Open-Domain Question Answering", ""),
            ("Improving language models by retrieving from trillions of tokens", ""),
            ("REPLUG: Retrieval-Augmented Black-Box Language Models", ""),
            ("Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection", ""),
            ("Retrieval-Augmented Generation for Large Language Models: A Survey", "refs"),
            ("Toolformer: Language Models Can Teach Themselves to Use Tools", ""),
            ("Gorilla: Large Language Model Connected with Massive APIs", ""),
            ("Efficient Guided Generation for Large Language Models", ""),
            ("Visual Instruction Tuning", ""),
            ("Learning Transferable Visual Models From Natural Language Supervision", ""),
            ("Flamingo: a Visual Language Model for Few-Shot Learning", ""),
            ("Robust Speech Recognition via Large-Scale Weak Supervision", ""),
        ],
    },
    "evaluation": {
        "label": "評価: ベンチマーク・LLM-as-a-judge・汚染・統計的妥当性・不確実性",
        "definition": (
            "含む: LLM のベンチマークの設計と提案(知識・推論・数学・コード・長文脈・エージェント)。"
            "LLM を評価者に使う手法とそのバイアス、人手評価との一致。"
            "ベンチマーク汚染・飽和・再現性・プロンプト感度、評価の統計的妥当性(分散・信頼区間)。"
            "動的・検証可能な環境による評価、不確実性の較正、評価に関するサーベイ。\n"
            "除く: LLM を使わない従来の機械学習のベンチマーク。"
            "特定の応用領域(医療・法務)での単発の精度報告(applications に属する)。"
            "安全性・有害性の評価(safety_interp に属する。ただし評価方法論の論点を含むなら含める)。"
        ),
        "queries": [
            '("benchmark" OR "evaluation") AND ("large language model" OR LLM) AND (reasoning OR knowledge OR capability)',
            '"LLM-as-a-judge" OR "LLM as a judge" OR "language model as judge"',
            '("data contamination" OR "benchmark contamination" OR "benchmark saturation") AND ("language model" OR LLM)',
            '("calibration" OR "uncertainty estimation" OR "confidence") AND ("large language model" OR LLM)',
        ],
        "recent_queries": [
            '(benchmark OR "evaluation framework" OR "evaluating") AND ("large language model" OR LLM) AND (agent OR reasoning OR "long-context")',
            '("LLM-as-a-judge" OR "LLM judge" OR "automatic evaluation") AND (LLM OR "language model")',
            '("benchmark contamination" OR "evaluation validity" OR "statistical" OR "reproducibility") AND (LLM OR "language model") AND (evaluation OR benchmark)',
        ],
        "cites_terms": '("language model" OR LLM OR benchmark OR evaluation)',
        "landmarks": [
            ("Measuring Massive Multitask Language Understanding", "cites"),
            ("Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", "cites"),
            ("Holistic Evaluation of Language Models", "refs"),
            ("Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models", ""),
            ("A Survey on Evaluation of Large Language Models", "refs"),
            ("Evaluating Large Language Models Trained on Code", ""),
            ("SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", ""),
            ("Training Verifiers to Solve Math Word Problems", ""),
            ("Measuring Mathematical Problem Solving With the MATH Dataset", ""),
            ("TruthfulQA: Measuring How Models Mimic Human Falsehoods", ""),
            ("GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding", ""),
            ("SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems", ""),
            ("Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", ""),
            ("GPQA: A Graduate-Level Google-Proof Q&A Benchmark", ""),
            ("Humanity's Last Exam", ""),
            ("Are Emergent Abilities of Large Language Models a Mirage?", ""),
            ("Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design", ""),
            ("Rethinking Benchmark and Contamination for Language Models with Rephrased Samples", ""),
            ("LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code", ""),
            ("G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment", ""),
            ("Large Language Models are not Fair Evaluators", ""),
            ("RULER: What's the Real Context Size of Your Long-Context Language Models?", ""),
            ("Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", ""),
            ("Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators", ""),
            ("Language Models (Mostly) Know What They Know", ""),
            ("AgentBench: Evaluating LLMs as Agents", ""),
            ("GAIA: a benchmark for General AI Assistants", ""),
        ],
    },
    "safety_interp": {
        "label": "信頼性・安全性・解釈: ハルシネーション・アライメント・攻撃・解釈可能性",
        "definition": (
            "含む: ハルシネーションの検出・抑制・事実性。"
            "アライメント(欺瞞、報酬ハッキング、迎合、スケーラブルな監督、思考の連鎖の忠実性)。"
            "敵対的攻撃(脱獄、プロンプトインジェクション、データ汚染・バックドア)。"
            "機械的解釈可能性(回路、特徴量・スパースオートエンコーダ、表現工学、知識編集)。"
            "プライバシー・記憶・著作権、バイアス・公平性、頑健性。\n"
            "除く: LLM を使わない機械学習の公平性・頑健性。"
            "AI ガバナンスや規制の政策論(既存の ai_governance 分野が担当)。"
            "一般的な性能評価のベンチマーク(evaluation に属する)。"
        ),
        "queries": [
            '"hallucination" AND ("large language model" OR LLM OR "language model")',
            '("jailbreak" OR "prompt injection" OR "adversarial attack") AND ("large language model" OR LLM)',
            '("mechanistic interpretability" OR "sparse autoencoder" OR "interpretability") AND ("language model" OR LLM)',
            '("alignment" OR "deceptive" OR "sycophancy" OR "reward hacking") AND ("large language model" OR LLM)',
        ],
        "recent_queries": [
            '(hallucination OR factuality) AND (LLM OR "large language model")',
            '(jailbreak OR "prompt injection" OR "red teaming" OR "backdoor") AND (LLM OR "large language model")',
            '("mechanistic interpretability" OR "sparse autoencoder" OR "circuit" OR "representation") AND (LLM OR "language model") AND (interpretability OR interpretable)',
            '("AI alignment" OR "scalable oversight" OR "deceptive alignment" OR "misalignment") AND (LLM OR "language model")',
        ],
        "cites_terms": '("language model" OR LLM OR hallucination OR jailbreak OR interpretability)',
        "landmarks": [
            ("Survey of Hallucination in Natural Language Generation", "refs"),
            ("A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions", "refs"),
            ("SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models", ""),
            ("Language Models (Mostly) Know What They Know", ""),
            ("Universal and Transferable Adversarial Attacks on Aligned Language Models", ""),
            ("Jailbroken: How Does LLM Safety Training Fail?", ""),
            ("Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", ""),
            ("Red Teaming Language Models with Language Models", ""),
            ("Extracting Training Data from Large Language Models", ""),
            ("Quantifying Memorization Across Neural Language Models", ""),
            ("Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training", ""),
            ("Alignment faking in large language models", ""),
            ("Frontier Models are Capable of In-context Scheming", ""),
            ("Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs", ""),
            ("Towards Understanding Sycophancy in Language Models", ""),
            ("Measuring Faithfulness in Chain-of-Thought Reasoning", ""),
            ("Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting", ""),
            ("Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision", ""),
            ("Discovering Language Model Behaviors with Model-Written Evaluations", ""),
            ("A Mathematical Framework for Transformer Circuits", ""),
            ("In-context Learning and Induction Heads", ""),
            ("Towards Monosemanticity: Decomposing Language Models With Dictionary Learning", ""),
            ("Sparse Autoencoders Find Highly Interpretable Features in Language Models", ""),
            ("Scaling and evaluating sparse autoencoders", ""),
            ("Representation Engineering: A Top-Down Approach to AI Transparency", ""),
            ("Locating and Editing Factual Associations in GPT", ""),
            ("Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small", ""),
            ("On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?", ""),
            ("Concrete Problems in AI Safety", ""),
            ("The Reversal Curse: LLMs trained on \"A is B\" fail to learn \"B is A\"", ""),
        ],
    },
    "theory_cognition": {
        "label": "理論・認知: 文脈内学習の理論・推論の限界・世界モデル・人間との比較",
        "definition": (
            "含む: 文脈内学習・創発・グロッキングの理論的説明。"
            "Transformer の表現力と計算量の限界(思考の連鎖の表現力、構成性の失敗)。"
            "LLM の内部の世界モデル・空間と時間の表現。"
            "人間の認知との比較(心の理論、言語と思考の分離、認知バイアス)。"
            "LLM による人間の行動のシミュレーション・社会科学への応用の妥当性。\n"
            "除く: 性能向上のための手法提案だけの論文。ベンチマークの提案(evaluation)。"
            "認知科学の既存研究で LLM に触れていないもの(既存の cognitive_science 分野が担当)。"
        ),
        "queries": [
            '("in-context learning" OR "emergent abilities" OR "grokking") AND (theory OR theoretical OR mechanism OR explanation)',
            '("theory of mind" OR "cognitive" OR "human-like") AND ("large language model" OR LLM) AND (evaluation OR comparison OR psychology)',
            '("world model" OR "world representation") AND ("language model" OR LLM)',
            '("expressive power" OR "limitations" OR "compositionality") AND (transformer OR "language model")',
        ],
        "recent_queries": [
            '("theory of mind" OR "cognitive science" OR "psychology") AND ("large language model" OR LLM)',
            '("limitations" OR "reasoning failure" OR "expressivity") AND (transformer OR "large language model" OR LLM) AND (theoretical OR theory)',
            '("simulate" OR "simulation of human") AND ("large language model" OR LLM) AND ("human behavior" OR "survey respondents" OR "social science")',
        ],
        "cites_terms": '("language model" OR LLM OR transformer OR "in-context")',
        "landmarks": [
            ("Sparks of Artificial General Intelligence: Early experiments with GPT-4", "refs"),
            ("What Can Transformers Learn In-Context? A Case Study of Simple Function Classes", ""),
            ("An Explanation of In-context Learning as Implicit Bayesian Inference", ""),
            ("Transformers learn in-context by gradient descent", ""),
            ("The Expressive Power of Transformers with Chain of Thought", ""),
            ("Chain of Thought Empowers Transformers to Solve Inherently Serial Problems", ""),
            ("Faith and Fate: Limits of Transformers on Compositionality", ""),
            ("The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity", ""),
            ("Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets", ""),
            ("Language Models Represent Space and Time", ""),
            ("Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task", ""),
            ("Dissociating language and thought in large language models", ""),
            ("Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks", ""),
            ("Theory of Mind May Have Spontaneously Emerged in Large Language Models", ""),
            ("Using cognitive psychology to understand GPT-3", ""),
            ("Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in ChatGPT", ""),
            ("Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data", ""),
            ("Talking About Large Language Models", ""),
            ("Out of One, Many: Using Language Models to Simulate Human Samples", ""),
            ("Can Large Language Models Transform Computational Social Science?", ""),
            ("Generative Agents: Interactive Simulacra of Human Behavior", ""),
        ],
    },
    "applications": {
        "label": "応用・実装・社会: ソフトウェア工学・科学・専門領域・生産性・運用",
        "definition": (
            "含む: コード生成とソフトウェア工学への適用(生成・テスト・レビュー・修正)。"
            "科学発見の自動化(数学・化学・生物)。医療・法務・金融などの専門領域での LLM の能力と限界。"
            "生成 AI の生産性・労働市場・経済への影響の実証。"
            "LLM アプリケーションの運用(LLMOps)、コストと遅延の設計。\n"
            "除く: 領域特化モデルでも LLM を使わない従来の機械学習の応用。"
            "AI 規制の政策論そのもの(ai_governance)。エージェント設計の一般論(agents)。"
        ),
        "queries": [
            '("code generation" OR "program synthesis" OR "software engineering") AND ("large language model" OR LLM)',
            '("large language model" OR LLM OR ChatGPT) AND (clinical OR medical OR legal OR financial) AND (evaluation OR performance)',
            '("generative AI" OR "large language model" OR ChatGPT) AND (productivity OR "labor market" OR workers) AND (experiment OR evidence)',
            '("scientific discovery" OR "automated research" OR "AI scientist") AND ("large language model" OR LLM)',
        ],
        "recent_queries": [
            '("large language model" OR LLM) AND ("software engineering" OR "code generation" OR "code review" OR "program repair")',
            '("generative AI" OR LLM OR "large language model") AND (productivity OR "field experiment" OR "randomized" OR "labor market")',
            '(LLM OR "large language model") AND (clinical OR medical OR legal OR "scientific discovery" OR "scientific research")',
            '(LLMOps OR "LLM application" OR "production deployment" OR "cost" ) AND (LLM OR "large language model") AND (system OR engineering)',
        ],
        "cites_terms": '("language model" OR LLM OR ChatGPT OR "generative AI")',
        "landmarks": [
            ("Large Language Models for Software Engineering: A Systematic Literature Review", "refs"),
            ("Challenges and Applications of Large Language Models", "refs"),
            ("Evaluating Large Language Models Trained on Code", ""),
            ("Competition-level code generation with AlphaCode", ""),
            ("Code Llama: Open Foundation Models for Code", ""),
            ("SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", ""),
            ("Large Language Models Encode Clinical Knowledge", ""),
            ("Capabilities of GPT-4 on Medical Challenge Problems", ""),
            ("Towards Expert-Level Medical Question Answering with Large Language Models", ""),
            ("BloombergGPT: A Large Language Model for Finance", ""),
            ("Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models", ""),
            ("Mathematical discoveries from program search with large language models", ""),
            ("The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery", ""),
            ("Autonomous chemical research with large language models", ""),
            ("Experimental evidence on the productivity effects of generative artificial intelligence", ""),
            ("GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models", ""),
            ("Generative AI at Work", ""),
            ("The Impact of AI on Developer Productivity: Evidence from GitHub Copilot", ""),
            ("Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality", ""),
        ],
    },
    "agents": {
        "label": "AI エージェント: 設計・計画・記憶・ツール・マルチエージェント・自己改善・評価・安全",
        "definition": (
            "含む: LLM を用いた自律エージェントの設計(推論と行動のループ、計画、反省、自己改善)。"
            "記憶・文脈管理、ツール利用とコンピュータ操作(GUI・ブラウザ・コード実行)。"
            "マルチエージェント(役割分担、協調・議論、失敗モード)。"
            "エージェントの訓練環境と強化学習、エージェント用ベンチマークと軌跡の評価。"
            "エージェントの権限設計・不可逆操作の防止・人間の関与点・ツール経由の攻撃。"
            "エージェントのコーディング・リサーチ・業務自動化への応用。\n"
            "除く: 従来の強化学習エージェント(LLM を使わないもの)。ロボット制御だけの論文。"
            "単発のプロンプト技法やツール呼び出しの単体技術(elicitation に属する)。"
        ),
        "queries": [
            '("LLM agent" OR "LLM-based agent" OR "language agent" OR "autonomous agent") AND ("large language model" OR LLM)',
            '("multi-agent" OR "multi agent") AND ("large language model" OR LLM)',
            '("agent memory" OR "agentic" OR "computer use" OR "web agent" OR "GUI agent") AND ("language model" OR LLM)',
            '("self-improving" OR "self-evolving" OR "self-refine" OR "reflection") AND (agent OR agents) AND ("language model" OR LLM)',
        ],
        "recent_queries": [
            '("LLM agent" OR "LLM-based agent" OR "AI agent" OR "agentic") AND (LLM OR "large language model")',
            '("multi-agent system" OR "multi-agent collaboration" OR "multi-agent") AND (LLM OR "large language model")',
            '("agent benchmark" OR "agent evaluation" OR "computer-use agent" OR "web agent" OR "coding agent") AND (LLM OR "language model")',
            '(agent OR agents) AND (safety OR security OR "prompt injection" OR "permission" OR "human oversight") AND (LLM OR "language model")',
            '(agent OR agents) AND ("memory" OR "context engineering" OR "planning" OR "self-evolving") AND (LLM OR "language model")',
        ],
        "cites_terms": '("language model" OR LLM OR agent OR agents)',
        "landmarks": [
            ("ReAct: Synergizing Reasoning and Acting in Language Models", "refs,cites"),
            ("Reflexion: Language Agents with Verbal Reinforcement Learning", ""),
            ("Self-Refine: Iterative Refinement with Self-Feedback", ""),
            ("Large Language Models Can Self-Improve", ""),
            ("Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents", ""),
            ("A Survey on Large Language Model based Autonomous Agents", "refs,cites"),
            ("The Rise and Potential of Large Language Model Based Agents: A Survey", "refs"),
            ("Cognitive Architectures for Language Agents", ""),
            ("Large Language Model based Multi-Agents: A Survey of Progress and Challenges", "refs"),
            ("Generative Agents: Interactive Simulacra of Human Behavior", ""),
            ("Voyager: An Open-Ended Embodied Agent with Large Language Models", ""),
            ("MemGPT: Towards LLMs as Operating Systems", ""),
            ("AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", ""),
            ("MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework", ""),
            ("CAMEL: Communicative Agents for \"Mind\" Exploration of Large Language Model Society", ""),
            ("ChatDev: Communicative Agents for Software Development", ""),
            ("Improving Factuality and Reasoning in Language Models through Multiagent Debate", ""),
            ("Why Do Multi-Agent LLM Systems Fail?", ""),
            ("HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face", ""),
            ("Tool Learning with Foundation Models", ""),
            ("ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs", ""),
            ("Executable Code Actions Elicit Better LLM Agents", ""),
            ("OpenHands: An Open Platform for AI Software Developers as Generalist Agents", ""),
            ("WebArena: A Realistic Web Environment for Building Autonomous Agents", ""),
            ("Mind2Web: Towards a Generalist Agent for the Web", ""),
            ("OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments", ""),
            ("Do As I Can, Not As I Say: Grounding Language in Robotic Affordances", ""),
        ],
    },
}

GATE_SYSTEM = (
    "あなたは大規模言語モデル(LLM)研究の文献レビュアーです。"
    "与えられた主題の定義に対して、各候補文献が LLM の専門家の学習・参照に使えるかを判定します。"
    "回答は JSON 配列のみ。JSON 以外は出力しないでください。"
)

GATE_USER = """主題: {label}
{definition}

判定区分:
- core: 主題の中心的な手法・理論・証拠を直接扱う(この主題を学ぶとき最初に読むべき文献)
- supporting: 主題に関連し、文脈や補強として引用できる
- off_topic: 主題と無関係、LLM を扱っていない、または語が別の意味で使われている

候補:
{candidates}

各候補について次の形式で返してください(JSON 配列のみ):
[{{"id": "W...", "verdict": "core|supporting|off_topic", "reason": "20〜40字の理由"}}]"""
