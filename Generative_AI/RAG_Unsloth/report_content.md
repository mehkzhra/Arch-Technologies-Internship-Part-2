# Report Content — RAG with Unsloth Dynamic 4-bit Quantization

## Student Information

- Name: Mehak Zahra
- Internship: Arch Technologies
- Domain: Generative AI
- Month: 2
- Task: 3
- Phone: 03322136800

Add the student's email address on the final report front page.

## Objective

The project builds a Retrieval-Augmented Generation system that retrieves relevant information from a small document collection and supplies it to a quantized language model for grounded answer generation.

## Implementation

Sentence Transformers converts documents and questions into normalized semantic embeddings. Cosine similarity selects the most relevant document. The retrieved document and question are formatted using the Llama 3.2 chat template and passed to an Unsloth Dynamic 4-bit Llama 3.2 1B Instruct model. Dynamic 4-bit quantization reduces GPU memory usage while preserving sensitive model parameters more carefully than uniform quantization.

## Results

The system should retrieve the submission-guidelines document for a report-format question and generate an answer based on that source. Add actual screenshots of the Tesla T4 GPU, embedding shape, allocated GPU memory, retrieved filename, similarity score and final answer.

## Conclusion

This task demonstrates document embeddings, semantic retrieval, contextual prompting, Dynamic 4-bit inference and source-grounded text generation in Google Colab.

## Tools

Google Colab, Tesla T4, Python, Unsloth, Llama 3.2, PyTorch, Sentence Transformers and NumPy.
