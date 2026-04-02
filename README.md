# AI Student Performance Report Generator

An AI-powered Python tool that automatically generates 
performance reports for students using the Groq API.

## What it does
- Takes student names and marks as input
- Saves student data to a file
- Uses AI to generate a detailed performance report for each student
- Saves all reports to an output file

## Technologies Used
- Python
- Groq API
- LLaMA 3.3 70B model
- File Handling

## How to Run

1. Clone the repository
   git clone https://github.com/shivani-py/performance-generator.git

2. Install required libraries
   pip install groq python-dotenv

3. Create a .env file and add your Groq API key
   GROQ_API_KEY=your-api-key-here

4. Run the program
   python performance_generator.py

## Sample Output

**Student Name:** Shivani
**Score:** 95/100
**Grade:** Excellent

**Strengths:**
- Academic Excellence
- Attention to Detail
- Critical Thinking

**Areas for Improvement:**
- Continued Effort
- Diverse Skill Set

**Rating:** 5/5
