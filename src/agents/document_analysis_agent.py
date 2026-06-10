#!/usr/bin/env python3
"""
Document Analysis Agent - Multi-document analysis and cross-document insights
Handles: batch document processing, comparison, theme extraction, synthesis
"""

import os
from typing import Dict, Any, List
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class DocumentAnalysisAgent:
    """
    Analyzes multiple documents simultaneously.
    Extracts themes, compares content, identifies patterns across documents.
    """

    def __init__(self, model_name: str = "llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=model_name,
            temperature=0.1,
            max_tokens=3000
        )
        self.agent_type = "document_analysis"
        self.model = model_name

    def _invoke(self, system: str, human: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system),
            ("human", "{input}")
        ])
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"input": human})

    def analyze_single(self, content: str, doc_name: str = "Document") -> Dict[str, Any]:
        """Analyze a single document."""
        system = """You are an expert document analyst. Analyze the provided document and extract:
1. Main topics and themes
2. Key arguments or findings
3. Important data points or statistics
4. Author's conclusions
5. Strengths and limitations
Be thorough and structured."""

        analysis = self._invoke(system, f"Analyze this document titled '{doc_name}':\n\n{content[:3000]}")
        return {"doc_name": doc_name, "analysis": analysis, "length": len(content)}

    def compare_documents(self, analyses: List[Dict[str, Any]]) -> str:
        """Compare multiple document analyses."""
        system = """You are an expert comparative analyst. Compare the provided document analyses and identify:
1. Common themes across documents
2. Contradictions or disagreements
3. Complementary findings
4. Gaps in coverage
5. Overall synthesis and conclusions
Provide a comprehensive cross-document analysis."""

        docs_summary = "\n\n".join([
            f"**{a['doc_name']}**:\n{a['analysis'][:800]}"
            for a in analyses
        ])

        return self._invoke(system, f"Compare these {len(analyses)} documents:\n\n{docs_summary}")

    def extract_themes(self, analyses: List[Dict[str, Any]]) -> str:
        """Extract common themes across all documents."""
        system = """You are a thematic analysis expert. Extract and categorize the main themes 
across all provided documents. Group related concepts, identify recurring patterns, 
and provide a structured thematic map."""

        combined = "\n\n".join([f"{a['doc_name']}: {a['analysis'][:500]}" for a in analyses])
        return self._invoke(system, f"Extract themes from these documents:\n\n{combined}")

    def generate_synthesis_report(self, documents: List[Dict[str, str]], query: str = "") -> Dict[str, Any]:
        """Generate a comprehensive synthesis report from multiple documents."""
        analyses = []
        for doc in documents:
            analysis = self.analyze_single(doc["content"], doc.get("name", f"Document {len(analyses)+1}"))
            analyses.append(analysis)

        comparison = self.compare_documents(analyses)
        themes = self.extract_themes(analyses)

        report = f"""# Multi-Document Analysis Report

**Documents Analyzed**: {len(documents)}
**Analysis Date**: {datetime.now().strftime("%B %d, %Y")}
{f'**Research Query**: {query}' if query else ''}

---

## Individual Document Summaries

"""
        for a in analyses:
            report += f"### {a['doc_name']}\n{a['analysis']}\n\n---\n\n"

        report += f"""## Cross-Document Themes

{themes}

---

## Comparative Analysis

{comparison}

---

## Synthesis Conclusion

*This analysis synthesized {len(documents)} documents to provide comprehensive insights.*
"""
        return {
            "success": True,
            "result": report,
            "documents_analyzed": len(documents),
            "themes": themes,
            "comparison": comparison,
            "agent_type": self.agent_type
        }

    def process_task(self, task: str, documents: List[Dict[str, str]] = None, content: str = "") -> Dict[str, Any]:
        """Main entry point for document analysis tasks."""
        from langsmith import traceable

        @traceable(
            run_type="chain",
            name="DocumentAnalysisAgent - Process Task",
            metadata={"agent": "DocumentAnalysisAgent", "task": task[:100]},
            tags=["document_analysis", "multi_doc"]
        )
        def execute(task_input: str):
            try:
                # If documents list provided, do multi-doc analysis
                if documents and len(documents) > 0:
                    print(f"[DocumentAnalysisAgent] Analyzing {len(documents)} documents...")
                    return self.generate_synthesis_report(documents, task_input)

                # If single content string provided
                if content:
                    print(f"[DocumentAnalysisAgent] Analyzing single document...")
                    analysis = self.analyze_single(content, "Provided Document")
                    return {
                        "success": True,
                        "result": analysis["analysis"],
                        "agent_type": self.agent_type
                    }

                # No documents - analyze the task description itself as a topic
                system = """You are a document analysis expert. The user wants document analysis 
but hasn't provided documents yet. Explain what you can do and ask for documents, 
or provide a general analysis framework for their topic."""
                result = self._invoke(system, task_input)
                return {
                    "success": True,
                    "result": result,
                    "agent_type": self.agent_type
                }

            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "result": f"Document analysis failed: {str(e)}",
                    "agent_type": self.agent_type
                }

        return execute(task)

    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "agent_type": self.agent_type,
            "name": "DocumentAnalysisAgent",
            "description": "Multi-document analysis and cross-document insights",
            "capabilities": [
                "Batch document processing",
                "Cross-document comparison",
                "Theme extraction and mapping",
                "Synthesis report generation",
                "Pattern identification across documents"
            ]
        }
