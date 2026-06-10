#!/usr/bin/env python3
"""
Research Paper Agent - Orchestrates existing agents to produce a complete research paper.

Workflow:
  1. SearchAgent     → gather research and sources on the topic
  2. SummarizerAgent → condense and extract key findings
  3. PlanningAgent   → create structured paper outline
  4. CreativeAgent   → write each section with academic tone
  5. Supervisor      → compile and format the final paper
"""

import os
import sys
from typing import Dict, Any, List
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ResearchPaperAgent:
    """
    Orchestrates existing specialized agents to produce a complete research paper.
    Each agent contributes its domain expertise to a different phase of the paper.
    """

    def __init__(self, model_name: str = "llama-3.1-8b-instant"):
        # Compiler LLM - only used for final assembly
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=model_name,
            temperature=0.1,
            max_tokens=2000
        )
        self.agent_type = "research_paper"
        self.model = model_name

    def _compile_final_paper(self, topic: str, sections: Dict[str, str]) -> str:
        """Compile all agent outputs into a formatted research paper."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an academic editor. Compile the provided sections into a 
cohesive, well-formatted research paper. Ensure smooth transitions between sections, 
consistent academic tone, and proper structure. Do not add new content - only format 
and connect the existing sections."""),
            ("human", "{input}")
        ])
        chain = prompt | self.llm | StrOutputParser()

        sections_text = "\n\n".join([
            f"=== {name} ===\n{content}"
            for name, content in sections.items()
        ])

        compiled = chain.invoke({
            "input": f"Compile this research paper on '{topic}':\n\n{sections_text}"
        })

        return f"""# {topic.title()}

*Research Paper | Generated: {datetime.now().strftime("%B %d, %Y")}*
*Methodology: Multi-Agent Collaborative Research*

---

{compiled}

---

*This paper was generated through coordinated multi-agent research:*
- *SearchAgent: Topic research and source gathering*
- *SummarizerAgent: Research synthesis and key findings*
- *PlanningAgent: Paper structure and outline*
- *CreativeAgent: Academic content writing*
"""

    def process_task(self, topic: str, paper_type: str = "research") -> Dict[str, Any]:
        """
        Orchestrate all existing agents to produce a complete research paper.
        
        Pipeline:
          SearchAgent -> SummarizerAgent -> PlanningAgent -> CreativeAgent -> Compile
        """
        from langsmith import traceable

        @traceable(
            run_type="chain",
            name="ResearchPaperAgent - Multi-Agent Pipeline",
            metadata={
                "agent": "ResearchPaperAgent",
                "topic": topic[:100],
                "pipeline": "Search -> Summarize -> Plan -> Write -> Compile"
            },
            tags=["research_paper", "multi_agent_pipeline"]
        )
        def execute(topic_input: str):
            try:
                from agents.search_agent import SearchAgent
                from agents.summarizer_agent import SummarizerAgent
                from agents.planning_agent import PlanningAgent
                from agents.creative_agent import CreativeAgent

                sections = {}
                print(f"\n[ResearchPaperAgent] Starting multi-agent pipeline for: {topic_input[:60]}")

                # ── STEP 1: SearchAgent - Gather research ──────────────────────
                print("  [Step 1/4] SearchAgent: Gathering research...")
                search_agent = SearchAgent()
                search_result = search_agent.process_task(
                    f"Comprehensive research on: {topic_input}. "
                    f"Include key concepts, recent developments, statistics, and expert findings."
                )
                research_data = (
                    search_result.get("research_results") or
                    search_result.get("result") or
                    search_result.get("trend_analysis") or ""
                )
                sections["Research Findings"] = research_data
                print(f"     Done. ({len(research_data)} chars)")

                # ── STEP 2: SummarizerAgent - Synthesize findings ──────────────
                print("  [Step 2/4] SummarizerAgent: Synthesizing key findings...")
                summarizer = SummarizerAgent()
                summary_result = summarizer.process_task(
                    f"Extract and synthesize the key academic findings, theories, and insights for a research paper on: {topic_input}",
                    research_data[:3000]  # Pass research as content
                )
                key_findings = (
                    summary_result.get("summary") or
                    summary_result.get("result") or ""
                )
                sections["Key Findings & Literature Review"] = key_findings
                print(f"     Done. ({len(key_findings)} chars)")

                # ── STEP 3: PlanningAgent - Structure the paper ────────────────
                print("  [Step 3/4] PlanningAgent: Structuring paper outline...")
                planner = PlanningAgent()
                plan_result = planner.process_task(
                    f"Create a detailed academic research paper structure and methodology for: {topic_input}. "
                    f"Include: research objectives, methodology, analysis framework, and conclusion strategy.",
                    key_findings[:1000]
                )
                paper_structure = (
                    plan_result.get("result") or
                    plan_result.get("plan") or
                    plan_result.get("project_plan") or ""
                )
                sections["Methodology & Structure"] = paper_structure
                print(f"     Done. ({len(paper_structure)} chars)")

                # ── STEP 4: CreativeAgent - Write academic content ─────────────
                print("  [Step 4/4] CreativeAgent: Writing academic content...")
                creative = CreativeAgent()

                # Write Introduction
                intro_result = creative.process_task(
                    f"Write a formal academic Introduction section for a {paper_type} paper on: {topic_input}. "
                    f"Include background, problem statement, research objectives, and paper organization.",
                    f"Research context: {key_findings[:500]}"
                )
                introduction = (
                    intro_result.get("result") or
                    intro_result.get("creative_content") or
                    intro_result.get("blog_post") or ""
                )
                sections["Introduction"] = introduction

                # Write Discussion & Conclusion
                conclusion_result = creative.process_task(
                    f"Write a formal academic Discussion and Conclusion section for a {paper_type} paper on: {topic_input}. "
                    f"Synthesize findings, discuss implications, limitations, and future research directions.",
                    f"Key findings: {key_findings[:500]}\nStructure: {paper_structure[:300]}"
                )
                conclusion = (
                    conclusion_result.get("result") or
                    conclusion_result.get("creative_content") or
                    conclusion_result.get("blog_post") or ""
                )
                sections["Discussion & Conclusion"] = conclusion
                print(f"     Done. ({len(introduction) + len(conclusion)} chars)")

                # ── STEP 5: Compile final paper ────────────────────────────────
                print("  [Step 5/5] Compiling final paper...")
                final_paper = self._compile_final_paper(topic_input, sections)
                print(f"  [ResearchPaperAgent] Complete! Total: {len(final_paper)} chars\n")

                return {
                    "success": True,
                    "result": final_paper,
                    "sections_written": list(sections.keys()),
                    "agents_used": ["SearchAgent", "SummarizerAgent", "PlanningAgent", "CreativeAgent"],
                    "word_count": len(final_paper.split()),
                    "agent_type": self.agent_type,
                    "topic": topic_input,
                    "pipeline": "Search -> Summarize -> Plan -> Write -> Compile"
                }

            except Exception as e:
                import traceback
                print(f"[ResearchPaperAgent] Error: {e}")
                return {
                    "success": False,
                    "error": str(e),
                    "result": f"Research paper generation failed: {str(e)}",
                    "agent_type": self.agent_type
                }

        return execute(topic)

    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "agent_type": self.agent_type,
            "name": "ResearchPaperAgent",
            "description": "Orchestrates SearchAgent, SummarizerAgent, PlanningAgent, and CreativeAgent to produce complete research papers",
            "pipeline": [
                "SearchAgent: Topic research and source gathering",
                "SummarizerAgent: Research synthesis and key findings",
                "PlanningAgent: Paper structure and methodology",
                "CreativeAgent: Academic content writing",
                "Supervisor: Final compilation and formatting"
            ],
            "capabilities": [
                "End-to-end research paper generation",
                "Multi-agent collaborative writing",
                "Academic tone and structure",
                "Literature review synthesis",
                "Methodology and conclusion writing"
            ]
        }
