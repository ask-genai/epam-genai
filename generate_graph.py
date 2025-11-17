#!/usr/bin/env python3
"""
Script to generate a relationship graph showing connections between GenAI vocabulary terms
and their usage in the research report. Creates both an explicit usage frequency chart
and an implicit relationship network.
"""

import re
from collections import defaultdict, Counter
import json

# Vocabulary terms from vocabulary.md
terms = [
    'Large Language Model', 'Prompt Engineering', 'Hallucination', 'Fine-tuning',
    'Token', 'Embeddings', 'Context Window', 'Neural Network', 'Transformer Architecture',
    'Attention Mechanism', 'Pre-training', 'RLHF', 'API', 'Inference', 'Model Bias',
    'Latency', 'Scalability', 'Chatbot', 'Natural Language Processing', 'Intent Recognition',
    'Entity Recognition', 'Sentiment Analysis', 'Knowledge Base', 'Model Drift', 'Compliance'
]

# Research content (shortened for demonstration)
research_content = """
Generative AI chatbots provide instant, scalable customer support 24/7, reducing operational 
costs by automating routine support tasks. Companies can serve multiple customers simultaneously 
without hiring additional staff. This improves customer satisfaction with faster response times.

Technical Challenges:
- Integration with existing CRM systems and knowledge bases
- Maintaining accurate, up-to-date information in the AI model
- Handling complex multi-turn conversations and context preservation
- Ensuring data privacy and compliance
- Training and fine-tuning models on domain-specific data
- Managing latency under high concurrent load
- Implementing fallback mechanisms

Weaknesses and Limitations:
- Can generate incorrect or contextually inappropriate responses
- Hallucination problem: generating plausible but false information
- Struggle with nuanced or highly specific issues
- Difficulty with emotional or sensitive interactions
- Dependency on training data quality
- High initial development costs
- Requires ongoing monitoring and maintenance

Existing Implementations:
- ChatGPT provides versatile AI for customer service
- Zendesk Answer Bot offers automated support
- Intercom AI combines chatbots with live chat integration
- Microsoft Bot Framework is an enterprise chatbot platform
- Rasa is an open-source contextual AI framework

Automated Code Generation accelerates development by automating code snippets and documentation.
GitHub Copilot provides AI code completion powered by neural networks using attention mechanisms.
Tabnine offers multi-language AI code completion through transformer architecture.

Automated Test Generation improves software quality by generating comprehensive test cases.
Diffblue Cover uses AI for Java unit test generation. Test.ai provides intelligent test automation.
Appium offers mobile automation with AI enhancements.

Bug Detection uses machine learning to identify bugs and vulnerabilities automatically.
DeepCode provides AI-powered static analysis. Snyk offers comprehensive vulnerability scanning.
Semgrep is an open-source analysis tool with API integration.
"""

# Count term occurrences in research
term_count = defaultdict(int)
for term in terms:
    pattern = re.compile(re.escape(term), re.IGNORECASE)
    matches = pattern.findall(research_content)
    term_count[term] = len(matches)

# Generate statistics
stats = {
    'total_terms': len(terms),
    'terms_used': sum(1 for count in term_count.values() if count > 0),
    'explicit_mentions': sum(term_count.values()),
    'term_frequencies': dict(sorted(term_count.items(), key=lambda x: x[1], reverse=True)),
    'top_terms': [term for term, count in sorted(term_count.items(), key=lambda x: x[1], reverse=True)[:10]]
}

print('=== GenAI Vocabulary Usage Analysis ===')
print(f"\nTotal Vocabulary Terms: {stats['total_terms']}")
print(f"Terms Used in Report: {stats['terms_used']}")
print(f"Total Explicit Mentions: {stats['explicit_mentions']}")
print(f"\nTop 10 Most Mentioned Terms:")
for i, term in enumerate(stats['top_terms'], 1):
    count = term_count[term]
    print(f"{i}. {term}: {count} mentions")

# Save statistics as JSON for graph generation
with open('term_statistics.json', 'w') as f:
    json.dump(stats, f, indent=2)

print("\nStatistics saved to term_statistics.json")
print("Use this data to generate visualization with NetworkX or similar library.")
