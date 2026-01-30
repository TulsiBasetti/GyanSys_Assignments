## Invoice Data Extraction
This project extracts headers and line items from invoice PDF files using LangChain and Groq LLMs.
It processes invoices in bulk and saves the output as JSON files.

## Features
- Extracts structured data from invoice PDFs
- Uses Groq LLM (LLaMA 3.3 – 70B) for high-accuracy extraction
- Outputs is in JSON format
- Handles missing fields using null
- Processes multiple invoices in one run (currently 5 pdfs)
---
## Tech Stack
- Python
- LangChain
- Groq (ChatGroq)
- PyPDF
- dotenv
---
## Project Structure 
```bash
Invoice_Extractor
│
├── invoice_dataset/        # Input PDF invoices
├── Invoices_JSON/          # Output extracted JSON files
├── invoice_extractor.py                  # Main script                  
└── README.md
```
---
## Environment Setup
- Create a .env file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```
- Install dependencies:
```
pip install langchain langchain-groq pypdf python-dotenv
```
---
## Extraction Schema
The model extracts data in the following JSON format:
```json
{
  "invoice_number": "string | null",
  "invoice_date": "string | null",
  "vendor_name": "string | null",
  "customer_name": "string | null",
  "currency": "string | null",
  "line_items": [
    {
      "product_name": "string | null",
      "sub-category": "string | null",
      "category": "string | null",
      "product_id": "string | null",
      "quantity_or_duration": "string | null",
      "rate": "number | null",
      "amount": "number | null"
    }
  ],
  "subtotal": "number | null",
  "discount": "number | null",
  "shipping": "number | null",
  "total": "number | null"
}
```
---
## Architecture Diagram 

---
## How to Run
```
python invoice_extractor.py
```
## Future Enhancements
- Multi-page invoice support
- Database storage instead of JSON
- Add OCR to support scanned and image-based invoices.
- Use historical invoices or vendor-specific templates to improve extraction accuracy and consistency
- Generate confidence scores for each extracted field
- Implement LangGraph to handle multi-step extraction flows (OCR → parsing → validation → enrichment)
- Streamlit frontend for uploads & visualization
