import frontmatter
import markdown
import os
import json
import logging
import re

# Add some logging functionality
logging.basicConfig(level=logging.INFO)

# Directory containing your FAQ Markdown files
faq_directory = os.path.join(os.getcwd())

# Initialize Markdown parser
md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'meta'])

heading_pattern = re.compile(r'^###\s+(.*)', re.MULTILINE)

# List to hold all FAQ entries
faq_entries = []

# Iterate over all Markdown files in the directory
for filename in os.listdir(faq_directory):
    #filename = os.listdir(faq_directory)[1]
    logging.info(f"Processing file: {filename}")
    if filename.endswith('.md') and filename != '_index.md':
        filepath = os.path.join(faq_directory, filename)
        #f = open(filepath, 'r', encoding='utf-8')
        with open(filepath, 'r', encoding='utf-8') as f:
            # Parse the front matter and content
            #text = f.read()
            post = frontmatter.load(f)
            tags = [post.get('title', 'FAQ')]  # Use the page title as a tag
            content = post.content
            f.close()

            # Find all questions and their positions
            questions = [(m.start(), m.end(), m.group(1)) for m in heading_pattern.finditer(content)]

            # Append an end position for the last answer
            questions.append((len(content), len(content), ''))

             # Extract question-answer pairs
            for i in range(len(questions) - 1):
                #i = 0
                q_start = questions[i][1]
                q_end = questions[i + 1][0]
                question_title = questions[i][2]
                answer_text = content[q_start:q_end].strip()

                # Convert Markdown to HTML
                question_html = md.convert(f"### {question_title}")
                answer_html = md.convert(answer_text)

                faq_entries.append({
                    'QuestionTitle': question_html.strip(),
                    'QuestionBody': '',
                    'Tags': tags,
                    'Answer': answer_html.strip()
                })

            md.reset()

# Output the FAQ entries as JSON
with open('faqs.json', 'w', encoding='utf-8') as outfile:
    json.dump(faq_entries, outfile, ensure_ascii=False, indent=2)
logging.info(f"Extracted {len(faq_entries)} FAQ entries in file faqs.json")