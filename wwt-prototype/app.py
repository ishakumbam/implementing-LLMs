import os
import google.generativeai as genai
from flask import Flask, render_template, request

# Configure Gemini API
genai.configure(api_key="AIzaSyAsWQF-V3Z4yxn3yTkWq9pWMR0hLA157F4")

app = Flask(__name__)


def call_gemini(company_text):
    """
    Calls the Gemini API to generate consulting analysis.
    Returns the AI response text or an error message.
    """
    prompt = f"""You are an experienced solutions consultant at a company. Analyze the following company description and provide specific, actionable insights.

Company Description:
{company_text}

Based on this specific company, provide:

1. TOP 3 BUSINESS PROBLEMS
   - Identify the most critical challenges this specific company faces
   - Each problem should be 1-2 sentences
   - Be specific to their industry and situation

2. 3 DEMO IDEAS
   - Create 3 unique prototype/demo concepts tailored to solve their problems
   - Each demo should be 1-2 sentences
   - Focus on innovative, practical solutions

3. EMAIL OPENER
   - Write a personalized 2-3 sentence email opener
   - Reference specific problems from their description
   - Offer concrete help and value

Be specific and avoid generic responses. Tailor everything to THIS company's unique situation.
"""
    
    print("=== SENDING PROMPT TO GEMINI ===")
    print(f"Company text length: {len(company_text)} characters")
    print(f"First 200 chars: {company_text[:200]}...")
    print("=" * 50)
    
    try:
        # Initialize the Gemini model with generation config for more variation
        model = genai.GenerativeModel(
            'gemini-2.0-flash-exp',
            generation_config={
                'temperature': 1.0,  # Higher temperature for more variation (0.0 to 2.0)
                'top_p': 0.95,
                'top_k': 40,
                'max_output_tokens': 2048,
            }
        )
        
        # Generate content
        response = model.generate_content(prompt)
        
        print("=== GEMINI RESPONSE ===")
        print(f"Response length: {len(response.text)} characters")
        print(response.text)
        print("=" * 50)
        
        return response.text
    
    except Exception as e:
        error_msg = f"Error calling Gemini API: {str(e)}"
        print(error_msg)
        print(f"Full error: {repr(e)}")
        return f"Sorry, AI is having trouble right now. Error: {str(e)}"


@app.route("/", methods=["GET"])
def home():
    """Render the main form page"""
    return render_template("form.html")


@app.route("/result", methods=["POST"])
def result():
    """Process the form submission and display AI results"""
    # Get the company text from the form
    company_text = request.form.get("company_text", "")
    
    print("\n" + "=" * 60)
    print("NEW REQUEST RECEIVED")
    print("=" * 60)
    print(f"Input length: {len(company_text)} characters")
    print(f"Input preview: {company_text[:100]}...")
    print("=" * 60 + "\n")
    
    # Call Gemini API to get analysis
    ai_response = call_gemini(company_text)
    
    # Render the results page
    return render_template(
        "ai_result.html",
        company_text=company_text,
        ai_response=ai_response
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)