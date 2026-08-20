# Generative AI Month 2 — Task 3

## RAG with Unsloth Dynamic 4-bit Quantization

This folder is designed for **Google Colab with a T4 GPU** because the student's local computer does not have an NVIDIA CUDA GPU and uses Python 3.13, which is unsuitable for this Unsloth setup.

### Files

- `GenAI_Task3_RAG_Unsloth_Dynamic_4bit.ipynb` — complete runnable Colab notebook
- `knowledge_base/submission_guidelines.txt` — sample RAG document
- `sample_output.txt` — expected output format
- `report_content.md` — material for the internship report
- `requirements.txt` — notebook dependencies

### How to Run

1. Open https://colab.research.google.com/.
2. Select `File → Upload notebook`.
3. Upload `GenAI_Task3_RAG_Unsloth_Dynamic_4bit.ipynb`.
4. Select `Runtime → Change runtime type → T4 GPU`.
5. Run every cell from top to bottom.
6. Capture screenshots of the GPU, embeddings, model information, retrieved source and final RAG answer.
7. Save through `File → Save a copy in Drive`, then download the executed `.ipynb`.

The notebook already applies the correct `llama-3.2` chat template to avoid the legacy-tokenizer response problem encountered during the first manual attempt.

### Expected Demonstration

The notebook retrieves `submission_guidelines.txt` and answers that the completed Word report should be converted into PDF format. The generated wording and similarity score may vary.
